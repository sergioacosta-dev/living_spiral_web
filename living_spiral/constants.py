"""
constants.py
All Dreamspell / 13-Moon calendar constants.

Sources: Foundation for the Law of Time — 13 Moon Peace Synchronometer
(Yellow Resonant Seed Year, July 26 2025 – July 25 2026).
See: https://www.lawoftime.org
"""

# ---------------------------------------------------------------------------
# 13 Moons (months) of the galactic year
# Each moon is 28 days. 13 × 28 = 364 days + 1 Day Out of Time (July 25).
# The new galactic year begins July 26.
# ---------------------------------------------------------------------------
MOONS = [
    "Magnetic",       # Moon  1 — Question: What is my purpose?
    "Lunar",          # Moon  2 — Question: What is my challenge?
    "Electric",       # Moon  3 — Question: How can I best serve?
    "Self-Existing",  # Moon  4 — Question: What is the form my service will take?
    "Overtone",       # Moon  5 — Question: How can I best empower myself?
    "Rhythmic",       # Moon  6 — Question: How can I extend my equality to others?
    "Resonant",       # Moon  7 — Question: How can I attune my service to others?
    "Galactic",       # Moon  8 — Question: Do I live what I believe?
    "Solar",          # Moon  9 — Question: How do I attain my purpose?
    "Planetary",      # Moon 10 — Question: How do I perfect what I do?
    "Spectral",       # Moon 11 — Question: How do I release and let go?
    "Crystal",        # Moon 12 — Question: How can I dedicate myself to all that lives?
    "Cosmic",         # Moon 13 — Question: How can I expand my joy and love?
]

# ---------------------------------------------------------------------------
# 7 Radial Plasmas — the days of the 28-day moon/week
# Each week of 7 days cycles through these plasma names.
# ---------------------------------------------------------------------------
PLASMAS = ["Dali", "Seli", "Gamma", "Kali", "Alpha", "Limi", "Silio"]

# ---------------------------------------------------------------------------
# 20 Solar Seals — the archetypal energies of the Tzolkin
# Numbered 1–20; index 0 = Seal 1 (Dragon), index 19 = Seal 20 (Sun).
# Source: PDF page 15 & 19.
# ---------------------------------------------------------------------------
SEALS = [
    "Red Dragon",         # 1  — Birth
    "White Wind",         # 2  — Spirit
    "Blue Night",         # 3  — Abundance
    "Yellow Seed",        # 4  — Flowering
    "Red Serpent",        # 5  — Life Force
    "White Worldbridger", # 6  — Death
    "Blue Hand",          # 7  — Accomplishment
    "Yellow Star",        # 8  — Elegance
    "Red Moon",           # 9  — Universal Water
    "White Dog",          # 10 — Heart
    "Blue Monkey",        # 11 — Magic
    "Yellow Human",       # 12 — Free Will
    "Red Skywalker",      # 13 — Space
    "White Wizard",       # 14 — Timelessness
    "Blue Eagle",         # 15 — Vision
    "Yellow Warrior",     # 16 — Intelligence
    "Red Earth",          # 17 — Navigation
    "White Mirror",       # 18 — Endlessness
    "Blue Storm",         # 19 — Self-Generation
    "Yellow Sun",         # 20 — Universal Fire
]

# ---------------------------------------------------------------------------
# 13 Galactic Tones
# Numbered 1–13; index 0 = Tone 1 (Magnetic).
# Source: PDF page 15 & 18.
# ---------------------------------------------------------------------------
TONES = [
    "Magnetic",     # 1
    "Lunar",        # 2
    "Electric",     # 3
    "Self-Existing",# 4
    "Overtone",     # 5
    "Rhythmic",     # 6
    "Resonant",     # 7
    "Galactic",     # 8
    "Solar",        # 9
    "Planetary",    # 10
    "Spectral",     # 11
    "Crystal",      # 12
    "Cosmic",       # 13
]

