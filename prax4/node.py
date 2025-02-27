#!/usr/bin/env python3

import sys
import json
import shutil
import time
import os.path

import server, client

'''
- Determine if we are master node or not
- If not master node, then fetch the list of known nodes from master

'''

is_master = False
    


def extract_port(ipstring):
    return int(ipstring.split(":")[1])


def get_config_file(port):
    return f"config-{port}.json"



def load_config(port):
    '''
    Each node has its own configuration in format `config-<port>.json`
    '''
    datafile = get_config_file(port)

    if not os.path.exists(datafile):
        shutil.copyfile("config.json", datafile)

    return json.load(open(datafile))



if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("\nUsage: ./node.py <port>\n")
        sys.exit(1)

    port = int(sys.argv[1])

    config = load_config(port)
    
    is_master = port == extract_port(config["master"])
    api_url = config["master"]

    server.start(port)
    server.add_known_address(port)

    tick = 0

    while True:
        if tick == 0:
            if is_master:
                print("I am the master. Waitng for connections ...")
            else:
                print("I am a client.")  


        # TODO: How to get the list of known nodes?

        try:
            upd_nodes = client.get_known_nodes(api_url, port)
        except:
            print("No nodes fetched")
            # TODO: Fetch list from next node in network

        print("Received nodes:", upd_nodes)
        for node in upd_nodes:
            if extract_port(node) == port:
                continue
            if node not in config["nodes"]:
                config["nodes"].append(node)

        json.dump(config, open(get_config_file(port), "w"))

        tick += 1
        time.sleep(5)


