from classes.blockchain import Blockchain
from classes.block import Block

election = Blockchain()

election.addBlock(Block(1, "02/02/2020", { "candidate": 1}))
election.addBlock(Block(2, "20/02/2020", { "candidate": 2}))

print(election.isChainValid())