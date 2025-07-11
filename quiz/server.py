#!/usr/bin/env python3
"""
Simple HTTP server to serve the quiz application locally.
Run this script and open http://localhost:8000 in your browser.
"""

import http.server
import socketserver
import os
import sys

def main():
    # Change to the parent directory so we can serve both quiz files and data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    os.chdir(parent_dir)
    
    HOSTNAME = "localhost"
    PORT = 8002
    
    class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            # Add CORS headers to allow local file access
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            super().end_headers()
    
    with socketserver.TCPServer((HOSTNAME, PORT), MyHTTPRequestHandler) as httpd:
        print(f"🌐 Server starting at http://{HOSTNAME}:{PORT}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"📊 Open http://{HOSTNAME}:{PORT}/quiz/ in your browser to start the quiz!")
        print("🛑 Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user")
            sys.exit(0)

if __name__ == "__main__":
    main()
