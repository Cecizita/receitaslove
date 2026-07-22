from config import db

class Comida(db.Model):
    __tablename__ = 'comidas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)

    def __init__(self, nome):
        self.nome = nome