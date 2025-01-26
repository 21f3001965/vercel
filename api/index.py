# api/index.py
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import pandas as pd


class handler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'x-api-key, Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'x-api-key, Content-Type')
        self.end_headers()
        
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        names = query_components.get('name')
        with open('tds.json', 'r') as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        marks = [df[df["name"] == name].values[0][1] for name in names]
        result = {
            "marks": marks
        }
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))
        return