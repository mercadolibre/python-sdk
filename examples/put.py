from meli_client import meli


def main():
    meli_obj = Meli(client_id=CLIENT_ID,client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN,site_id='MLA')
    body = {"title":"oculos edicao especial!", "price":1000 }
    response = meli_obj.put("/items/ITEM_+ID", body, {'access_token':meli_obj.access_token})
    print response.content

if __name__ == "__main__":
    main()
