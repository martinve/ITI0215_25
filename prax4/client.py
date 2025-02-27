#!/usr/bin/env python3

import sys
import requests

def get_known_nodes(api_url, port):

    # TODO: Remove this later. We do not want the node to broadcast to itself.

    req_url = f"http://{api_url}/addr?port={port}"
    req = requests.get(req_url)
    if req.status_code != 200:
        return []
    return req.json()


if __name__ == "__main__":
    
    r = requests.get(f"{api_url}/ping")

    data = {"id": 1, "name": "Sample"}

    r = requests.get(f"{api_url}/name", params=data)
    assert r.status_code == 200 

    r = requests.post(f"{api_url}/name", data=data)
    assert r.status_code == 200 

    # Print the response status code
    print(r.status_code)

    # Print the response body
    print(r.text)