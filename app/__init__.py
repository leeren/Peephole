from flask import Flask

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

# Load stage configurations
app.config.from_object('config.%sConfig' % stage)

# Load private-defined configurations
app_config_dir = app.config.get('APPLICATION_CONFIG_DIR')
config_path = os.path.join(envroot, app_config_dir, 'config.py')
app.config.from_pyfile(config_path, silent=True)

# END OF PROJECT CONFIGURATION

from . import controllers
from . import forms
