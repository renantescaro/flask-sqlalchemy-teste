from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from models.usuario import Usuario

db  = SQLAlchemy()
app = Flask('api_clima', static_url_path='/static', static_folder='static')
db.init_app(app)
db.create_all()

@app.route('/', methods=['GET'])
def user_records():
    username = request.args.get('user')
    email    = request.args.get('email')
    if username and email:
        new_user = Usuario(
            username = username,
            email    = email,
            created  = dt.now(),
            admin    = False,
            bio      = "In West Philadelphia born and raised, on the \
                        playground is where I spent most of my days" )

        db.session.add(new_user)
        db.session.commit()
    return make_response(f"{new_user} successfully created!")

if __name__ == "__main__":
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    app.secret_key = '+777/ sUper_SeCret-kEY ! |777*'
    app.run(debug=True, host='192.168.1.182', port=5000)