from os import getenv
from dotenv import load_dotenv
from flask import Flask
from routes.contact_routes import contact_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(contact_bp)

PORT = int(getenv('PORT'))
app.run(port=PORT)
