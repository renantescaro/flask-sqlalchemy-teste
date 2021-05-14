from flaskr.routes.usuario_route import UsuarioRoute

class Rotas:
    def __init__(self, app):
        self._app = app
        self._iniciar_rotas()


    def _iniciar_rotas(self):
        UsuarioRoute(self._app)