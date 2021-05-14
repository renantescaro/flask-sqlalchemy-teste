from flask import request, render_template
from flaskr import db
from flaskr.models.usuario import Usuario

class UsuarioRoute:
    def __init__(self, app):
        self._app = app

        self._app.add_url_rule(
            '/usuario/listar',
            'usuario-listar',
            self.listar )

        self._app.add_url_rule(
            '/usuario/criar',
            'usuario-criar',
            self.criar )

        self._app.add_url_rule(
            '/usuario/inserir',
            'usuario-inserir',
            self.inserir )


    def listar(self):
        usuarios = Usuario.query.all()
        return render_template(
            'listagem.html',
            usuarios=usuarios )


    def criar(self):
        db.create_all()
        return '<h1>Tabela criada com sucesso!</h1>'


    def inserir(self):
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