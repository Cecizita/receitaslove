from config import db

class Bebida(db.Model):
    __tablename__ = 'bebidas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)

    def __init__(self, nome):
        self.nome = nome