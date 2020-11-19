from hashlib import sha256

class Block:
    def __init__(self, index, timestamp, data, previousHash = '' ):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def __str__(self):
        return {"index": self.index, "timestamp": self.timestamp, "data": self.data, "previousHash": self.previousHash, "hash": self.hash}
    def calculateHash(self):
        return sha256((str(self.index)+ self.previousHash + self.timestamp + str(self.data)).encode()).hexdigest()