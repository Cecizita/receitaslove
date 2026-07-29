from flask import *
from config import *
from dao.usuario_dao import UsuarioDAO

admin = Blueprint('bp_admin', __name__)


@admin.route('/')
def index():
    return render_template(
        'adminpage.html',comidas=comidas, bebidas=bebidas)



@admin.route('/cadastrarcomida', methods=['POST'])
def cadastrar_comida():
    nome = request.form.get('nome')
    comidas.append(nome)
    return render_template('adminpage.html',comidas=comidas)


@admin.route('/cadastrarbebida', methods=['POST'])
def cadastrar_bebida():
    nome = request.form.get('nome')
    bebidas.append(nome)
    return render_template('adminpage.html',bebidas=bebidas)



@admin.route('/removerusers/<login>')
def excluir_usuario(login):

    u = UsuarioDAO.buscar_por_login(login)
    if u:
        UsuarioDAO.excluir(u)
        usuarios = UsuarioDAO.listar_todos()
        return render_template('removerusers.html', usuarios=usuarios)
    else:
        usuarios = UsuarioDAO.listar_todos()
        msg = 'usartuioooooooooo'
        return render_template('removerusers.html', usuarios=usuarios, msg=msg)

@admin.route('/listarremoverusers')
def listarexcluir_usuario():
    usuarios = UsuarioDAO.listar_todos()
    return render_template('removerusers.html', usuarios=usuarios)