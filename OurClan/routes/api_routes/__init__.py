from flask import Blueprint

api_bp = Blueprint('api_routes', __name__)

from OurClan.routes.api_routes import members 