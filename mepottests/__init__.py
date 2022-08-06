from flask_testing import TestCase
from application import create_app, db
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    WTF_CSRF_ENABLED=False
    DEBUG = True


class TestBase(TestCase):

    def create_app(self):
        app = create_app()
        app.config.update(TestConfig().SQLALCHEMY_DATABASE_URI)
        return app


    def setUp(self):
        sel.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

