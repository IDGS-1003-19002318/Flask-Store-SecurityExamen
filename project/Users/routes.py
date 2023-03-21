from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import login_required, SQLAlchemyUserDatastore, Security, current_user
from flask_security.utils import login_user,logout_user#, hash_password, encrypt_password
from models import Product, db, Role, User


admin = Blueprint('auth', __name__#, url_prefix='/admin'
                  )
userDataStore = SQLAlchemyUserDatastore(db, User, Role)


@admin.route("/dashboard")
def dashboard():
    return render_template('listado.html')


@admin.route("/modificar")
def modificar():
    pass


@admin.route('/eliminar')
def eliminar():
    pass