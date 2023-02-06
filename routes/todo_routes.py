from flask import Blueprint, request, jsonify
from models.todo_model import Todo
from models.user_model import User
from config.database import Database

todo_bp = Blueprint('todo', __name__)

db = Database()
db_connection = db.createConnection()

# instanciate todo model
todo = Todo(db_connection)
user = User(db_connection)

@todo_bp.post('/api/todos/active')
def active_todos_controller():
    req_body = request.get_json()

    if not req_body.get('userId'):
        db_connection.close()
        return jsonify(
            message='Missing paramater `userId` in the req body',
            userId=req_body.get('userId')
        ), 400

    # check if user exist
    user_id=req_body['userId']
    is_user = user.get_user(user_id)

    if not is_user:
        db_connection.close()
        return jsonify(
            message="No User With That ID Found",
            userId=user_id,
        ), 401


    active_todos_numb = todo.get_active()

    db_connection.close()
    return jsonify(
        active=active_todos_numb[0]
    ), 200


@todo_bp.post('/api/todos/done')
def done_todos_controller():
    req_body = request.get_json(force=True)
    user_id=req_body.get('userId')

    if not user_id:
        db_connection.close()
        return jsonify(
            message='Missing paramater `userId` in the req body',
            userId=user_id
        ), 400

    # check if user exist
    is_user = user.get_user(user_id)

    if not is_user:
        db_connection.close()
        return jsonify(
            message="No User With That ID Found",
            userId=user_id,
        ), 401

    done_todos_numb = todo.get_completed()

    db_connection.close()
    return jsonify(
        done=done_todos_numb[0]
    ), 200
