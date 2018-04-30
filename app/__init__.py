<<<<<<< HEAD
from flask import Flask
from config import Config
import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler
=======
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request
>>>>>>> 566fa6331c3bce3dd2083961b9c8ded3803312b2
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
<<<<<<< HEAD
=======
from flask_babel import Babel, lazy_gettext as _l
from config import Config
>>>>>>> 566fa6331c3bce3dd2083961b9c8ded3803312b2

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
<<<<<<< HEAD
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
=======
login.login_message = _l('Please log in to access this page.')
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)
>>>>>>> 566fa6331c3bce3dd2083961b9c8ded3803312b2

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
<<<<<<< HEAD
            fromaddr='no-reply@'+app.config['MAIL_SERVER'],
=======
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
>>>>>>> 566fa6331c3bce3dd2083961b9c8ded3803312b2
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
<<<<<<< HEAD
        backupCount=10)
=======
                                       backupCount=10)
>>>>>>> 566fa6331c3bce3dd2083961b9c8ded3803312b2
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

<<<<<<< HEAD
=======

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


>>>>>>> 566fa6331c3bce3dd2083961b9c8ded3803312b2
from app import routes, models, errors
