"""
calendar_logic.py
Living Spiral — 13-Moon / Dreamspell calendar engine.

Implements the Dreamspell Kin count and 13-Moon calendar as defined by
the Foundation for the Law of Time. See: https://www.lawoftime.org

Public API
----------
get_kin_for_date(year, month, day) -> KinData
    Calculate the galactic signature (Kin) for any Gregorian date.

get_today_moon_data() -> MoonData | DayOutOfTimeData
    Calculate today's full 13-Moon calendar position and daily affirmation.

Both functions raise InvalidDateError for out-of-range or malformed inputs.
"""

from __future__ import annotations

from datetime import date
from typing import TypedDict, Union

from .constants import (
    CREATIVE_POWERS,
    GALACTIC_ACTIVATION_PORTALS,
    MOON_QUESTIONS,
    MOONS,
    MONTH_TABLE,
    PLASMAS,
    POWERS_OF_THE_SEAL,
    SEAL_ACTIONS,
    SEAL_COLORS,
    SEAL_FUNCTIONS,
    SEAL_POWERS,
    SEALS,
    SELF_GUIDED_TONES,
    TONE_ACTIONS,
    TONE_FUNCTIONS,
    TONE_NAMES,
    TONES,
    YEAR_TABLE,
    MIN_YEAR,
    MAX_YEAR,
)
from .exceptions import InvalidDateError

__all__ = ["get_kin_for_date", "get_today_moon_data", "KinData", "MoonData", "DayOutOfTimeData", "OraclePartner"]


# ---------------------------------------------------------------------------
# Return-type definitions
# ---------------------------------------------------------------------------

class OraclePartner(TypedDict):
    """One of the four oracle partners (analog, antipode, occult, guide)."""
    kin_number: int
    tone_number: int
    seal_number: int
    tone: str
    seal: str
    seal_color: str


class KinData(TypedDict):
    """Return type for get_kin_for_date()."""
    kin_number: int         # 1–260
    tone_number: int        # 1–13
    seal_number: int        # 1–20
    tone: str               # e.g. "Resonant"
    seal: str               # e.g. "Yellow Seed"
    seal_color: str         # "Red", "White", "Blue", or "Yellow"
    guide: str              # guide seal name, e.g. "Yellow Warrior"
    analog: OraclePartner   # helping partner — same tone, seal +10
    antipode: OraclePartner # challenge partner — tone +6, seal +10
    occult: OraclePartner   # hidden power — tone + seal = 14/21
    is_galactic_portal: bool
    affirmation: str        # Full five-line (or six-line) code spell


class MoonData(TypedDict):
    """Return type for get_today_moon_data() on a normal day."""
    is_day_out_of_time: bool   # Always False here
    moon_number: int            # 1–13
    moon_name: str              # e.g. "Resonant"
    moon: str                   # e.g. "7 Resonant Moon"
    moon_question: str          # e.g. "How can I attune my service to others?"
    moon_day: int               # 1–28
    moon_day_of_week: int       # 1–7
    plasma: str                 # e.g. "Gamma"
    kin_number: int
    tone_number: int
    seal_number: int
    tone: str
    seal: str
    seal_color: str
    guide: str
    analog: OraclePartner
    antipode: OraclePartner
    occult: OraclePartner
    is_galactic_portal: bool
    affirmation: str


class DayOutOfTimeData(TypedDict):
    """Return type for get_today_moon_data() on July 25 (Day Out of Time)."""
    is_day_out_of_time: bool   # Always True here
    kin_number: int             # Kin 228 (fixed for Day Out of Time)
    message: str


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _validate_date(year: int, month: int, day: int) -> None:
    """Raise InvalidDateError if the date is not a valid Gregorian date
    or is outside the range covered by the Year Table."""
    if year < MIN_YEAR or year > MAX_YEAR:
        raise InvalidDateError(
            f"Year {year} is outside the supported range ({MIN_YEAR}–{MAX_YEAR}).",
            year=year, month=month, day=day,
        )
    try:
        date(year, month, day)
    except ValueError as exc:
        raise InvalidDateError(
            f"Invalid date: {year}-{month:02d}-{day:02d}. {exc}",
            year=year, month=month, day=day,
        ) from exc


