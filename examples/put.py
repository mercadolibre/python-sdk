import sys
sys.path.append('../lib')
from meli import Meli

def main():
    meli = Meli(client_id=CLIENT_ID,client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
    body = {"title":"oculos edicao especial!", "price":1000 }
    response = meli.put("/items/ITEM_+ID", body, {'access_token':meli.access_token})
    print response.content

if __name__ == "__main__":
    main()
