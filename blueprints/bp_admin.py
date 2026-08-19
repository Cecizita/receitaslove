from flask import *

from dao.usuario_dao import UsuarioDAO
from config import comidas
from config import bebidas

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
    print('entrou no remover user', u)
    if u:
        print('veio')
        UsuarioDAO.excluir(u)
        clientes = UsuarioDAO.listar_todos()
        return render_template('adminpage.html', usuarios=clientes, comidas=comidas, bebidas=bebidas)
    else:
        print('nao veio')
        usuarios = UsuarioDAO.listar_todos()
        msg = 'usartuioooooooooo'
        return render_template('adminpage.html', usuarios=usuarios, msg=msg)

@admin.route('/listarremoverusers')
def listarexcluir_usuario():
    usuarios = UsuarioDAO.listar_todos()
    return render_template('removerusers.html', usuarios=usuarios)