import re
import hashlib
from block import Block
from proof_of_work import ProofOfWork

class Blockchain(object):
    """
    Represents a Block Chain.

    Attributes:
        chain (list of Block): Holds the blocks of the chain.
        pending_data (list of obj): Contains data to be added to the chain
    """

    def __init__(self):
        self.chain = []
        self.pending_data = []
        self._create_genesis_block()

    @classmethod
    def from_dict(cls, dic):
        block_chain = cls()
        block_chain.pending_data = dic['pending_data']
        for block in dic['chain']:
            block_chain.pending_data.append(Block.from_dict(block))
        return block_chain


    def _create_genesis_block(self):
        """Creates a genesis block for the chain"""
        block = Block.from_args(len(self.chain), '0' * 64, [])
        ProofOfWork.mine(block)
        self.chain.append(block)

    def new_block(self):
        """Creates and mines a new block then adds it to the chain."""
        block = Block.from_args(len(self.chain), self.last_block.hash, self.pending_data)
        ProofOfWork.mine(block)
        self.chain.append(block)
        self.pending_data = []

    def add_data(self, data):
        """
        Adds data to be added to the chain.

        Args:
            data (obj): The data to be added

        Returns:
            The index of the block that will contain the data.
        """
        if not data:
            raise ValueError('Data should not be empty.')
        self.pending_data.append(data)
        print self.pending_data
        return len(self.chain)

    @property
    def last_block(self):
        """Block: The last block in the chain."""
        return self.chain[-1]

    def is_chain_valid(self):
        """
        Chaecks if the Block Chain is valid.

        Returns:
            True if the chain is valid. False otherwise.
        """
        prev_block = self.chain[0]
        i = 1
        while i < len(self.chain):
            current = self.chain[i]

            if not re.match(r'^[A-Fa-f0-9]{64}$', current.hash):
                return False

            if current.hash[:ProofOfWork.difficulty] != '0' * ProofOfWork.difficulty:
                return False

            block_str = ''.join([str(current.index), str(current.data),
                                 current.prev_hash, str(current.nonce)])
            if hashlib.sha256(block_str).hexdigest() != current.hash:
                return False

            if current.prev_hash != prev_block.hash:
                return False

            prev_block = current
            i += 1

        return True
