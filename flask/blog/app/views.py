# -*- coding: utf-8 -*- 

from app import app, db, lm, oid
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm, PostForm
from models import User, Post
from datetime import datetime

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user_by_id(id):
    return User.query.get(int(id))

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data,
                    timestamp = datetime.utcnow(),
                    author = g.user)
        db.session.add(post)
        db.session.commit()
        flash('Seu post foi inserido.')
        return redirect(url_for('index'))
    posts = Post.query.filter_by(user_id=g.user.id)
    return render_template('index.html',
            title='Home',
            form=form,
            posts=posts) 

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template("login.html",
            title = 'Entrar',
            form = form,
            providers = app.config['OPENID_LOGIN'])

@oid.after_login
def after_login(r):
    if r.email is None or r.email == "":
        flash('Login falhou.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = r.email).first()
    if user is None:
        username = r.username
        if username is None or username == "":
            username = r.email.split("@")[0]
        user = User(username = username, email = r.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if "remember_me" in session:
        remember_me = session["remember_me"]
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
