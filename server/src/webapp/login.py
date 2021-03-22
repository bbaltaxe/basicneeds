from webapp import app
import uuid

import configparser
import json
import os
import traceback


from flask import Flask, jsonify, request,  session, redirect
from flask_cors import CORS

from duo_universal.client import Client, DuoException


#DUO Communications
config = configparser.ConfigParser()
config.read("webapp/duo.conf")

#session INIT
sesh_key = config['session']['session_key']
app.secret_key = sesh_key

try:
    duo_client = Client(
        client_id=config['duo']['client_id'],
        client_secret=config['duo']['client_secret'],
        host=config['duo']['api_hostname'],
        redirect_uri=config['duo']['redirect_uri'],
    )
except DuoException as e:
    print("*** DUO CONFIG ERROR. Duo.conf values are wrong ***")
    raise e

duo_failmode = config=config['duo']['failmode']


@app.route('/duo', methods=['POST'])
def login_post():
    """
    Login protocol for reading user forms on /login

    ->Accepts json
    """
    response_object = {'staus': 'success', 'msg': "NA"}
    if request.method == 'POST':
        try:
            duo_client.health_check()
        except DuoException:
            traceback.print_exc()
            if duo_failmode.upper() == "OPEN":
                response_object["msg"] = "Login 'Successful', but 2FA Not Performed. Confirm Duo client/secret/host values are correct"
            else:
                response_object["msg"] = "2FA Unavailable. Confirm Duo client/secret/host values are correct"
            return jsonify(response_object)


    post_data = request.get_json()
    username = post_data["name"]
    password = post_data["password"]

    print(username)
    print(password)
    state = duo_client.generate_state()
    session['state'] = state
    session['username'] = username
    prompt_uri = duo_client.create_auth_url(username, state)
    response_object['msg'] = prompt_uri
    return jsonify(response_object)#successful validation


#This route URL must match the redirect_uri passed to the duo client
@app.route("/duo-callback")
def duo_callback():
    response_object = {"callback_msg": ''}
    if request.args.get('error'):
        return "Got Error: {}".format(request.args)

    # Get state to verify consistency and originality
    state = request.args.get('state')

    # Get authorization token to trade for 2FA
    code = request.args.get('duo_code')

    if 'state' in session and 'username' in session:
        saved_state = session['state']
        username = session['username']
    else:
        # For flask, if url used to get to login.html is not localhost,
        # (ex: 127.0.0.1) then the sessions will be different
        # and the localhost session does not have the state
        response_object["callback_msg"] = "No saved state please login again"
        return jsonify(response_object)

    # Ensure nonce matches from initial request
    if state != saved_state:
        response_object["callback_msg"] = "Duo state does not match saved state"
        return jsonify(response_object)

    decoded_token = duo_client.exchange_authorization_code_for_2fa_result(code, username)

    # Exchange happened successfully so render success page
    response_object["callback_msg"] = "successs"
    return jsonify(response_object)



