# main.py
from flask import Blueprint, render_template
from flask_security import login_required, current_user
from flask_security.decorators import roles_required, roles_accepted
from models import Product as Productos
# from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
@roles_accepted('admin', 'user')
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/listado')
@login_required
@roles_accepted('admin', 'user')
def ProductosAll():
    productos = Productos.query.all()
    ''' print(productos)
    for p in productos:
        print(p.name) '''
    return render_template('listado.html', productos=productos, roles=current_user.roles[0].name)
    