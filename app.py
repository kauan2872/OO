from flask import Flask
from config import configure
from database import db

def create_app(*args, **kwargs):
    app = Flask(__name__)
    configure(app)
    return app
