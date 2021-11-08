from flask import request, render_template, Blueprint, redirect, url_for
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
            'pessoa/listagem.html',
            pessoas=pessoas )


    @bp.route('/pessoas/nova', methods=['GET'])
    def nova():
        return render_template(
            'pessoa/formulario.html',
            pessoa = None )


    @bp.route('/pessoas/editar/<id>', methods=['GET'])
    def editar(id):
        return render_template(
            'pessoa/formulario.html',
            pessoa = Pessoa.query.filter_by(id=id).first() )


    @bp.route('/pessoas/salvar', methods=['POST'])
    def salvar():
        pessoa = None
        id     = request.form.get('id')
        nome   = request.form.get('nome')
        email  = request.form.get('email')

        if nome and email:
            # inserir
            if id == '':
                pessoa = Pessoa(
                    nome  = nome,
                    email = email )
                db.session.add(pessoa)
                db.session.commit()
                return redirect(url_for('pessoas.listar'))

            # edição
            pessoa = Pessoa.query.filter_by(id=id).first()
            pessoa.nome  = nome
            pessoa.email = email
            db.session.commit()
        return redirect(url_for('pessoas.listar'))


    @bp.route('/pessoas/excluir/<id>', methods=['GET'])
    def excluir(id):
        pessoa = Pessoa.query.filter_by(id=id).first()
        db.session.delete(pessoa)
        db.session.commit()
        return redirect(url_for('pessoas.listar'))