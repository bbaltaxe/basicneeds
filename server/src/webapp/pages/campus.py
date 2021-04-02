 from flask import current_app
 
 #home campus route 
@current_app.route('/campuses', methods=['GET'])
def all_campuses(): 
    response_object = {'status': 'success'}
    response_object['campuses'] = CAMPUSES
    return jsonify(response_object)
