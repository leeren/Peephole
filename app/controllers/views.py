from flask import Blueprint, render_template, flash, redirect
from app.forms import LoginForm
from app import lm
from flask_oauthlib.client import OAuthException
from flask_login import current_user, login_user, logout_user, login_required

mod=Blueprint('home', __name__)

@lm.user_loader(user_id):
    return User.query.get(int(user_id))

@app.before_request
def get_user():
    g.user = current_user

@mod.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if g.user.is_authenticated:
        return render_template('tmp.html')
    return render_template('login.html')

@mod.route('/define-self', methods=['GET'])
def define_self():
	return render_template('define-self.html')

@mod.errorhandler(403)
def page_not_found(e):
    return render_template('error.html', message="Restricted access", error=e)

@mod.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message="Page not found", error=e)

