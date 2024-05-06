Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from hashlib import sha256
... import json
... import time
... class Block:
... def __init__(self, index, transactions, timestamp, previous_hash):
... self.index = index
... self.transactions = transactions
... self.timestamp = timestamp
... self.previous_hash = previous_hash
... self.nonce = 0
... def compute_hash(self):
... """
... A function that return the hash of the block contents.
... """
... block_string = json.dumps(self.__dict__, sort_keys=True)
... return sha256(block_string.encode()).hexdigest()
SyntaxError: multiple statements found while compiling a single statement
