import os
import sys

_API_DIR  = os.path.dirname(os.path.abspath(__file__))
_ROOT_DIR = os.path.dirname(_API_DIR)
for _p in (_API_DIR, _ROOT_DIR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from http.server import BaseHTTPRequestHandler
from _utils import json_response

from living_spiral import get_today_moon_data, MOON_QUESTIONS


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = get_today_moon_data()
        json_response(self, dict(data))

    def log_message(self, *_):
        pass
