import os


class Config(object):
    SECRET_KEY = os.urandom(24)
    SESSION_COOKIE_SECURE = False
    SECURITY_PASSWORD_SALT = 'thisissecretsalt'
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    UPLOAD_FOLDER = 'static/img'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@127.0.0.1/examenseguridad"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


