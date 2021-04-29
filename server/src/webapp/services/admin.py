from flask import current_app, Blueprint, jsonify, request

from webapp.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/addservice', methods=(['GET', 'POST']))
def add_service():
    response_object = {
        "status" : "fail"
    }

    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)

        name =          post_data['name']
        location =      post_data['campus']
        resource =      post_data['resource_type']
        description =   post_data['description']
        hours =         post_data['hours']
        email =         post_data['email']

        db = get_db()
        error = False

        service_found = db.execute('SELECT id FROM service WHERE name = ?', (name,)).fetchone()

        if service_found is not None:
            response_object['msg'] = "There's already a service with that name"
            error = True

        if not error:
            db.execute(
                "INSERT INTO service ('name', 'resource', 'location', 'description', 'hours', 'email') VALUES (?, ?, ?, ?, ?, ?)",
                (name, resource, location, description, hours, email)
            )
            db.commit()
            response_object['status'] = 'success'
            return jsonify(response_object), 200
        else: 
            return jsonify(response_object), 401

@bp.route('/getservice', methods=(['POST']))
def get_service():
    response_object = {"get_service": "empty"}
    if request.method == 'POST':
        post_data = request.get_json()
    
        campuses_selected = post_data['campuses']
        categories_selected = post_data['categories']
        print(campuses_selected)
        db_select = 'SELECT * FROM SERVICE WHERE location = ?', ()
        



    return jsonify(response_object), 401


