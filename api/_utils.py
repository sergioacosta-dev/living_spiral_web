"""Shared utilities for Vercel Python serverless handlers."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def json_response(handler, data, status=200):
    body = json.dumps(data).encode()
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.end_headers()
    handler.wfile.write(body)


def error_response(handler, message, status=400):
    json_response(handler, {"error": message}, status)
