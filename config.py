import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'shh ssh rt tthh jjj kkkk'


class DevConfig(Config):
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = None
    MYSQL_DATABASE_PASSWORD = None
    MYSQL_DATABASE_DB= 'mepot-dev-db'
    MYSQL_DATABASE_CHARSET='utf-8'

    DEBUG = True

class ProdConfig(Config):
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = None
    MYSQL_DATABASE_PASSWORD = None
    MYSQL_DATABASE_DB= 'mepot-prod-db'
    MYSQL_DATABASE_CHARSET='utf-8'

    DEBUG = False