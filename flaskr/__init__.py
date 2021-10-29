from flask import Flask
from flaskr.controllers.pessoa_ctrl import bp as bp_pessoas
from flaskr.models import db


def create_app():
    app = Flask(
        __name__,
        static_url_path = '/static',
        static_folder   = 'static' )

    app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False,
        SQLALCHEMY_DATABASE_URI = 'mysql://usuario:senha@localhost/sql_alchemy' )

    db.init_app(app)
    app.register_blueprint(bp_pessoas)

    with app.app_context():
        db.create_all()

    return app