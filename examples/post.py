import sys
sys.path.append('../lib')
from meli import Meli

def main():
    meli = Meli(client_id=CLIENT_ID,client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)
    body = {"condition":"new", "warranty":"60 dias", "currency_id":"BRL", "accepts_mercadopago":True, "description":"Lindo Ray_Ban_Original_Wayfarer", "listing_type_id":"bronze", "title":"oculos Ray Ban Aviador  Que Troca As Lentes  Lancamento!", "available_quantity":64, "price":289, "subtitle":"Acompanha 3 Pares De Lentes!! Compra 100% Segura", "buying_mode":"buy_it_now", "category_id":"MLB5125", "pictures":[{"source":"http://upload.wikimedia.org/wikipedia/commons/f/fd/Ray_Ban_Original_Wayfarer.jpg"}, {"source":"http://en.wikipedia.org/wiki/File:Teashades.gif"}] }
    response = meli.post("/items", body, {'access_token':meli.access_token})
    print response.content

if __name__ == "__main__":
    main()
