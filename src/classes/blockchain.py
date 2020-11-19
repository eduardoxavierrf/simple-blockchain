from .block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block(0, "01/01/2020", "Genesis block", "0")

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]
    
    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)

    def isChainValid(self):
        for i, block  in enumerate(self.chain):
            if(block.index != 0):
                previousBlock = self.chain[i - 1]

                if (block.hash != block.calculateHash()):
                    return False
                
                if(block.previousHash != previousBlock.hash):
                    return False
        
        return True
