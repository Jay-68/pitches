from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy


def create_app(config_name):

    # initializing the application
    app = Flask(__name__)
