# A simple REST API that invokes another REST API
# Showcasing one cool feature from Python 3.10 (Pattern Matching)
from flask import Flask, jsonify
import users_service


app = Flask(__name__)

BASE_PATH = '/fun/users/'
# instantiate the UserService
user_service = users_service.UserService()


@app.route(BASE_PATH)
def get_all_users():
    if user_service.get_all_users():
        return jsonify(user_service.get_all_users())
    else:
        return user_service.get_all_users()


# identifier is a dynamic path parameter
@app.route(BASE_PATH + '<identifier>')
def get_one_user(identifier):
    return user_service.get_single_user(identifier)
