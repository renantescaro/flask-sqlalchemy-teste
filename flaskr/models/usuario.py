from flaskr import db

class Usuario(db.Model):
    id = db.Column(
        db.Integer,
        primary_key = True )

    nome = db.Column(
        db.String(64),
        index    = False,
        unique   = True,
        nullable = False )

    email = db.Column(
        db.String(80),
        index    = True,
        unique   = True,
        nullable = False )

    def __repr__(self):
        return '<Usuario %r>' % self.nome