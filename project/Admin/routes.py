import os
import forms
from flask import Blueprint, render_template, request, redirect, url_for
#from werkzeug.utils import secure_filename
from flask_security import current_user
from flask_security.decorators import roles_accepted
from models import Product as Productos, db
from logger import Logger

admin = Blueprint('admin', __name__)
log = Logger('admin')


@admin.route("/modificar", methods=['GET','POST'])
@roles_accepted('admin')
def modificar():
    form = forms.ProductForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        producto = Productos.query.get(id)
        form.id.data = producto.id
        form.name.data = producto.name
        form.price.data = producto.price
        form.stock.data = producto.stock
        form.description.data = producto.description
        form.image.data = producto.image
    if request.method == 'POST':
        id = form.id.data
        producto = db.session.query(Productos).filter(Productos.id == id).first()
        producto.name = form.name.data
        producto.price = form.price.data
        producto.stock = form.stock.data
        producto.description = form.description.data
        producto.image = form.image.data
        db.session.add(producto)
        db.session.commit()
        log.debug('Producto {} modificado por {}'.format(id, current_user.email))
        return redirect(url_for('user.productosAll'))
    return render_template('admin/modificar.html', form=form)
    
    


@admin.route('/eliminar', methods=['GET','POST'])
@roles_accepted('admin')
def eliminar():
    id = request.args.get('id')
    producto = Productos.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    log.debug('Producto {} eliminado por {}'.format(id, current_user.email))
    return redirect(url_for('user.productosAll'))


@admin.route('/agregar', methods=['GET','POST'])
@roles_accepted('admin')
def agregar():
    form = forms.ProductForm(request.form)
    if request.method == 'POST' and form.validate():
        product = Productos(name=form.name.data, 
                            price=form.price.data, 
                            stock=form.stock.data, 
                            description=form.description.data, 
                            image=form.image.data)
        db.session.add(product)
        db.session.commit()
        log.debug('Producto {} agregado por {}'.format(product.id, current_user.email))
        return redirect(url_for('user.productosAll'))
    return render_template('admin/agregar.html', form=form)    