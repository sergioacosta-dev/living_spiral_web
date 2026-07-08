"""
Local dev server — serves /public as static files and /api/* via handlers.
Run: python dev_server.py
"""
import sys
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from pathlib import Path

ROOT = Path(__file__).parent
PUBLIC = ROOT
sys.path.insert(0, str(ROOT))


def _import_handler(name):
    import importlib.util, types

    # Provide a fake package so relative imports in api/api_utils.py work
    pkg_name = "api"
    if pkg_name not in sys.modules:
        pkg = types.ModuleType(pkg_name)
        pkg.__path__ = [str(ROOT / "api")]
        pkg.__package__ = pkg_name
        sys.modules[pkg_name] = pkg

    spec = importlib.util.spec_from_file_location(
        f"api.{name}", ROOT / "api" / f"{name}.py",
        submodule_search_locations=[]
    )
    mod = importlib.util.module_from_spec(spec)
    mod.__package__ = pkg_name
    sys.modules[f"api.{name}"] = mod
    spec.loader.exec_module(mod)
    return mod.handler


# Pre-load all handlers
_handlers = {
    "/api/today":       _import_handler("today"),
    "/api/kin":         _import_handler("kin"),
    "/api/practices":   _import_handler("practices"),
    "/api/meditations": _import_handler("meditations"),
}

MIME = {
    ".html": "text/html; charset=utf-8",
    ".css":  "text/css; charset=utf-8",
    ".js":   "application/javascript; charset=utf-8",
    ".ico":  "image/x-icon",
    ".png":  "image/png",
}


class DevHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path).path

        # API routes — call do_GET as an unbound method with self so the
        # DevHandler's already-parsed request/socket is reused correctly.
        api_handler_cls = _handlers.get(path)
        if api_handler_cls:
            api_handler_cls.do_GET(self)
            return

        # Static files
        if path == "/" or path == "":
            path = "/index.html"
        file_path = PUBLIC / path.lstrip("/")

        if not file_path.exists() or not file_path.is_file():
            self.send_error(404, f"Not found: {path}")
            return

        data = file_path.read_bytes()
        mime = MIME.get(file_path.suffix, "application/octet-stream")
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        print(f"  {self.address_string()} {fmt % args}")


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = HTTPServer(("127.0.0.1", port), DevHandler)
    print(f"Living Spiral dev server → http://127.0.0.1:{port}")
    server.serve_forever()
