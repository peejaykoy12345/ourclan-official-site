from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ILOVESKIBIDITOILET'

from OurClan.routes.general import general_bp

app.register_blueprint(general_bp)