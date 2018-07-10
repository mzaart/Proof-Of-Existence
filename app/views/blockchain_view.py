from flask import jsonify, Response
from flask.views import MethodView
from flask_inject import inject
import jsonpickle


class BlockchainView(MethodView):
    """Contains endpoints for interacting with the Block Chain"""

    @inject('node')
    def __init__(self, node):
        self.chain = node.current_chain

    def get(self):
        """
        Gets the current chain at the node.
        """
        return Response(jsonpickle.encode(self.chain), mimetype='application/json'), 200

    def post(self):
        """
        Mines a new block.
        """
        self.chain.new_block()
        return jsonify(succeeded=True), 200
