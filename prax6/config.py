import json
import shutil
import os


addrlist = []


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


def save_nodes(port, config):
    f = get_config_file(port)
    json.dump(config, open(f, "w"))


def get_known_addresses(port=False):
    # TODO: Do not return address with :<port>
    return addrlist
    

def add_known_address(port):

    # TODO: Where to save this data?

    new_addr = f"127.0.0.1:{port}"
    if new_addr in addrlist:
        print(f"Port:{port} is already in the list")
    else:
        addrlist.append(new_addr)
        # TODO: Do not return address with :<port>
    return addrlist


def remove_address(addr):
    if addr in addrlist:
        addrlist.remove(addr)