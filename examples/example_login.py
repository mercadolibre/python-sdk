 #!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, run, template, route, request
import json

from meli_client import meli


meli_obj = meli.Meli(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,site_id='MLA')

app = Bottle()

@app.route('/authorize')
def authorize():
    if request.query.get('code'):
        meli_obj.authorize(request.query.get('code'), REDIRECT_URI)
    return meli_obj.access_token

@app.route('/login')
def login():
    return "<a href='"+meli_obj.auth_url(redirect_URI=REDIRECT_URI)+"'>Login</a>"

run(app, host='localhost', port=4567, reloader=True)