def _calculate_kin(year: int, month: int, day: int) -> int:
    """
    Compute the Dreamspell Kin number (1–260) for a given Gregorian date.

    Algorithm (official Law of Time method — PDF page 17):
        kin = YEAR_TABLE[year] + MONTH_TABLE[month] + day
        if result > 260: subtract 260
        if result <= 0:  add 260

    The YEAR_TABLE is indexed by calendar year.  The MONTH_TABLE values are
    pre-computed cumulative day offsets that already account for the Tzolkin
    modular arithmetic (some months show values like 13, 44, 74 rather than
    273, 304, 334 because 260 has been subtracted).

    Leap-year note (PDF page 16):
        February 29 before noon → treat as February 28 (pass day=28).
        February 29 after noon  → treat as March 1 (pass month=3, day=1).
    No additional adjustment is needed; the table formula handles this.

    Note: the PDF example labelled "July 26, 2026" is a typo — it computes
    July 26, 2025 (the start of the Yellow Resonant Seed year, Kin 124).
    All dates use YEAR_TABLE[calendar_year] directly.
    """
    raw = YEAR_TABLE[year] + MONTH_TABLE[month] + day
    kin = raw % 260
    if kin == 0:
        kin = 260
    return kin


def _kin_to_tone_and_seal(kin: int) -> tuple[int, int]:
    """Return (tone_number, seal_number) for a given Kin (1–260)."""
    tone_number = ((kin - 1) % 13) + 1   # 1–13
    seal_number = ((kin - 1) % 20) + 1   # 1–20
    return tone_number, seal_number


def _get_guide_seal_number(tone_number: int, seal_number: int) -> int:
    """
    Return the guide seal number using the official Guide Table.

    Algorithm (PDF page 20):
    The 20 seals are arranged in 4 colour families of 5 seals each,
    ordered by steps of 4 within each family (Dragon, Serpent, Dog,
    Eagle, Earth are one family at positions 1, 5, 9, 13, 17, etc.).
    The guide is always in the same colour family as the subject seal.
    Which family member acts as guide depends on (tone_number % 5):

        tone % 5 == 1  → guide = same seal (own power doubled if self-guided tone)
        tone % 5 == 2  → guide = seal + 4  positions (wrapping within 1–20)
        tone % 5 == 3  → guide = seal + 8  positions
        tone % 5 == 4  → guide = seal + 12 positions
        tone % 5 == 0  → guide = seal + 16 positions

    The offsets are multiples of 4 (the colour-family step size), cycling
    through 5 positions.
    """
    GUIDE_OFFSETS = {1: 0, 2: 4, 3: 8, 4: 12, 0: 16}
    offset = GUIDE_OFFSETS[tone_number % 5]
    # Seals are 1-indexed; work in 0-based, then convert back
    guide_seal_number = ((seal_number - 1 + offset) % 20) + 1
    return guide_seal_number


def _make_oracle_partner(kin: int) -> OraclePartner:
    """Build an OraclePartner dict for any Kin number (1–260)."""
    tone, seal = _kin_to_tone_and_seal(kin)
    return OraclePartner(
        kin_number=kin,
        tone_number=tone,
        seal_number=seal,
        tone=TONES[tone - 1],
        seal=SEALS[seal - 1],
        seal_color=SEAL_COLORS[seal - 1],
    )


def _get_oracle_partners(kin: int) -> tuple[OraclePartner, OraclePartner, OraclePartner]:
    """
    Return (analog, antipode, occult) oracle partners for a given Kin (1–260).

    Formulas (all mod 260, 1-indexed):
        analog   = ((kin - 1 + 130) % 260) + 1   # same tone, seal + 10
        antipode = ((kin - 1 + 110) % 260) + 1   # tone + 6, seal + 10
        occult   = 261 - kin                       # tone + seal sums to 14/21

    The analog and antipode share the same seal (the analog seal); the occult
    is entirely independent.  All three tone/seal values are uniquely determined
    because gcd(13, 20) = 1, so CRT guarantees a unique solution mod 260.
    """
    analog_kin   = ((kin - 1 + 130) % 260) + 1
    antipode_kin = ((kin - 1 + 110) % 260) + 1
    occult_kin   = 261 - kin
    return (
        _make_oracle_partner(analog_kin),
        _make_oracle_partner(antipode_kin),
        _make_oracle_partner(occult_kin),
    )


