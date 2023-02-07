from os import getenv
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from config.database import Database
from models.todo_model import Todo
from models.user_model import User


load_dotenv()


db = Database()
db_connection = db.createConnection()


todo = Todo(db_connection)
user = User(db_connection)


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


@cross_origin()
@app.post('/api/todos/stats')
def active_todos_controller():
    req_body = request.get_json()

    print(req_body.get('userId'))

    if not req_body.get('userId'):
        db_connection.close()
        resp = make_response(jsonify(
            message='Missing paramater `userId` in the req body',
            userId=req_body.get('userId')
        ))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp, 400

    # check if user exist
    user_id = req_body['userId']
    is_user = user.get_user(user_id)

    if not is_user:
        db_connection.close()
        resp = make_response(jsonify(
            message="No User With That ID Found",
            userId=user_id,
        ))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp, 401

    active_todos_numb = todo.get_active()
    done_todos_numb = todo.get_completed()

    db_connection.close()
    resp = make_response(jsonify(
        active=active_todos_numb[0],
        done=done_todos_numb[0],
    ))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp, 200


PORT = int(getenv('PORT'))
app.run('127.0.0.1', port=PORT, debug=True)
