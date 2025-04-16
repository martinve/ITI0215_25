#!/usr/bin/env python3


"""
A toy blockchain implementation
"""

from datetime import datetime as dt
import hashlib


class Block:
    def __init__(self, index, timestamp, previous_hash, data):

        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        self.data = data

    def calculate_hash(self):

        hs = f"{self.previous_hash}|{self.index}|{self.timestamp}"

        newhash = hashlib.sha256(hs.encode('utf8')).hexdigest()
        return newhash # [0:20] 
    


class BlockChain:
    def __init__(self):
        self.chain = [ self.add_genesis_block() ]

    def add_genesis_block(self):
        return Block(0, dt.timestamp(dt.now()), "", "Genesis block")

    def add_block(self, block):
        block.previous_hash = self.chain[-1].hash
        self.chain.append(block)



def debug_chain(num):

    b = BlockChain()


    for i in range(1, num + 1):

        ts = dt.timestamp(dt.now())

        block = Block(i, ts, "", f"Block data {i}")
        b.add_block(block)


    for bl in b.chain:
        print(f"Block #{bl.index}")
        print(f"Timestamp: {bl.timestamp}")
        print(f"Prev hash: {bl.previous_hash}")
        print(f"Hash: {bl.hash}")
        print(f"Data: {bl.data}")
        print()



if __name__ == "__main__":
    
    debug_chain(3)