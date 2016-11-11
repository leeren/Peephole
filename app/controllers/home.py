from flask import Blueprint, render_template

mod=Blueprint('home', __name__)

@mod.route('/')
def index():
    user = {'name':'Leeren'}
    print 'hey'
    return render_template('index.html', user=user)

@mod.errorhandler(403)
def page_not_found(e):
    return render_template('error.html', message="Restricted access", error=e)

@mod.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message="Page not found", error=e)
