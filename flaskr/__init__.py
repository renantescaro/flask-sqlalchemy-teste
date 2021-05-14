from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskr.routes.rotas import Rotas

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path = '/static',
        static_folder   = 'static' )

    app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False,
        SQLALCHEMY_DATABASE_URI     = 'mysql://USUARIO:SENHA@localhost/teste' )

    db.init_app(app)

    Rotas(app)
    return app