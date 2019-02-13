from flask import Flask, Blueprint
from flask_cors import CORS
from flask_mail import Mail
from .api.v2 import version2 as v2
from app.database import QuestionerDB
from app import config

mail = Mail()


def create_app(configuration="development"):
    """Development cofiguration"""
    app = Flask(__name__)
    app.config.from_object(config.config[configuration])
    QuestionerDB.dbconnection(app.config["DB_URL"])
    QuestionerDB.create_tables()
    app.register_blueprint(v2)
    app.url_map.strict_slashes = False
    mail.init_app(app)
    CORS(app)

    return app
