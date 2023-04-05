# auth.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import login_required, SQLAlchemyUserDatastore, Security, current_user
from flask_security.utils import login_user,logout_user
from models import User, db, Role
from logger import Logger
#from app import userDataStore

auth = Blueprint('auth', __name__, url_prefix='/security')
userDataStore = SQLAlchemyUserDatastore(db, User, Role)
log = Logger('auth')

@auth.route('/login')
def login():
    return render_template('security/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        log.error('Usuario {} no encontrado'.format(email))
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    log.debug('Usuario {} logueado'.format(current_user.email))
    return redirect(url_for('user.profile'))


@auth.route('/register')
def register():
    return render_template('security/register.html')


@auth.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(
        email=email).first()

    if user:
        log.error('Usuario {} ya existente {}'.format(email))
        return redirect(url_for('auth.register'))

    userDataStore.create_user(name=name,email=email,password=generate_password_hash(password, method='sha256'))
    db.session.commit()
    log.debug('Usuario {} registrado'.format(email))

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    log.debug('Usuario {} logout'.format(current_user.email))
    logout_user()
    return redirect(url_for('user.index'))