# ---------------------------------------------------------------------------
# Affirmation formula components — sourced from PDF pages 18–19.
#
# The affirmation template is:
#   "I {CREATIVE_POWER} in order to {SEAL_ACTION}
#    {TONE_ACTION} {SEAL_POWER}
#    I seal the {SEAL_FUNCTION} of {SEAL_POWER_OF}
#    With the {TONE_NAME} tone of {TONE_FUNCTION}
#    I am guided by the power of {GUIDE_SEAL_POWER_OF}"
#
# Tones 1 (Magnetic), 6 (Rhythmic), 11 (Spectral) replace the last line with:
#   "I am guided by my own power doubled"
# ---------------------------------------------------------------------------

# Column A — Creative Power (indexed by tone 1–13, i.e. index = tone_number - 1)
CREATIVE_POWERS = [
    "Unify",        # Tone 1  Magnetic
    "Polarize",     # Tone 2  Lunar
    "Activate",     # Tone 3  Electric
    "Define",       # Tone 4  Self-Existing
    "Empower",      # Tone 5  Overtone
    "Organize",     # Tone 6  Rhythmic
    "Channel",      # Tone 7  Resonant
    "Harmonize",    # Tone 8  Galactic
    "Pulse",        # Tone 9  Solar
    "Perfect",      # Tone 10 Planetary
    "Dissolve",     # Tone 11 Spectral
    "Dedicate",     # Tone 12 Crystal
    "Endure",       # Tone 13 Cosmic
]

# Column B — Seal Action (indexed by seal 1–20, i.e. index = seal_number - 1)
SEAL_ACTIONS = [
    "Nurture",      # 1  Dragon
    "Communicate",  # 2  Wind
    "Dream",        # 3  Night
    "Target",       # 4  Seed
    "Survive",      # 5  Serpent
    "Equalize",     # 6  Worldbridger
    "Know",         # 7  Hand
    "Beautify",     # 8  Star
    "Purify",       # 9  Moon
    "Love",         # 10 Dog
    "Play",         # 11 Monkey
    "Influence",    # 12 Human
    "Explore",      # 13 Skywalker
    "Enchant",      # 14 Wizard
    "Create",       # 15 Eagle
    "Question",     # 16 Warrior
    "Evolve",       # 17 Earth
    "Reflect",      # 18 Mirror
    "Catalyze",     # 19 Storm
    "Enlighten",    # 20 Sun
]

# Column C — Tone Action (indexed by tone 1–13)
TONE_ACTIONS = [
    "Attracting",       # Tone 1
    "Stabilizing",      # Tone 2
    "Bonding",          # Tone 3
    "Measuring",        # Tone 4
    "Commanding",       # Tone 5
    "Balancing",        # Tone 6
    "Inspiring",        # Tone 7
    "Modeling",         # Tone 8
    "Realizing",        # Tone 9
    "Producing",        # Tone 10
    "Releasing",        # Tone 11
    "Universalizing",   # Tone 12
    "Transcending",     # Tone 13
]

# Column D — Seal Power / Essence (indexed by seal 1–20)
SEAL_POWERS = [
    "Being",            # 1  Dragon
    "Breath",           # 2  Wind
    "Intuition",        # 3  Night
    "Awareness",        # 4  Seed
    "Instinct",         # 5  Serpent
    "Opportunity",      # 6  Worldbridger
    "Healing",          # 7  Hand
    "Art",              # 8  Star
    "Flow",             # 9  Moon
    "Loyalty",          # 10 Dog
    "Illusion",         # 11 Monkey
    "Wisdom",           # 12 Human
    "Wakefulness",      # 13 Skywalker
    "Receptivity",      # 14 Wizard
    "Mind",             # 15 Eagle
    "Fearlessness",     # 16 Warrior
    "Synchronicity",    # 17 Earth
    "Order",            # 18 Mirror
    "Energy",           # 19 Storm
    "Life",             # 20 Sun
]

