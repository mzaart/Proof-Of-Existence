from flask import jsonify, request, Response
from flask.views import MethodView
from flask_inject import inject
import jsonpickle
from app.blokchain import BlockData

class DocumentHashView(MethodView):
    """Contains endpoints for adding/querying document hashes"""

    @inject('node')
    def __init__(self, node):
        self.chain = node.current_chain

    def get(self):
        """
        Checks whether a document hash exists.
        """
        index = request.args.get('index', type=int)
        doc_hash = request.args['hash']
        if index < 0 or index > (len(self.chain.chain)-1):
            return jsonify(suceeded=False, reason='Invalid Index'), 404

        block = self.chain.chain[index]
        for data in block.data:
            if data.hash == doc_hash:
                return jsonify({
                    'suceeded':True,
                    'hash':doc_hash,
                    'time_stamp':data.time
                }), 200
        return jsonify(suceeded=False, reason='Invalid Index'), 404

    def post(self):
        """
        Adds a new document hash to the chain (to be mined)
        """
        data = BlockData(request.json['hash'])
        index = self.chain.add_data(data)
        return jsonify(suceeded=True, index=index), 200
