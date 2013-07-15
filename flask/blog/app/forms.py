from flask.ext.wtf import Form, TextField, BooleanField, Required

class LoginForm(Form):

    openid = TextField('openid', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)

class PostForm(Form):

    content = TextField('content', validators=[Required()])
