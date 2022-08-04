import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'shh ssh rt tthh jjj kkkk'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or "sqlite:///mepot.db"


# class DevConfig(Config):
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'shh ssh rt tthh jjj kkkk'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:12345@localhost:3306/product-dev-db"
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'shh ssh rt tthh jjj kkkk'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     DEBUG = True

# class ProdConfig(Config):
#     MYSQL_DATABASE_HOST s= 'localhost'
#     MYSQL_DATABASE_PORT = '3306'
#     MYSQL_DATABASE_USER = 'olayodech'
#     MYSQL_DATABASE_PASSWORD = 12345
#     MYSQL_DATABASE_DB= 'mepot-prod-db'
#     MYSQL_DATABASE_CHARSET='utf-8'
#     # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:12345@localhost:3306/product-prod-db"
#     # "mysql://${MYSQL_DATABASE_USER}:${MYSQL_DATABASE_PASSWORD}@${MYSQL_DATABASE_HOST}:${MYSQL_DATABASE_PORT}/${MYSQL_DATABASE_DB}"
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'shh ssh rt tthh jjj kkkk'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

#     DEBUG = False