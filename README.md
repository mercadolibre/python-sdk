![No longer maintained](https://img.shields.io/badge/Maintenance-OFF-red.svg)

### [DEPRECATED] This repository is no longer maintained

> From the first week of April 2021 we will stop maintaining our SDKs.
>
> This project is not functional, the dependencies will not be updated to latest ones.
>
> We recommend you read our [documentation](https://developers.mercadolibre.com).

  <a href="https://developers.mercadolibre.com">
    <img src="https://user-images.githubusercontent.com/1153516/73021269-043c2d80-3e06-11ea-8d0e-6e91441c2900.png" alt="Mercado Libre Developers" width="200"></a>
  </a>

---

<br>
<h1 align="center">
  <a href="https://developers.mercadolibre.com">
    <img src="https://user-images.githubusercontent.com/1153516/29861072-689ec57e-8d3e-11e7-8368-dd923543258f.jpg" alt="Mercado Libre Developers" width="230"></a>
  </a>
  <br><br>
  MercadoLibre's Python SDK
  <br>
</h1>

<h4 align="center">This is the official Python SDK for MercadoLibre's Platform.</h4>

## Requirements.

Python 2.7 and 3.4+

## Installation

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/mercadolibre/python-sdk.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/mercadolibre/python-sdk.git`)

Then import the package:

```python
import meli
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import meli
```

## Usage

```python
# Auth URLs Options by country

# 1:  "https://auth.mercadolibre.com.ar"
# 2:  "https://auth.mercadolivre.com.br"
# 3:  "https://auth.mercadolibre.com.co"
# 4:  "https://auth.mercadolibre.com.mx"
# 5:  "https://auth.mercadolibre.com.uy"
# 6:  "https://auth.mercadolibre.cl"
# 7:  "https://auth.mercadolibre.com.cr"
# 8:  "https://auth.mercadolibre.com.ec"
# 9:  "https://auth.mercadolibre.com.ve"
# 10: "https://auth.mercadolibre.com.pa"
# 11: "https://auth.mercadolibre.com.pe"
# 12: "https://auth.mercadolibre.com.do"
# 13: "https://auth.mercadolibre.com.bo"
# 14: "https://auth.mercadolibre.com.py"

# For example in your app, you can make some like this to get de auth
import urllib

params = urllib.urlencode({'response_type':'code', 'client_id':'your_client_id', 'redirect_uri':'your_redirect_uri'})
f = urllib.urlopen("https://auth.mercadolibre.com.ar/authorization?%s" % params)
print f.geturl()
```

his will give you the url to redirect the user. You need to specify a callback url which will be the one that the user will redirected after a successfull authrization process.

Once the user is redirected to your callback url, you'll receive in the query string, a parameter named code. You'll need this for the second part of the process

## Examples for OAuth - get token

```python
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
    api_instance = meli.OAuth20Api(api_client)
    grant_type = 'authorization_code' # str
    client_id = 'client_id_example' # Your client_id
    client_secret = 'client_secret_example' # Your client_secret
    redirect_uri = 'redirect_uri_example' # Your redirect_uri
    code = 'code_example' # The parameter CODE
    refresh_token = 'refresh_token_example' # Your refresh_token

try:
    # Request Access Token
    api_response = api_instance.get_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OAuth20Api->get_token: %s\n" % e)
```

## Example using the RestClient with a POST Item

```python
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
    resource = 'resource_example' # A resource like items, search, etc
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
```

## Documentation & Important notes

##### The URIs are relative to https://api.mercadolibre.com

##### The Authorization URLs (set the correct country domain): https://auth.mercadolibre.{country_domain}

##### All docs for the library are located [here](https://github.com/mercadolibre/python-sdk/tree/master/docs)

##### Check out our examples codes in the folder [examples](https://github.com/mercadolibre/python-sdk/tree/master/examples)

##### Don’t forget to check out our [developer site](https://developers.mercadolibre.com/)
