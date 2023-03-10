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

    important_todos_numb = todo.get_important()
    normal_todos_numb = todo.get_normal()

    db_connection.close()
    resp = make_response(jsonify(
        normal=normal_todos_numb[0],
        important=important_todos_numb[0],
    ))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp, 200


PORT = int(getenv('PORT'))
app.run('192.168.252.203', port=PORT, debug=True)
