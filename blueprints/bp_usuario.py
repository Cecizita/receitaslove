from flask import *
from modelos.usuario import Usuario
from dao.usuario_dao import UsuarioDAO
from config import comidas
from config import bebidas

usuario = Blueprint('bp_usuario',__name__)
usuarios = []
@usuario.route('/')
def index():
    return render_template('index.html')


@usuario.route('/cadastrar' , methods=['POST'])
def fazercadastro():
    nome = request.form.get('nome')
    login = request.form.get('login')
    senha = request.form.get('senha')
    novo_user = Usuario(nome=nome, login=login ,senha=senha)
    UsuarioDAO.salvar(novo_user)

    return render_template('index.html')


@usuario.route('/login', methods=['POST' , 'GET'])
def login():
    login_user = request.form.get('login')
    senha_user = request.form.get('senha')

    if login_user == 'admin' and senha_user == '123':
        clientes = UsuarioDAO.listar_todos()
        return render_template('adminpage.html', usuarios=clientes, comidas=comidas, bebidas=bebidas)
    u = UsuarioDAO.buscar_por_login(login_user)
    if u:
        if senha_user == u.senha:
            session['usuario'] = login_user

            return render_template('paginaprincipal.html')
    else:
        return render_template('index.html')


    if login_user == 'admin' and senha_user == '123':
        clientes = UsuarioDAO.listar_todos()
        return render_template('adminpage.html', usuarios=clientes, bebidas=bebidas)
    u = UsuarioDAO.buscar_por_login(login_user)
    if u:
        if senha_user == u.senha:
            session['usuario'] = login_user

            return render_template('paginaprincipal.html')
    else:
        return render_template('index.html')

