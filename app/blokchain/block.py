import time
import re
import json

class Block(object):
    """Represents a block in a block chain."""

    def __init__(self):
        self._index = None
        self._prev_hash = None
        self._data = None
        self._time_stamp = time.time()
        self._nonce = None
        self._hash = None

    @classmethod
    def from_args(cls, index, prev_hash, data):
        block = cls()
        block._index = index
        block.set_prev_hash = prev_hash
        block.set_data = data
        return block

    @classmethod
    def from_dict(cls, dic):
        block = cls()
        block.__dict__ = dic
        return block

    @property
    def index(self):
        """int: The block's index."""
        return self._index

    @property
    def prev_hash(self):
        """
        str: A hex string representing the SHA-256 hash of the previous block.

        Raises:
            ValueError: If the hash is not valid.
        """
        return self._prev_hash

    @prev_hash.setter
    def set_prev_hash(self, hash_str):
        if not hash_str:
            raise ValueError('Hash string can not be empty')

        if not re.match(r'^[A-Fa-f0-9]{64}$', hash_str):
            raise ValueError('Hash should be a 64 hex character string')

        self._prev_hash = hash_str

    @property
    def time_stamp(self):
        """float: Denotes the creation time of the block as a Unix time stamp."""
        return self._time_stamp

    @property
    def data(self):
        """
        obj: Represents the data stored in the block.

        Raises:
            ValueError: If the data is empty.
        """
        return self._data

    @data.setter
    def set_data(self, val):
        self._data = val

    @property
    def nonce(self):
        """int: The block's nonce."""
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        self._nonce = nonce

    @property
    def hash(self):
        """str: The hash of the Index, Data and Nonce"""
        return self._hash

    @hash.setter
    def hash(self, hash_str):
        self._hash = hash_str

    def __str__(self):
        """
        Provides string representaion of the block.

        Returns:
            A JSON representation of the block.
        """
        return json.dumps(self.__dict__, indent=4, separators=(',', ': ')).encode()
