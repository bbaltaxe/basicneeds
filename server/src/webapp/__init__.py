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


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

CAMPUSES = [
    
    'UC Santa Cruz', 
    'UC Berkeley', 
    'UC Davis', 
    'UC Irvine', 
    'UC Los Angeles', 
    'UC Merced', 
    'UC Riverside', 
    'UC San Diego', 
    'UC San Francisco', 
    'UC Santa Barbara'
]

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

    from . import auth 
    app.register_blueprint(auth.bp)

    return app

# enable CORS
#CORS(app, resources={r'/*': {'origins': '*'}})

"""
def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#home campus route 
@app.route('/campuses', methods=['GET'])
def all_campuses(): 
    response_object = {'status': 'success'}
    response_object['campuses'] = CAMPUSES
    return jsonify(response_object)

# books example route
@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)
"""

if __name__ == '__main__':
    app.run()
