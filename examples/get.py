# -*- coding: UTF-8 -*-

import sys

from meli import Meli

sys.path.append('../lib')


def main():
    meli = Meli(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        access_token=ACCESS_TOKEN,
        refresh_token=REFRESH_TOKEN
    )
    response = meli.get("/items/ITEM_ID")
    print response.content

if __name__ == "__main__":
    main()
