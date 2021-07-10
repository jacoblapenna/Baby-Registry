from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__.split('.')[0])

from registry_app import views
