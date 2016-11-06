#!/usr/bin/env python
import sys 

from app import app

host = '127.0.0.1'
port = 8000

if len(sys.argv) > 1:
    host = sys.argv[1]
if len(sys.argv) > 2:
    port = int(sys.argv[2])

app.run(host=host, port=port, debug=True, use_reloader=False)
