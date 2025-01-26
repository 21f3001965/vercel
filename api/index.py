# api/index.py
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import pandas as pd

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        name1 = query_components.get('name')[0]
        name2 = query_components.get('name')[1]
        with open('tds.json', 'r') as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        
        result = {
            "message": [df[df["name"] == name1].values[0][1], df[df["name"] == name2].values[0][1]]
        }
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))
        return