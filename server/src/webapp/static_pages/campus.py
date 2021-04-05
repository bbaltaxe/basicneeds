from flask import current_app, Blueprint, jsonify    


bp = Blueprint('campus', __name__)


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
    'UC Santa Barbara',
    
]

 #home campus route 
@bp.route('/campuses', methods=['GET'])
def all_campuses(): 
    response_object = {'status': 'success'}
    response_object['campuses'] = CAMPUSES
    return jsonify(response_object)
