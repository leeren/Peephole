#!/usr/bin/env python
import sys 

from app import app

host = '127.0.0.1'
port = 8000

app.run(host=host, port=port, debug=True, use_reloader=False)
