import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'strongkey_secret'

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG = True

    MONGO_DATABASE_SECURITY_SERVER = os.environ.get('DEV_DATABASE_SERVER') or 'localhost'
    MONGO_DATABASE_SECURITY_PORT = os.environ.get('DEV_DATABASE_PORT') or 27017
    MONGO_DATABASE_SECURITY_NAME = os.environ.get('DEV_DATABASE_NAME') or 'DEV_BLANKSPIDER_SECURITY'

    MONGO_DATABASE_BLANKSPIDER_SERVER = os.environ.get('DEV_DATABASE_SERVER') or 'localhost'
    MONGO_DATABASE_BLANKSPIDER_PORT = os.environ.get('DEV_DATABASE_PORT') or 27017
    MONGO_DATABASE_BLANKSPIDER_NAME = os.environ.get('DEV_DATABASE_NAME') or 'DEV_BLANKSPIDER'

    MONGO_DATABASE_ARCHIVIED_SERVER = os.environ.get('DEV_DATABASE_SERVER') or 'localhost'
    MONGO_DATABASE_ARCHIVIED_PORT = os.environ.get('DEV_DATABASE_PORT') or 27017
    MONGO_DATABASE_ARCHIVIED_NAME = os.environ.get('DEV_DATABASE_NAME') or 'blankspider_content_database'
    #MONGO_DATABASE_ARCHIVIED_NAME = os.environ.get('DEV_DATABASE_NAME') or 'blankspider_content_tshirt'

class Production(Config):
    DEBUG = False
    MONGO_DATABASE_SERVER = os.environ.get('PROD_DATABASE_SERVER') or 'localhost'
    MONGO_DATABASE_PORT = os.environ.get('PROD_DATABASE_PORT') or 27017
    MONGO_DATABASE_NAME = os.environ.get('PROD_DATABASE_NAME') or 'DEV_BLANKSPIDER_ARCHIVIED'


config = {
    'development': Development,
    'production': Production,
    'default': Development
}

