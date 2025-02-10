#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparse
import sys

"""
Routes

/addr
/getblocks

"""

def get_known_addresses():
    return ["8000", "8001", "8003"]
    ## return "Getting a list of known addresses\n"



class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        parsed = urlparse.urlparse(self.path)      
        urlvars = urlparse.parse_qs(parsed.query)

        if parsed.path == "/addr":
            result = get_known_addresses()
            result = ",".join(result)
        elif parsed.path == "/getblocks":
            result = "Getting a list of blocks\n"    
        else:
            name = urlvars.get("name", [])
            id = urlvars.get("id", [])
            result = f"Tere {name}, sinu ID on {id}\n"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(result.encode("utf-8"))

    def do_POST(self):
        pass

if __name__ == "__main__":

    port = int(sys.argv[1])

    server = HTTPServer(("", port), MyHandler)
    print(f"Server started on {port}")
    server.serve_forever()