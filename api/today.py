from http.server import BaseHTTPRequestHandler
from ._utils import json_response, ROOT
import sys, os
sys.path.insert(0, ROOT)

from living_spiral import get_today_moon_data, MOON_QUESTIONS


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = get_today_moon_data()
        json_response(self, dict(data))

    def log_message(self, *_):
        pass
