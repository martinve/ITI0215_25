#!/usr/bin/env python3

from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import threading
import urllib.parse as urlparse
import sys
import json

"""
Routes

/addr
/getblocks

"""

addrlist = [
        "127.0.0.1:5000", 
        "127.0.0.1:5002",
        "127.0.0.1:5003"
    ]


def get_known_addresses():
    return addrlist
    ## return "Getting a list of known addresses\n"


def add_known_address(port):
    new_addr = f"127.0.0.1:{port}"
    if new_addr in addrlist:
        print(f"Port:{port} is already in the list")
    else:
        addrlist.append(new_addr)
    return addrlist



class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        parsed = urlparse.urlparse(self.path)      
        urlvars = urlparse.parse_qs(parsed.query)

        is_ok = True

        if parsed.path == "/addr":
            result = get_known_addresses()
            port = urlvars.get("port", [])[0]
            add_known_address(port)
            result = json.dumps(result)
        elif parsed.path == "/getblocks":
            result = "Getting a list of blocks\n"    
        elif parsed.path == "/ping":
            result = "pong\n"
        elif parsed.path == "/name":
            name = urlvars.get("name", [])
            id = urlvars.get("id", [])
            result = f"Hello {name}, your ID is {id}\n"     
        else:
            is_ok = False
            self.send_response(404)
            self.end_headers()
            return


        if is_ok:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(result.encode("utf-8"))

    def do_POST(self):
        content_length_str = self.headers.get('Content-Length')
        if content_length_str is None:
            self.send_response(400)  # Bad request
            self.end_headers()
            self.wfile.write(b'Content-Length header is missing')
            return

        content_length = int(content_length_str)
        rawdata = self.rfile.read(content_length)
        data = rawdata.decode("utf-8")

        parsed = urlparse.parse_qs(data)
        name = parsed.get("name")[0]
        id = parsed.get("id")[0]

        # If we are 100% sure there are no duplicate values we can use `rlparse.parse_qsl` instead
        parsed2 = dict(urlparse.parse_qsl(data))
        print(parsed2)
        name = parsed2.get("name")
        id = parsed2.get("id")
        
        out = f"Hello `{name}`, your ID is `{id}`.\n"       

        self.send_response(200)  # Bad request
        self.end_headers()
        self.wfile.write(out.encode("utf-8"))


def start(port):
    if port < 2000 or port > 65535:
        print("Port number must be between 1024 and 65535")
        sys.exit(1)

    server = ThreadingHTTPServer(("", port), MyHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
 

    print(f"Server started on {port}")
  





if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("\nUsage: ./server.py <port>\n")
        sys.exit(1)

    port = int(sys.argv[1])
    start(port)
