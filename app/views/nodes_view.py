from flask import jsonify, request, Response
from flask.views import MethodView
from flask_inject import inject
import jsonpickle


class NodesView(MethodView):
    """Contains endpoints for interacting with the node."""

    @inject('node')
    def __init__(self, node):
        self.node = node

    def get(self):
        """
        Fetches and returns the longest chain in the network
        """
        self.node.resolve()
        return Response(jsonpickle.encode(self.node), mimetype='application/json'), 200

    def post(self):
        """
        Adds a URL of another node to the network to the current node.
        """
        self.node.add_node(request.json['node_id'])
        return jsonify(succeeded=True), 200
