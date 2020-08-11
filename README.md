
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
from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)


# Enter a context with an instance of the API client
with meli.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meli.ItemsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Return a Item.
        api_instance.items_id_get(id)
    except ApiException as e:
        print("Exception when calling ItemsApi->items_id_get: %s\n" % e)
```

## Documentation & Important notes

##### The URIs are relative to https://api.mercadolibre.com

##### The Authorization URLs:
###### Remember set your correct country ID
###### https://auth.mercadolibre.{country_domain}

#####  All docs for the library are located [here](https://github.com/mercadolibre/python-sdk/tree/master/docs)

#####  Check out our examples codes in the folder [examples](https://github.com/mercadolibre/python-sdk/tree/master/examples)

##### Don’t forget to check out our [developer site](https://developers.mercadolibre.com/)
