#!/usr/bin/env python3

import requests

api_url = "http://127.0.0.1:5000"

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