import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

CSRF_ENABLED = True
SECRET_KEY = 'e-la-vamos-nos'

OPENID_LOGIN = [
        { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
        { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
        { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
        { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
        { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com'} ]
