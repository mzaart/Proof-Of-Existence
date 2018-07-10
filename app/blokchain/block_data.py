import time


class BlockData(object):
    """
    Represents the data to be stored in a block in the block chain.

    The data is compromised of a hash digest of the document and a time stamp
    representing the time of verification.

    Attributes:
        time (float): The document time stamp in Unix time.
        hash (str): A string represnting the hash digest of the document.
    """

    def __init__(self, hash_str):
        """
        Args:
            hash_str (str): The hash digest of the document.
        """
        self.time = time.time()
        self.hash = hash_str
