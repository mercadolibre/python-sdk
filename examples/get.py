from meli_client import meli


def main():
    meli_obj = meli.Meli(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN,
                         refresh_token=REFRESH_TOKEN, site_id='MLA')

    response = meli_obj.get("/items/ITEM_ID")
    print response.content


if __name__ == "__main__":
    main()
