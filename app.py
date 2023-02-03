from flask import Flask
from routes.contact_routes import contact_bp

app = Flask(__name__)

app.register_blueprint(contact_bp)

app.run(port=9200)