# Column E — Seal Function / Chakra group (indexed by seal 1–20)
# Seals 1–4 = Input, 5–8 = Store, 9–12 = Process, 13–16 = Output, 17–20 = Matrix
# Source: PDF page 19.
SEAL_FUNCTIONS = [
    "Input",    # 1  Dragon
    "Input",    # 2  Wind
    "Input",    # 3  Night
    "Input",    # 4  Seed
    "Store",    # 5  Serpent
    "Store",    # 6  Worldbridger
    "Store",    # 7  Hand
    "Store",    # 8  Star
    "Process",  # 9  Moon
    "Process",  # 10 Dog
    "Process",  # 11 Monkey
    "Process",  # 12 Human
    "Output",   # 13 Skywalker
    "Output",   # 14 Wizard
    "Output",   # 15 Eagle
    "Output",   # 16 Warrior
    "Matrix",   # 17 Earth
    "Matrix",   # 18 Mirror
    "Matrix",   # 19 Storm
    "Matrix",   # 20 Sun
]

# Column F — Power of the Seal (indexed by seal 1–20)
POWERS_OF_THE_SEAL = [
    "Birth",            # 1  Dragon
    "Spirit",           # 2  Wind
    "Abundance",        # 3  Night
    "Flowering",        # 4  Seed
    "Life Force",       # 5  Serpent
    "Death",            # 6  Worldbridger
    "Accomplishment",   # 7  Hand
    "Elegance",         # 8  Star
    "Universal Water",  # 9  Moon
    "Heart",            # 10 Dog
    "Magic",            # 11 Monkey
    "Free Will",        # 12 Human
    "Space",            # 13 Skywalker
    "Timelessness",     # 14 Wizard
    "Vision",           # 15 Eagle
    "Intelligence",     # 16 Warrior
    "Navigation",       # 17 Earth
    "Endlessness",      # 18 Mirror
    "Self-Generation",  # 19 Storm
    "Universal Fire",   # 20 Sun
]

# Column G — Tone Name (same as TONES; kept separately for affirmation clarity)
TONE_NAMES = TONES

# Column H — Tone Function (indexed by tone 1–13)
TONE_FUNCTIONS = [
    "Purpose",          # Tone 1  Magnetic
    "Challenge",        # Tone 2  Lunar
    "Service",          # Tone 3  Electric
    "Form",             # Tone 4  Self-Existing
    "Radiance",         # Tone 5  Overtone
    "Equality",         # Tone 6  Rhythmic
    "Attunement",       # Tone 7  Resonant
    "Integrity",        # Tone 8  Galactic
    "Intention",        # Tone 9  Solar
    "Manifestation",    # Tone 10 Planetary
    "Liberation",       # Tone 11 Spectral
    "Cooperation",      # Tone 12 Crystal
    "Presence",         # Tone 13 Cosmic
]

# ---------------------------------------------------------------------------
# Tones that trigger "guided by my own power doubled"
# Source: PDF page 18 — Tones 1, 6, 11 (Magnetic, Rhythmic, Spectral)
# ---------------------------------------------------------------------------
SELF_GUIDED_TONES = {1, 6, 11}  # 1-based tone numbers

# ---------------------------------------------------------------------------
# 13-Moon guiding questions — one per moon (1-indexed)
# Source: Foundation for the Law of Time — 13 Moon Peace Synchronometer
# ---------------------------------------------------------------------------
MOON_QUESTIONS = {
    1:  "What is my purpose?",
    2:  "What is my challenge?",
    3:  "How can I best serve?",
    4:  "What is the form my service will take?",
    5:  "How can I best empower myself?",
    6:  "How can I extend my equality to others?",
    7:  "How can I attune my service to others?",
    8:  "Do I live what I believe?",
    9:  "How do I attain my purpose?",
    10: "How do I perfect what I do?",
    11: "How do I release and let go?",
    12: "How can I dedicate myself to all that lives?",
    13: "How can I expand my joy and love?",
}

# ---------------------------------------------------------------------------
# Kin lookup tables — the official method from the Law of Time PDF (page 17).
#
# To find a Kin:  kin = YEAR_TABLE[year] + MONTH_TABLE[month] + day
# If result > 260, subtract 260.
#
# These tables encode the cumulative Dreamspell day count anchored to the
# start of the Dreamspell count on July 26, 1987 (Kin 1).
# ---------------------------------------------------------------------------

