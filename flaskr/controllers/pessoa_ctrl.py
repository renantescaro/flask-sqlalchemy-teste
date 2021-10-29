from flask import request, render_template, Blueprint
from flaskr.models.pessoa import Pessoa
from flaskr.models.pessoa import db

bp = Blueprint(
    'pessoas',
    __name__,
    template_folder='templates' )


class PessoaCtrl:
    @bp.route('/pessoas', methods=['GET'])
    def listar():
        pessoas = Pessoa.query.all()
        return render_template(
            'listagem.html',
            pessoas=pessoas )


    @bp.route('/pessoas/nova', methods=['GET'])
    def nova():
        #db.create_all()
        return '<h1>form nova</h1>'


    @bp.route('/pessoas/editar', methods=['GET'])
    def editar():
        #db.create_all()
        return '<h1>form editar</h1>'


    @bp.route('/pessoas/salvar', methods=['POST'])
    def salvar():
        nome  = request.args.get('nome')
        email = request.args.get('email')
        if nome and email:
            pessoa = Pessoa(
                nome  = nome,
                email = email )

            db.session.add(pessoa)
            db.session.commit()
        return render_template(
            f"{pessoa} criado com sucesso!" )