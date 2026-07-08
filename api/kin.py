import os
import sys

_API_DIR  = os.path.dirname(os.path.abspath(__file__))
_ROOT_DIR = os.path.dirname(_API_DIR)
for _p in (_API_DIR, _ROOT_DIR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from api_utils import json_response, error_response

from living_spiral import get_kin_for_date, InvalidDateError


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        try:
            year  = int(params["year"][0])
            month = int(params["month"][0])
            day   = int(params["day"][0])
        except (KeyError, ValueError, IndexError):
            error_response(self, "year, month, and day are required integers")
            return

        try:
            kin = get_kin_for_date(year, month, day)
        except InvalidDateError as e:
            error_response(self, str(e))
            return
        except Exception as e:
            error_response(self, f"Unexpected error: {e}", 500)
            return

        json_response(self, dict(kin))

    def log_message(self, *_):
        pass
