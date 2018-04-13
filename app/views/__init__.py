from app import app
from blockchain_view import BlockchainView
from document_hash_view import DocumentHashView
from nodes_view import NodesView

app.add_url_rule('/api/chain/', view_func=BlockchainView.as_view('chain'))
app.add_url_rule('/api/document/', view_func=DocumentHashView.as_view('document'))
app.add_url_rule('/api/nodes/', view_func=NodesView.as_view('nodes'))
