from config import db
from modelos.usuario import Usuario


class UsuarioDAO:
    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()

    @staticmethod
    def listar_todos():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_login(login):
        return Usuario.query.filter_by(login=login).first()

    @staticmethod
    def excluir(usuarios):
        db.session.delete(usuarios)
        db.session.commit()