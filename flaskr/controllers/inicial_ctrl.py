from flask import Blueprint, render_template

bp = Blueprint(
    'inicial',
    __name__,
    template_folder='templates' )


class InicialCtrl:
    @bp.route('/', methods=['GET'])
    def inicial():
        return render_template(
            'base.html')