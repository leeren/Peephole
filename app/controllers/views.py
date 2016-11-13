from flask import Blueprint, render_template, flash, redirect, session, request, url_for, g
from app import app, lm, facebook, db
from app.models import User
from flask_oauthlib.client import OAuthException
from flask_login import current_user, login_user, logout_user, login_required

mod=Blueprint('home', __name__)

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def get_user():
    g.user = current_user

@mod.route('/', methods=['GET', 'POST'])
def index():
    if g.user.is_authenticated:
        return render_template('define-self.html')
    return render_template('login.html')

@mod.route('/login', methods=['GET', 'POST'])
def login():
    callback = url_for(
            'authorize_facebook',
            _external=True
            )
    return facebook.authorize(callback=callback)

@app.route('/login/authorize')
def authorize_facebook():
    resp = facebook.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error%s' % (
                request.args['error_reason'],
                request.args['error_description']
                )
    if isinstance(resp, OAuthException):
        return 'Acess denied: %s' % resp.message
    session['oauth_token'] = (resp['access_token'], '')
    fb_user = facebook.get('/me/?fields=email,name,id,picture')
    return set_user(fb_user)

def set_user(fb_user):
    user = User.query.filter_by(facebook_id = fb_user.data['id']).first()
    if user is None:
        create_user(fb_user)
        return render_template('define-self.html')
    login_user(user, remember=True)
    return render_template('define-self.html')
    
def create_user(fb_user):
    new_user = User(
        facebook_id = fb_user.data['id'],
        pic_url = fb_user.data['picture']['data']['url'],
        name = fb_user.data['name'],
        email = fb_user.data['email']
    )
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user, remember=True)
    return new_user

@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

@mod.errorhandler(403)
def page_not_found(e):
    return render_template('error.html', message="Restricted access", error=e)

@mod.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message="Page not found", error=e)

