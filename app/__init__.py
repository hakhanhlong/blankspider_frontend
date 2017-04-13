from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager, current_user
from config import config
from flask_debugtoolbar import DebugToolbarExtension

from flask_moment import Moment

bootstrap = Bootstrap()
db = MongoEngine()
login_manager = LoginManager()






def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config[config_name])

    moment = Moment(app)

    '''app.config['MONGODB_SETTINGS'] = {
        'db': config[config_name].MONGO_DATABASE_NAME,
        'host': config[config_name].MONGO_DATABASE_SERVER,
        'port': config[config_name].MONGO_DATABASE_PORT

    }'''

    app.config['MONGODB_SETTINGS'] = [
        {
            'alias': 'default',
            'db': config[config_name].MONGO_DATABASE_SECURITY_NAME,
            'host': config[config_name].MONGO_DATABASE_SECURITY_SERVER,
            'port': config[config_name].MONGO_DATABASE_SECURITY_PORT
        },
        {
            'alias': config[config_name].MONGO_DATABASE_ARCHIVIED_NAME,
            'db': config[config_name].MONGO_DATABASE_ARCHIVIED_NAME,
            'host': config[config_name].MONGO_DATABASE_ARCHIVIED_SERVER,
            'port': config[config_name].MONGO_DATABASE_ARCHIVIED_PORT
        },
        {
            'alias': config[config_name].MONGO_DATABASE_BLANKSPIDER_NAME,
            'db': config[config_name].MONGO_DATABASE_BLANKSPIDER_NAME,
            'host': config[config_name].MONGO_DATABASE_BLANKSPIDER_SERVER,
            'port': config[config_name].MONGO_DATABASE_BLANKSPIDER_PORT
        }
    ]

    config[config_name].init_app(app)
    bootstrap.init_app(app)


    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    app.session_interface = MongoEngineSessionInterface(db)

    db.init_app(app)

    # Specify the debug panels you want
    app.config['DEBUG_TB_PANELS'] = [
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
        # Add the MongoDB panel
        #'flask.ext.mongoengine.panels.MongoDebugPanel',
    ]
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    toolbar = DebugToolbarExtension(app)

    ############### begin blueprint ############################
    from app.controllers.auth import auth as auth_blueprint
    from app.controllers.home import home as home_blueprint
    from app.controllers.source import source as source_blueprint
    from app.controllers.repository import repository as repository_blueprint
    from app.controllers.ajax import ajax as ajax_blueprint



    app.register_blueprint(home_blueprint, url_prefix='/')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(source_blueprint, url_prefix='/source')
    app.register_blueprint(repository_blueprint, url_prefix='/repository')
    app.register_blueprint(ajax_blueprint, url_prefix='/ajax')

    ############### end blueprint   ############################





    return app



