from flask import jsonify, request, Response
from flask.views import MethodView
from flask_inject import inject
import jsonpickle
from app.blokchain import Node

class NodesView(MethodView):
    """Contains endpoints for interacting with the node."""

    @inject('node')
    def __init__(self, node):
        self.node = node

    def get(self):
        """
        Fetches and returns the longest chain in the network

        responses:
            200: Data fetched successfully
            schema:
                type: object
                properties:
                    neighbours:
                        type: array
                        items:
                            type: string
                            description: URL's of other nodes on the network
                    chain:
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
        self.node.resolve()
        return Response(jsonpickle.encode(self.node), mimetype='application/json'), 200

    def post(self):
        """
        Adds a URL of another node to the network to the current node.

        parameters:
            node_id:
                type: string
                description: The nodes URL

        responses:
            200: URL added successfully
            schema:
                type: object
                properties:
                    succeeded: true
        """
        self.node.add_node(request.json['node_id'])
        return jsonify(succeeded=True), 200
