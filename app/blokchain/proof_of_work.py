import hashlib


class ProofOfWork(object):
    """Provides utility methods for Proof of Work"""

    difficulty = 4
    """int: The difficulty level of the Proof of Work algorithm"""

    @staticmethod
    def mine(block):
        """
        Sets a nonce to  block.

        Args:
            block (Block): The block to mine.
        """
        block_str = ''.join([str(block.index), str(block.data), block.prev_hash])
        nonce = 0
        hash_str = ProofOfWork.is_nonce_valid(block_str, nonce)
        while hash_str is None:
            nonce += 1
            hash_str = ProofOfWork.is_nonce_valid(block_str, nonce)
        block.nonce = nonce
        block.hash = hash_str

    @staticmethod
    def is_nonce_valid(block_str, nonce):
        """
        Validates a nonce.

        Args:
            block_str (str): A string representation of a block
            nonce (int): The nonce to check

        Returns:
            A hex string representing the SHA256 hash if the nonce is valid.
            Returns None otherwise.
        """

        hash_str = hashlib.sha256(block_str + str(nonce)).hexdigest()
        if hash_str[:ProofOfWork.difficulty] == '0' * ProofOfWork.difficulty:
            return hash_str
        else:
            return None
