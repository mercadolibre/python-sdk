import sys
import json
import requests
from bs4 import BeautifulSoup as bs
from lib.meli import Meli
from flask import Flask, request

'''
USUARIO TESTE
id: 475387306
nick: TESTJ2ZZC5VK
pass: qatest3435
mail:test_user_25270859@testuser.com

{"id":475400831,"nickname":"TESTYUGAYEKW","password":"qatest9282","site_status":"active","email":"test_user_59765277@testuser.com"
Novo access_token
https://api.mercadolibre.com/oauth/token?grant_type=refresh_token&client_id=APP_ID&client_secret=SECRET_KEY&refresh_token=REFRESH_TOKEN
'''

CLIENT_ID = '106413693'

APP_ID = '2359959178558309'

CLIENT_SECRET = '14kpjfE0ps677nifrb8xfdDTJtwbNu4C'

AUTH_URI = 'http://localhost:5000/authorize'

meli = Meli(client_id=APP_ID, client_secret=CLIENT_SECRET)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/authorize')
def authorize():
    meli.authorize(request.args.get('code'), AUTH_URI)
    ACCESS_TOKEN = meli.access_token
    return """<form class="" action="/post" method="get">
      <input type="text" name="anuncio" value="">
      <button type="submit" name="button">Postar anúncio</button>
    </form>"""

@app.route('/login')
def login():
    return "<a href='"+meli.auth_url(redirect_URI=AUTH_URI)+"'>Login</a>"


@app.route('/get')
def getItem():
    idCode = request.args.get('code').replace('-', '')
    res = meli.get(f'/items/{idCode}')
    data = json.loads(res.content)
    res = meli.get("/items/"+idCode, {'access_token':meli.access_token})
    return res.content

@app.route('/post')
def postItem():
    idCode = request.args.get('anuncio').replace('-', '')
    res = meli.get(f'/items/{idCode}')
    data = json.loads(res.content)
    temp = []
    for i in data['variations']:
        i['available_quantity'] = 1
        del i['catalog_product_id']
        temp.append(i)
    data['variations'] = temp
    j2 = {'title': data['title'], 'category_id': data['category_id'], 'price': data['price'], 'currency_id': data['currency_id'], 'available_quantity': data['available_quantity'], 'buying_mode': data['buying_mode'], 'listing_type_id': data['listing_type_id'], 'condition': data['condition'], 'description': data['descriptions'][0], 'video_id': data['video_id'], 'tags': data['tags'], 'warranty': data['warranty'], 'pictures': data['pictures'], 'variations': data['variations'], 'attributes': data['attributes'], 'accepts_mercadopago': data['accepts_mercadopago'], 'shipping': data['shipping'], 'sale_terms': data['sale_terms']}
    res = meli.post("/items", j2, {'access_token':meli.access_token})
    return res.content