def _build_affirmation(
    tone_number: int,
    seal_number: int,
    guide_seal_number: int,
    is_galactic_portal: bool = False,
) -> str:
    """
    Construct the five-line Dreamspell code spell / daily affirmation.

    Template (PDF page 18):
        I {A} in order to {B}
        {C} {D}
        I seal the {E} of {F}
        With the {G} tone of {H}
        I am guided by the power of {F_guide}
        [I am a galactic activation portal enter me]  ← portal days only

    Self-guided tones (1, 6, 11) replace the guide line with:
        "I am guided by my own power doubled"
    """
    t = tone_number - 1   # 0-based tone index
    s = seal_number - 1   # 0-based seal index
    g = guide_seal_number - 1  # 0-based guide seal index

    line1 = f"I {CREATIVE_POWERS[t]} in order to {SEAL_ACTIONS[s]}"
    line2 = f"{TONE_ACTIONS[t]} {SEAL_POWERS[s]}"
    line3 = f"I seal the {SEAL_FUNCTIONS[s]} of {POWERS_OF_THE_SEAL[s]}"
    line4 = f"With the {TONE_NAMES[t]} tone of {TONE_FUNCTIONS[t]}"

    if tone_number in SELF_GUIDED_TONES:
        line5 = "I am guided by my own power doubled"
    else:
        line5 = f"I am guided by the power of {POWERS_OF_THE_SEAL[g]}"

    lines = [line1, line2, line3, line4, line5]
    if is_galactic_portal:
        lines.append("I am a galactic activation portal enter me")

    return "\n".join(lines)


def _get_galactic_year_start(for_date: date) -> date:
    """
    Return the July 26 start date of the galactic year that contains for_date.
    The galactic year runs July 26 – July 24 (July 25 is Day Out of Time).
    """
    if for_date.month < 7 or (for_date.month == 7 and for_date.day < 26):
        start_year = for_date.year - 1
    else:
        start_year = for_date.year
    return date(start_year, 7, 26)


def _days_since_galactic_new_year(for_date: date) -> int:
    """Return the number of days elapsed since the start of the galactic year (0-indexed)."""
    start = _get_galactic_year_start(for_date)
    return (for_date - start).days


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def get_kin_for_date(year: int, month: int, day: int) -> KinData:
    """
    Return the Dreamspell galactic signature (Kin) for a given Gregorian date.

    Parameters
    ----------
    year : int
        Gregorian year (supported range: 1858–2117).
    month : int
        Gregorian month (1–12).
    day : int
        Gregorian day of month (1–31, validated against the actual month).

    Returns
    -------
    KinData
        A TypedDict containing kin_number, tone, seal, guide, and affirmation.

    Raises
    ------
    InvalidDateError
        If the date is invalid or outside the supported year range.

    Examples
    --------
    >>> get_kin_for_date(1939, 1, 24)
    {'kin_number': 11, 'tone': 'Spectral', 'seal': 'Blue Monkey', ...}
    # Jose Arguelles — Kin 11, Blue Spectral Monkey (verified on PDF page 17)

    >>> get_kin_for_date(1945, 2, 6)
    {'kin_number': 134, 'tone': 'Self-Existing', 'seal': 'White Wizard', ...}
    # Bob Marley — Kin 134, White Self-Existing Wizard (verified on PDF page 17)
    """
    _validate_date(year, month, day)

    kin = _calculate_kin(year, month, day)
    tone_number, seal_number = _kin_to_tone_and_seal(kin)
    guide_seal_number = _get_guide_seal_number(tone_number, seal_number)
    analog, antipode, occult = _get_oracle_partners(kin)
    is_portal = kin in GALACTIC_ACTIVATION_PORTALS

    tone = TONES[tone_number - 1]
    seal = SEALS[seal_number - 1]
    guide = SEALS[guide_seal_number - 1]
    affirmation = _build_affirmation(tone_number, seal_number, guide_seal_number, is_portal)

    return KinData(
        kin_number=kin,
        tone_number=tone_number,
        seal_number=seal_number,
        tone=tone,
        seal=seal,
        seal_color=SEAL_COLORS[seal_number - 1],
        guide=guide,
        analog=analog,
        antipode=antipode,
        occult=occult,
        is_galactic_portal=is_portal,
        affirmation=affirmation,
    )


