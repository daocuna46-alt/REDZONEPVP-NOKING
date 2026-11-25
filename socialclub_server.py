#!/usr/bin/env python3
"""SocialClub File Server - serves socialclub.dll & socialclub.pak on port 8080"""
import os, http.server, socketserver, threading, time

PORT = 8080
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'socialclub')

def log(msg): print(f"[{time.strftime('%H:%M:%S')}] {msg}")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE, **kwargs)
    def log_message(self, fmt, *args):
        log(f"{self.address_string()} - {fmt%args}")

def serve():
    log(f"Starting SocialClub Server on port {PORT}, dir: {BASE}")
    with socketserver.ThreadingTCPServer(("0.0.0.0", PORT), Handler) as httpd:
        httpd.serve_forever()

if __name__ == '__main__':
    os.makedirs(BASE, exist_ok=True)
    serve()
