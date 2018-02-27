# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess-dis-password'

OPENID_PROVIDERS = [
	{'name': 'Google', 'url': 'https://www.google.com/accounts/08/id'},
	{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
	{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
	{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

# email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = '<email>'
MAIL_PASSWORD = '<password>'

# administrator list
ADMINS = ['<email>']

# pagination
POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

#available languages
LANGUAGES = {
	'en': 'English',
	'es': 'Español'
}
