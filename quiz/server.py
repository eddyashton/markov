#!/usr/bin/env python3
"""
Simple HTTP server to serve the quiz application locally.
Run this script and open http://localhost:8000 in your browser.
"""

import http.server
import socketserver
import os
import sys
import json
import urllib.parse

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
        
        def do_GET(self):
            # Handle API endpoint for listing data files
            if self.path == '/api/data-files':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                try:
                    data_dir = os.path.join(os.getcwd(), 'data')
                    if os.path.exists(data_dir):
                        files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]
                        response = {'files': files}
                    else:
                        response = {'files': [], 'error': 'Data directory not found'}
                except Exception as e:
                    response = {'files': [], 'error': str(e)}
                
                self.wfile.write(json.dumps(response).encode())
                return
            
            # Default behavior for all other requests
            super().do_GET()
    
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
