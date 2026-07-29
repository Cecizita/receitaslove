from flask import *
from config import db
from blueprints.bp_admin import admin
from blueprints.bp_usuario import usuario
from config import comidas
from config import bebidas


app = Flask(__name__)
app.secret_key = 'KJ#H4k3jh412dasd'


app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(usuario, url_prefix='/usuario')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mostrarcomidas')
def mostrar_comidas():
    return render_template('compras.html',lista = comidas)

@app.route('/usuario/encomendarcomida' , methods=['POST', 'GET'])
def comprar_comida():
    if request.method == 'GET':
        return render_template('compras.html', comidas=comidas)
    else:
        nome_comida = request.form.getlist('comida')
        print(nome_comida)

        return render_template('paginaprincipal.html')


@app.route('/usuario/encomendarbebida' , methods=['POST', 'GET'])
def comprar_bebida():
    if request.method == 'GET':
        return render_template('comprasbebidas.html', bebidas=bebidas)
    else:
        nome_bebida = request.form.getlist('bebida')
        print(nome_bebida)

        return render_template('paginaprincipal.html')


@app.route('/usuario/logout')
def logout():
    session.clear()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)