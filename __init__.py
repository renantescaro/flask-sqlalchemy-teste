from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from models.usuario import Usuario

app = Flask(
    'api_clima',
    static_url_path='/static',
    static_folder='static' )

app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False,
        SQLALCHEMY_DATABASE_URI = 'mysql://root:Tz0rKy2003@localhost/teste' )

app.run(debug=True, host='192.168.1.182', port=5000)

db = SQLAlchemy()
db.init_app(app)

@app.route('/criar', methods=['GET'])
def criar_tabela_usuarios():
    db.create_all()
    return '<h1>Tabela criada com sucesso!</h1>'

@app.route('/inserir', methods=['GET'])
def inserir_usuario():
    nome  = request.args.get('nome')
    email = request.args.get('email')
    if nome and email:
        usuario = Usuario(
            nome  = nome,
            email = email )

        db.session.add(usuario)
        db.session.commit()
    return render_template(
        f"{usuario} criado com sucesso!" )

@app.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template(
        'listagem.html',
        usuarios=usuarios
    )