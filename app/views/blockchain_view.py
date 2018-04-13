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
        responses:
            200: The chain was returned successfully.
            schema:
                type: object
                properties:
                    pending_data:
                        type: array
                        items:
                            type: object
                            properties:
                                hash:
                                    type: string
                                time: 
                                    type: double
                    chain:
                        type: array
                        items:
                            type: object
                            properties:
                                _prev_hash:
                                    type: string
                                _hash:
                                    type: string
                                _index:
                                    type: int
                                _nonce:
                                    type: int
                                _data:
                                    type: array
                                    items:
                                        type: object
                                        properties:
                                            hash:
                                                type: string
                                            time:
                                                type: double
                                time_stamp:
                                    type: double
        """
        return Response(jsonpickle.encode(self.chain), mimetype='application/json'), 200

    def post(self):
        """
        Mines a new block.

        responses:
            200: The block was mined successfully.
            schema:
                tyepe: object
                properties:
                    succeeded: true
        """
        self.chain.new_block()
        return jsonify(succeeded=True), 200
