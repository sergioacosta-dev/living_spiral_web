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

TXT_DIR = os.path.join(_ROOT_DIR, "txt_files")

MEDITATIONS = {
    "galactic_prayer":          "Galactic Prayer",
    "natural_mind_meditation":  "Natural Mind Meditation",
    "rainbow_bridge_meditation":"Rainbow Bridge Meditation",
    "5_synchronic_keys":        "5 Synchronic Keys",
    "DOT":                      "Day Out of Time",
}


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        name = params.get("name", [None])[0]

        if name is None:
            # Return the list of available meditations
            json_response(self, [
                {"key": k, "title": v} for k, v in MEDITATIONS.items()
            ])
            return

        if name not in MEDITATIONS:
            error_response(self, f"Unknown meditation: {name}", 404)
            return

        path = os.path.join(TXT_DIR, f"{name}.txt")
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            error_response(self, f"File not found: {name}.txt", 404)
            return

        json_response(self, {"key": name, "title": MEDITATIONS[name], "text": text})

    def log_message(self, *_):
        pass
