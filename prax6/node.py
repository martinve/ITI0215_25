#!/usr/bin/env python3

import sys
import json
import shutil
import time
import os.path

import server, client
import config as cfg

from logger import logger

'''
- Determine if we are master node or not
- If not master node, then fetch the list of known nodes from master

'''

is_master = False
    


def extract_port(ipstring):
    return int(ipstring.split(":")[1])






if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("\nUsage: ./node.py <port>\n")
        sys.exit(1)

    port = int(sys.argv[1])

    config = cfg.load_config(port)
    
    is_master = port == extract_port(config["master"])
    api_url = config["master"]

    server.start(port)
    cfg.add_known_address(port)

    tick = 0

    while True:
        if tick == 0:
            if is_master:
                logger.info("I am the master. Waitng for connections ...")
            else:
                logger.info("I am a client.")  

        
        upd_nodes = client.get_known_nodes(api_url, port)

        if -1 == upd_nodes:
            cfg.remove_address(api_url)
            time.sleep(5)
            continue

        logger.debug(f"Received nodes: {upd_nodes}")
        for node in upd_nodes:
            if extract_port(node) == port:
                continue
            
            nodes = client.get_known_nodes(node, port)

            # The node does not respond, thus we do not want to add it
            if nodes == -1:
                continue

            if node not in config["nodes"]:
                config["nodes"].append(node)

            


        cfg.save_nodes(port, config)


        tick += 1
        time.sleep(5)