# Year Table: maps Gregorian year to its base Kin offset.
# Values repeat on a 52-year cycle (260 kin / 5 seals per colour family).
# Source: PDF page 17.
YEAR_TABLE = {
    1858: 62,  1859: 167, 1860: 12,  1861: 117, 1862: 222, 1863: 67,  1864: 172,
    1865: 17,  1866: 122, 1867: 227, 1868: 72,  1869: 177, 1870: 22,  1871: 127,
    1872: 232, 1873: 77,  1874: 182, 1875: 27,  1876: 132, 1877: 237, 1878: 82,
    1879: 187, 1880: 32,  1881: 137, 1882: 242, 1883: 87,  1884: 192, 1885: 37,
    1886: 142, 1887: 247, 1888: 92,  1889: 197, 1890: 42,  1891: 147, 1892: 252,
    1893: 97,  1894: 202, 1895: 47,  1896: 152, 1897: 257, 1898: 102, 1899: 207,
    1900: 52,  1901: 157, 1902: 2,   1903: 107, 1904: 212, 1905: 57,  1906: 162,
    1907: 7,   1908: 112, 1909: 217, 1910: 62,  1911: 167, 1912: 12,  1913: 117,
    1914: 222, 1915: 67,  1916: 172, 1917: 17,  1918: 122, 1919: 227, 1920: 72,
    1921: 177, 1922: 22,  1923: 127, 1924: 232, 1925: 77,  1926: 182, 1927: 27,
    1928: 132, 1929: 237, 1930: 82,  1931: 187, 1932: 32,  1933: 137, 1934: 242,
    1935: 87,  1936: 192, 1937: 37,  1938: 142, 1939: 247, 1940: 92,  1941: 197,
    1942: 42,  1943: 147, 1944: 252, 1945: 97,  1946: 202, 1947: 47,  1948: 152,
    1949: 257, 1950: 102, 1951: 207, 1952: 52,  1953: 157, 1954: 2,   1955: 107,
    1956: 212, 1957: 57,  1958: 162, 1959: 7,   1960: 112, 1961: 217, 1962: 62,
    1963: 167, 1964: 12,  1965: 117, 1966: 222, 1967: 67,  1968: 172, 1969: 17,
    1970: 122, 1971: 227, 1972: 72,  1973: 177, 1974: 22,  1975: 127, 1976: 232,
    1977: 77,  1978: 182, 1979: 27,  1980: 132, 1981: 237, 1982: 82,  1983: 187,
    1984: 32,  1985: 137, 1986: 242, 1987: 87,  1988: 192, 1989: 37,  1990: 142,
    1991: 247, 1992: 92,  1993: 197, 1994: 42,  1995: 147, 1996: 252, 1997: 97,
    1998: 202, 1999: 47,  2000: 152, 2001: 257, 2002: 102, 2003: 207, 2004: 52,
    2005: 157, 2006: 2,   2007: 107, 2008: 212, 2009: 57,  2010: 162, 2011: 7,
    2012: 112, 2013: 217, 2014: 62,  2015: 167, 2016: 12,  2017: 117, 2018: 222,
    2019: 67,  2020: 172, 2021: 17,  2022: 122, 2023: 227, 2024: 72,  2025: 177,
    2026: 22,  2027: 127, 2028: 232, 2029: 77,  2030: 182, 2031: 27,  2032: 132,
    2033: 237, 2034: 82,  2035: 187, 2036: 32,  2037: 137, 2038: 242, 2039: 87,
    2040: 192, 2041: 37,  2042: 142, 2043: 247, 2044: 92,  2045: 197, 2046: 42,
    2047: 147, 2048: 252, 2049: 97,  2050: 202, 2051: 47,  2052: 152, 2053: 257,
    2054: 102, 2055: 207, 2056: 52,  2057: 157, 2058: 2,   2059: 107, 2060: 212,
    2061: 57,  2062: 162, 2063: 7,   2064: 112, 2065: 217, 2066: 62,  2067: 167,
    2068: 12,  2069: 117, 2070: 222, 2071: 67,  2072: 172, 2073: 17,  2074: 122,
    2075: 227, 2076: 72,  2077: 177, 2078: 22,  2079: 127, 2080: 232, 2081: 77,
    2082: 182, 2083: 27,  2084: 132, 2085: 237, 2086: 82,  2087: 187, 2088: 32,
    2089: 137, 2090: 242, 2091: 87,  2092: 192, 2093: 37,  2094: 142, 2095: 247,
    2096: 92,  2097: 197, 2098: 42,  2099: 147, 2100: 252, 2101: 97,  2102: 202,
    2103: 47,  2104: 152, 2105: 257, 2106: 102, 2107: 207, 2108: 52,  2109: 157,
    2110: 2,   2111: 107, 2112: 212, 2113: 57,  2114: 162, 2115: 7,   2116: 112,
    2117: 217,
}

