#!/usr/bin/env python3

import sys
import requests

api_url = "http://127.0.0.1:5000"

def get_known_nodes(port):
    req_url = f"{api_url}/addr?port={port}"
    req = requests.get(req_url)

    if req.status_code != 200:
        return -1

    res = req.json()
    return res


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