from flask import Blueprint, render_template
from flask_security import login_required, current_user
from flask_security.decorators import roles_required, roles_accepted
from models import Product as Productos
# from . import db

user = Blueprint('user', __name__)


@user.route('/')
def index():
    return render_template('index.html')


@user.route('/profile')
@login_required
@roles_accepted('admin', 'user')
def profile():
    return render_template('profile.html', name=current_user.name)


@user.route('/listado')
@login_required
@roles_accepted('admin', 'user')
def productosAll():
    productos = Productos.query.all()
    ''' print(productos)
    for p in productos:
        print(p.name) '''
    return render_template('/user/listado.html', productos=productos, roles=current_user.roles[0].name)
    