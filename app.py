import flask
from flask import *
#from application.user_services import userclass
from application_services.address_service import *
import json
 
app = Flask(__name__)


@app.route('/')
def index_page():
    return """render_template("index.html")"""

# newsId = shortuuid.uuid(url)


@app.route('/users', methods=['GET', 'POST'])
def users():
    if flask.request.method == 'POST':
        # User form['user'] for data insertion -> None
        insert_user(request.form['user'])

    elif flask.request.method == 'GET':
        # get_all_user_info() -> JSON()
        return json.dumps(get_all_user())


@app.route('/users/<userID>', methods=['GET', 'PUT', 'DELETE'])
def users_id(userID):
    if flask.request.method == 'GET':
        # get_user_info(userID) - userID get from url -> JSON
        return json.dumps(get_user_by_id(userID))

    elif flask.request.method == 'PUT':
        # update_user_info(userID) - userID get from url - request.form['user'] input form
        update_user(userID, request.form['user'])

    elif flask.request.method == 'DELETE':
        # delete_user_info(userID) - userID get from url
        delete_user(userID)


@app.route('/users/<userID>/address', methods=['GET', 'POST'])
def users_id_address(userID):
    if flask.request.method == 'POST':
        return update_address_by_uid(userID)

    elif flask.request.method == 'GET':
        return json.dumps(get_address_by_uid(userID))


@app.route('/address', methods=['GET', 'POST'])
def address():
    if flask.request.method == 'POST':
        insert_address(request.form['address'])

    elif flask.request.method == 'GET':
        # print(get_all_address())
        return json.dumps(get_all_address())


@app.route('/address/<addressID>', methods=['GET', 'PUT', 'DELETE'])
def address_id(addressID):
    if flask.request.method == 'GET':
        return json.dumps(get_address_by_aid(addressID))

    elif flask.request.method == 'PUT':
        update_address(addressID, request.form['address'])

    elif flask.request.method == 'DELETE':
        delete_address(addressID)


@app.route('/address/<addressID>/users', methods=['GET', 'POST'])
def address_id_users(addressID):
    if flask.request.method == 'POST':
        return insert_user_by_addressid(addressID)

    elif flask.request.method == 'GET':
        return json.dumps(get_user_by_addressid(addressID))


if __name__ == '__main__':
    app.run()