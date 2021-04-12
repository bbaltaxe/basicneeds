import functools
import uuid
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)

from flask_cors import CORS
from werkzeug.security import check_password_hash, generate_password_hash

from webapp.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    response_object = {
        "insert_status": "success",
        "msg": "registration successful",
    }

    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']

        db = get_db()
        error = False
        user_found = db.execute('SELECT id FROM user WHERE username = ?', (username,)).fetchone()


        if not username:
            response_object['insert_status'] = "fail"
            response_object['msg'] = "Username is required"
            error = True
        elif not password:
            response_object['insert_status'] = "fail"
            response_object['msg'] = 'Password is required.'
            error = True
        elif user_found is not None:
            response_object['insert_status'] = "fail"
            response_object['msg'] = "User already registered"
            error = True

        if not error:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()

    return jsonify(response_object)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    response_object = {
        "status": "success",
        "auth": "fail"
    }
    
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data['username']
        password = post_data['password']
        print(post_data)
        db = get_db()
        error = False
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        print(user)
        if user is None:
            response_object['msg'] = 'Incorrect username.'
            error = True
        elif not check_password_hash(user['password'], password):
            response_object['msg'] = 'Incorrect password.'
            error = True

        #proper auth
        if not error:

            response_object['msg'] = "Login Successful"
            response_object['auth'] = "success"
            response_object['token'] = uuid.uuid1()
            return jsonify(response_object), 200
        else:
            return jsonify(response_object), 401
 
@bp.route('/logout')
def logout():
    return redirect(url_for('index'))
