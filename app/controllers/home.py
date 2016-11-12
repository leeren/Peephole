from flask import Blueprint, render_template, flash, redirect
from app.forms import LoginForm

mod=Blueprint('home', __name__)

@mod.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    user = {'name':'Leeren'}
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
    return render_template('login.html', form=form, user=user)

@mod.errorhandler(403)
def page_not_found(e):
    return render_template('error.html', message="Restricted access", error=e)

@mod.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message="Page not found", error=e)
