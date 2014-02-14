 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from bottle import Bottle, run, request

from meli import Meli

sys.path.append('../lib')

meli = Meli(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

app = Bottle()


@app.route('/authorize')
def authorize():
    if request.query.get('code'):
        meli.authorize(request.query.get('code'), REDIRECT_URI)
    return meli.access_token


@app.route('/login')
def login():
    return "<a href='{0}'>Login</a>".format(
        meli.auth_url(redirect_URI=REDIRECT_URI))

run(app, host='localhost', port=4567, reloader=True)
