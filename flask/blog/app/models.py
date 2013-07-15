# -*- coding: utf-8 -*- 

from app import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def get_id(self):
        """Retorna o id do usuário em formato unicode. Caso não seja unicode, provavelmente SQLAlchemy retornará um erro."""
        return unicode(self.id)

    def is_authenticated(self):
        """Retorna se o usuário está autenticado."""
        return True

    def is_active(self):
        """Retorna True caso o usuário esteja ativo."""
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % self.content
