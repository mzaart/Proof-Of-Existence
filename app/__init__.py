from flask import Flask
from flask_inject import Inject
from app.blokchain import Blockchain
from app.blokchain import Node

app = Flask(__name__, instance_relative_config=True)

# configure di
inj = Inject(app)
inj.map(node=Node(Blockchain()))

from app.views import BlockchainView