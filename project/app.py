# init.py
from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_wtf.csrf import CSRFProtect
from Auth.routes import auth as auth_blueprint
from Admin.routes import admin as admin_blueprint
from Users.routes import user as main_blueprint
from models import db, User, Role
from config import DevelopmentConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()
userDataStore = SQLAlchemyUserDatastore(db, User, Role)


app.register_blueprint(auth_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(main_blueprint)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    Security(app, userDataStore)

    app.run(port=3000)