def get_today_moon_data() -> Union[MoonData, DayOutOfTimeData]:
    """
    Return today's full 13-Moon calendar position and daily affirmation.

    On July 25 (Day Out of Time), returns a DayOutOfTimeData dict.
    On all other days, returns a MoonData dict.

    Returns
    -------
    MoonData | DayOutOfTimeData

    Raises
    ------
    InvalidDateError
        If today's year is outside the supported range (extremely unlikely).
    """
    today = date.today()

    # -----------------------------------------------------------------------
    # Day Out of Time — July 25
    # Always Kin 228 (the day before the new galactic year begins).
    # Source: PDF page 14.
    # -----------------------------------------------------------------------
    if today.month == 7 and today.day == 25:
        return DayOutOfTimeData(
            is_day_out_of_time=True,
            kin_number=228,
            message=(
                "Day Out of Time — July 25\n\n"
                "This is a sacred pause between cycles.\n"
                "Use it for creativity, release, and renewal.\n\n"
                "Suggestions:\n"
                "• Create something from spirit (art, music, dance)\n"
                "• Reflect on the cycle just completed\n"
                "• Let go of old patterns\n"
                "• Celebrate being a living spiral\n\n"
                "Affirmation:\n"
                "\"I exist beyond time. I am a living spiral.\""
            ),
        )

    # -----------------------------------------------------------------------
    # Normal day
    # -----------------------------------------------------------------------
    _validate_date(today.year, today.month, today.day)

    kin = _calculate_kin(today.year, today.month, today.day)
    tone_number, seal_number = _kin_to_tone_and_seal(kin)
    guide_seal_number = _get_guide_seal_number(tone_number, seal_number)
    analog, antipode, occult = _get_oracle_partners(kin)
    is_portal = kin in GALACTIC_ACTIVATION_PORTALS

    tone = TONES[tone_number - 1]
    seal = SEALS[seal_number - 1]
    guide = SEALS[guide_seal_number - 1]
    affirmation = _build_affirmation(tone_number, seal_number, guide_seal_number, is_portal)

    # 13-Moon calendar position
    days_elapsed = _days_since_galactic_new_year(today)
    moon_index = (days_elapsed // 28) % 13
    moon_number = moon_index + 1
    moon_name = MOONS[moon_index]
    moon_day = (days_elapsed % 28) + 1
    moon_day_of_week = ((moon_day - 1) % 7) + 1
    plasma = PLASMAS[moon_day_of_week - 1]

    return MoonData(
        is_day_out_of_time=False,
        moon_number=moon_number,
        moon_name=moon_name,
        moon=f"{moon_number} {moon_name} Moon",
        moon_question=MOON_QUESTIONS[moon_number],
        moon_day=moon_day,
        moon_day_of_week=moon_day_of_week,
        plasma=plasma,
        kin_number=kin,
        tone_number=tone_number,
        seal_number=seal_number,
        tone=tone,
        seal=seal,
        seal_color=SEAL_COLORS[seal_number - 1],
        guide=guide,
        analog=analog,
        antipode=antipode,
        occult=occult,
        is_galactic_portal=is_portal,
        affirmation=affirmation,
    )


# ---------------------------------------------------------------------------
# Quick smoke-test against the PDF's verified examples
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Verified examples from PDF page 17 ===\n")

    tests = [
        ((1939, 1, 24), 11,  "Blue Spectral Monkey",      "Jose Arguelles"),
        ((1973, 1, 8),  185, "Red Electric Serpent",       "Stephanie South"),
        ((1948, 3, 21), 232, "Yellow Spectral Human",      "Regina of Mexico"),
        ((1945, 2, 6),  134, "White Self-Existing Wizard", "Bob Marley"),
        ((2025, 7, 26), 124, "Yellow Resonant Seed",       "July 26, 2025 (year-bearer)"),
        ((2025, 8,  1), 130, "Cosmic Dog",                  "Aug 1, 2025 — Kin 130, White Cosmic Dog"),
    ]

    all_pass = True
    for (y, m, d), expected_kin, expected_name, label in tests:
        result = get_kin_for_date(y, m, d)
        kin = result["kin_number"]
        name = f"{result['tone']} {result['seal'].split()[-1]}"
        status = "✓" if kin == expected_kin else "✗"
        if kin != expected_kin:
            all_pass = False
        print(f"{status} {label}: Kin {kin} ({result['tone']} {result['seal']}) — expected Kin {expected_kin} ({expected_name})")

    print()
    print("=== Today's moon data ===\n")
    moon = get_today_moon_data()
    for k, v in moon.items():
        print(f"  {k}: {v}")

    print()
    print("All tests passed!" if all_pass else "SOME TESTS FAILED — check constants/logic.")
