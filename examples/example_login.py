 #!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, run, template, route, request
import json

import sys
sys.path.append('../lib')
from meli import Meli

meli = Meli(client_id=CLIENT_ID,client_secret=CLIENT_SECRET)

app = Bottle()

@app.route('/authorize')
def authorize():
    if request.query.get('code'):
        meli.authorize(request.query.get('code'), REDIRECT_URI)
    return meli.access_token

@app.route('/login')
def login():
    return "<a href='"+meli.auth_url(redirect_URI=REDIRECT_URI)+"'>Login</a>"

run(app, host='localhost', port=4567, reloader=True)
