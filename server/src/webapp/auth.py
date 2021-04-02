import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from webapp.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    response_object = {
        "insert_status": "success",
        "msg": "registration successful"
    }

    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        username = post_data['name']
        password = post_data['password']

        db = get_db()
        error = False
        user_found = db.execute('SELECT id FROM user WHERE username = ?', (username,)).fetchone()
    
        print(user_found)

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

        print(error)
        if not error:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()

    return jsonify(response_object)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    response_object = {"status": "success"}
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = False
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            request_object['msg'] = 'Incorrect username.'
            error = True
        elif not check_password_hash(user['password'], password):
            request_object['msg'] = 'Incorrect password.'
            error = True

        #proper auth
        if not error:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))