# Month Table: maps Gregorian month number to its cumulative day offset.
# Source: PDF page 17.
MONTH_TABLE = {
    1:  0,    # January
    2:  31,   # February
    3:  59,   # March   (use 60 in leap years — handled in code)
    4:  90,   # April   (use 91 in leap years)
    5:  120,  # May     (use 121 in leap years)
    6:  151,  # June    (use 152 in leap years)
    7:  181,  # July    (use 182 in leap years)
    8:  212,  # August  (use 213 in leap years)
    9:  243,  # September (use 244 in leap years)
    10: 13,   # October  (mod-260 applied: 273 → 13)
    11: 44,   # November (mod-260 applied: 304 → 44)
    12: 74,   # December (mod-260 applied: 334 → 74)
}

# Earliest year supported by the YEAR_TABLE lookup
MIN_YEAR = min(YEAR_TABLE)
MAX_YEAR = max(YEAR_TABLE)

# ---------------------------------------------------------------------------
# Seal color families — each of the 4 colours has 5 seals (steps of 4).
# Red: 1,5,9,13,17 | White: 2,6,10,14,18 | Blue: 3,7,11,15,19 | Yellow: 4,8,12,16,20
# Source: PDF page 19 groupings.
# ---------------------------------------------------------------------------
SEAL_COLORS = [
    "Red",    # 1  Dragon
    "White",  # 2  Wind
    "Blue",   # 3  Night
    "Yellow", # 4  Seed
    "Red",    # 5  Serpent
    "White",  # 6  Worldbridger
    "Blue",   # 7  Hand
    "Yellow", # 8  Star
    "Red",    # 9  Moon
    "White",  # 10 Dog
    "Blue",   # 11 Monkey
    "Yellow", # 12 Human
    "Red",    # 13 Skywalker
    "White",  # 14 Wizard
    "Blue",   # 15 Eagle
    "Yellow", # 16 Warrior
    "Red",    # 17 Earth
    "White",  # 18 Mirror
    "Blue",   # 19 Storm
    "Yellow", # 20 Sun
]

# ---------------------------------------------------------------------------
# 52 Galactic Activation Portals — fixed Kin numbers in the Tzolkin.
# These form a symmetric hourglass/lemniscate in the 13×20 grid.
# Portal days add "I am a galactic activation portal enter me" to the
# daily code affirmation (PDF page 18).
# Source: Foundation for the Law of Time standard tables.
# ---------------------------------------------------------------------------
GALACTIC_ACTIVATION_PORTALS: frozenset[int] = frozenset({
    1,  11,  12,  22,  23,  33,  34,  44,  45,  52,
    55,  65,  66,  76,  77,  87,  88,  98,  99, 105,
   106, 116, 117, 127, 128, 138, 139, 149, 150, 156,
   157, 167, 168, 178, 179, 189, 190, 196, 197, 207,
   208, 218, 219, 225, 226, 236, 237, 247, 248, 250,
   251, 260,
})
