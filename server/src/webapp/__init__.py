import os
import uuid
import json
import traceback
import sqlite3
import click

from flask import Flask, jsonify, request, current_app, g
from flask.cli import with_appcontext
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from duo_universal.client import Client, DuoException

# configuration
DEBUG = True

# app init
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'webapp.sqlite')
    )

    CORS(app, resources={r'/*': {'origins': '*'}})

    if test_config is None:
        #load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 

    from . import db
    db.init_app(app)


    #REGISTER IN FACTORY
    #--------------------
    from . import auth 
    app.register_blueprint(auth.bp)

    from .static_pages import campus 
    app.register_blueprint(campus.bp)

    return app


if __name__ == '__main__':
    app.run()
