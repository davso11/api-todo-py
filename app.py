from flask import Flask
from dotenv import load_dotenv
from os import getenv
from routes.todo_routes import todo_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(todo_bp)

PORT = int(getenv('PORT'))
app.run('127.0.0.1', port=PORT, debug=True)
