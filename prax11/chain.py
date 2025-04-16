#!/usr/bin/env python3


"""
A toy blockchain implementation

Implemented:
# 11_01: Need to add Chain.is_valid method
# 11_01_01: Need to update calculate_hash with self.data for block
# 11_02: Validate transactions
# 11_03: Add Proof of Work 
	- add `nonce` variable to block class
# 11_04: Add self.difficulty variable to blockchain

# 11_05: Basic transaction object, creation handling
# 11_06: Block: replace `index`, with `transactions` list
# 11_07: Update blockchain to manage transactions and mining rewards

Not implemented:
- Mining rewards
- Transaction integrity balance checking

"""

from datetime import datetime as dt
import hashlib
from pprint import pprint
import sys



class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __repr__(self):
        return f"Transaction({self.sender}, {self.recipient}, {self.amount})"


class Block:
    def __init__(self, index, timestamp, previous_hash, transactions):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.nonce = 0
        self.difficulty = 0

        self.hash = self.calculate_hash()


    def calculate_hash(self, debug=False):
        hs = f"{self.previous_hash}|{self.index}|{self.timestamp}|{self.transactions}|{self.nonce}"
        newhash = hashlib.sha256(hs.encode('utf8')).hexdigest()

        if debug:
            pprint({
                "debug": debug,
                "prev_hash": self.previous_hash,
                "index": self.index,
                "timestamp": self.timestamp,
                "transactions": self.transactions,
                "hs": hs,
                "newhash": newhash
            }, indent=2)
            print()

        return newhash # [0:20] 
    

    def mine_block(self):
        while self.hash[:self.difficulty] != "0" * self.difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash(debug=False) 
            print("Block hash:",self.hash)
        return self


class BlockChain:
    def __init__(self):
        self.chain = [ self.add_genesis_block() ]
        self.pending_transactions = []


    def mine_transactions(self):
        block = Block(len(self.chain), dt.timestamp(dt.now()), self.chain[-1].hash, self.pending_transactions)
        block.mine_block()
        self.chain.append(block)
        self.pending_transactions = []


    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)


    def add_genesis_block(self):
        return Block(0, dt.timestamp(dt.now()), "", [])

    def add_block_hash(self, block):
        """
        previous version w/o mining
        """
        block.previous_hash = self.chain[-1].hash
        newhash = block.calculate_hash()
        block.hash = newhash
        self.chain.append(block)

    def add_block(self, block):
        block.previous_hash = self.chain[-1].hash   
        new_block = block.mine_block() 
        self.chain.append(new_block)   

    def is_valid(self):

        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False


        return True



def debug_validate_chain(b):
    print("Chain is valid:", b.is_valid())
    print("Change data in chain")

    # b.chain[1].data = "Changed data"
    print("Chain is valid:", b.is_valid())    

    print("Change some hash in chain")
    # b.chain[1].hash = "Changed hash"
    print("Chain is valid:", b.is_valid())


def debug_chain(num, b):
    
    for i in range(1, num + 1):

        ts = dt.timestamp(dt.now())

        block = Block(i, ts, "", f"Block data {i}")
        b.add_block(block)


    for bl in b.chain:
        debug_block(bl)

    # debug_validate_chain(b)


def debug_transactions(chain):

    chain.add_transaction(Transaction("sender", "recipient", 5))
    chain.add_transaction(Transaction("sender", "recipient", 4))
    chain.add_transaction(Transaction("sender", "recipient", 8))

    chain.mine_transactions()

    for bl in chain.chain:
        debug_block(bl)




def debug_block(bl):
    print(f"Block #{bl.index}")
    print(f"Timestamp: {bl.timestamp}")
    print(f"Prev hash: {bl.previous_hash}")
    print(f"Hash: {bl.hash}")
    print(f"Transactions: {bl.transactions}")
    print()


if __name__ == "__main__":
    chain = BlockChain()

    # debug_chain(3, chain)
    debug_transactions(chain)