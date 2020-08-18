# You need use this example code in to the main folder
from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint
# Defining the host, defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)


# Enter a context with an instance of the API client
with meli.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meli.RestClientApi(api_client)
    resource = 'items' # A resource like items, search, category etc
    access_token = 'access_token_example' # Your access token

    # A body example to post a item in Argentina
    body = {
      "title": "Item de test - No Ofertar",
      "category_id": "MLA5991",
      "price": "350",
      "currency_id": "ARS",
      "available_quantity": "12",
      "buying_mode": "buy_it_now",
      "listing_type_id": "bronze",
      "condition": "new",
      "description": "Item de Teste. Mercado Livre SDK",
      "video_id": "RXWn6kftTHY",
      "pictures": [
        {
          "source": "https://http2.mlstatic.com/storage/developers-site-cms-admin/openapi/319968615067-mp3.jpg"
        }
      ],
      "attributes": [
        {
          "id": "DATA_STORAGE_CAPACITY",
          "name": "Capacidad de almacenamiento de datos",
          "value_id": "null",
          "value_name": "8 GB",
          "value_struct": {
            "number": 8,
            "unit": "GB"
          },
          "values": [
            {
              "id": "null",
              "name": "8 GB",
              "struct": {
                "number": 8,
                "unit": "GB"
              }
            }
          ],
          "attribute_group_id": "OTHERS",
          "attribute_group_name": "Otros"
        }
      ],
      "variations": [
        {
          "price": 350,
          "attribute_combinations": [
            {
              "name": "Color",
              "value_id": "283165",
              "value_name": "Gris"
            }
          ],
          "available_quantity": 2,
          "sold_quantity": 0,
          "picture_ids": [
            "882629-MLA40983876214_032020"
          ]
        }
      ]
    }

    try:
        # Resourse path POST
        api_response = api_instance.resource_post(resource, access_token, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RestClientApi->resource_post: %s\n" % e)