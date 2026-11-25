#!/usr/bin/env python3
"""SocialClub File Server - serves socialclub.dll & socialclub.pak on port 8080"""
import os, http.server, socketserver

PORT = 8080
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'socialclub')

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format%args}")

if __name__ == '__main__':
    os.makedirs(DIR, exist_ok=True)
    print(f"Serving SocialClub files at http://localhost:{PORT}/")
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        httpd.serve_forever()
