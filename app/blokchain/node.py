import requests
import jsonpickle

class Node(object):
    """
    This class represents a single node and is responsible for syncing up 
    the block chain with the network and resolving confilcts.

    Attributes:
        current_chain (Blockchain): The block chain of the current node.
        neighbours (set of str): Contains URLs of nodes on the network
    """
    def __init__(self, current_chain):
        self.current_chain = current_chain
        self.neighbours = set()

    def add_node(self, node):
        """
        Adds a URL of a node

        Args:
            node (str): The URL of the node
        """
        self.neighbours.add(node)

    def resolve(self):
        """
        Resolves any conflicts and sets the longest chain as the current chain.
        """
        new_chain = self.current_chain
        for node in self.neighbours:
            url = 'http://{node}/api/chain'.format(node=node)
            print node
            print url
            response = requests.get(url)
            print type(response.json())
            chain = jsonpickle.decode(response.text)
            if len(chain.chain) > len(new_chain.chain):
                new_chain = chain

        self.current_chain = new_chain
        return self.current_chain
