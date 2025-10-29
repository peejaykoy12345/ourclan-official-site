from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ILOVESKIBIDITOILET'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from OurClan.routes.general import general_bp
from OurClan.routes.api_routes import api_bp

app.register_blueprint(general_bp)
app.register_blueprint(api_bp)