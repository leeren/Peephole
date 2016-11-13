from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_oauthlib.client import OAuth
from flask_login import LoginManager

import os
import config

app = Flask(__name__)

# START OF PROJECT CONFIGURATION

# Project stage (Default/Dev/Prod/Stage)
stage = os.environ.get('ENVIRONMENT_STAGE', 'Default')
# Project root directory 
envroot = os.environ.get('ENVIRONMENT_ROOT', os.path.abspath(os.curdir))

# Load default configurations
app.config.from_object('config.DefaultConfig')
app.config['ENVIRONMENT_STAGE'] = stage
app.config['ENVIRONMENT_ROOT'] = envroot

# Load DB configurations
app.config['MIGRATION_DIR'] = os.path.join(envroot, 'migrations/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(envroot, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
print app.config['SQLALCHEMY_DATABASE_URI']

# Load stage configurations
app.config.from_object('config.%sConfig' % stage)

# Load private-defined configurations
app_config_dir = app.config.get('APPLICATION_CONFIG_DIR')
config_path = os.path.join(envroot, app_config_dir, 'config.py')
app.config.from_pyfile(config_path, silent=True)

lm = LoginManager()
lm.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
oauth = OAuth(app)

facebook = oauth.remote_app(
        'facebook',
        consumer_key=app.config.get('FACEBOOK_APP_ID'),
        consumer_secret=app.config.get('FACEBOOK_APP_SECRET'),
        request_token_params={'scope': 'email'},
        base_url='https://graph.facebook.com',
        request_token_url=None,
        access_token_url='/oauth/access_token',
        access_token_method='GET',
        authorize_url='https://www.facebook.com/dialog/oauth'
        )

from . import controllers
from . import models
from . import forms
