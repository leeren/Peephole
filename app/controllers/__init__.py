from app import app

import importlib
import os

modules_dir = os.path.dirname(os.path.abspath(__file__))
for name in os.listdir(modules_dir):
    if (name.endswith('.py') and '__init__' not in name):
        base = os.path.splitext(name)[0]
        module = importlib.import_module('app.controllers.%s' % base) 
        if hasattr(module, 'mod'):
            app.register_blueprint(module.mod)
