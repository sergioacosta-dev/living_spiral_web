import os
import sys
import json

_API_DIR  = os.path.dirname(os.path.abspath(__file__))
_ROOT_DIR = os.path.dirname(_API_DIR)
for _p in (_API_DIR, _ROOT_DIR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from http.server import BaseHTTPRequestHandler
from api_utils import json_response

from living_spiral import get_today_moon_data, MOON_QUESTIONS

DATA_DIR = os.path.join(_ROOT_DIR, "data")
CURRICULUM_PATH = os.path.join(DATA_DIR, "living_spiral_curriculum.json")

_curriculum_cache = None


def _load_curriculum():
    global _curriculum_cache
    if _curriculum_cache is None:
        try:
            with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
                _curriculum_cache = json.load(f)
        except Exception:
            _curriculum_cache = {}
    return _curriculum_cache


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = get_today_moon_data()
        moon_number = data["moon_number"]
        moon_day    = data["moon_day"]

        curriculum = _load_curriculum()
        global_day = str((moon_number - 1) * 28 + moon_day)
        entry = curriculum.get(global_day, {})

        json_response(self, {
            "moon_number":   moon_number,
            "moon":          data["moon"],
            "moon_day":      moon_day,
            "moon_question": MOON_QUESTIONS.get(moon_number, ""),
            "affirmation":   data.get("affirmation", ""),
            "curriculum":    entry,
        })

    def log_message(self, *_):
        pass
