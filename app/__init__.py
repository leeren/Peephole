from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

import os

import config

app = Flask(__name__)
db = SQLAlchemy(app)

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
app.config['DB_URI'] = 'sqlite:///' + os.path.join(envroot, 'app.db')

# Load stage configurations
app.config.from_object('config.%sConfig' % stage)

# Load private-defined configurations
app_config_dir = app.config.get('APPLICATION_CONFIG_DIR')
config_path = os.path.join(envroot, app_config_dir, 'config.py')
app.config.from_pyfile(config_path, silent=True)

from . import controllers
from . import models
from . import forms
