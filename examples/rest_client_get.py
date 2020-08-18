# You need use this example code in to the main folder
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
    api_instance = meli.RestClientApi(api_client)
    resource = 'sites/MLA/categories' # A resource example like items, search, category, etc.
    access_token = 'access_token_example' # Your access token.

try:
    # Resource path GET
    api_response = api_instance.resource_get(resource, access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestClientApi->resource_get: %s\n" % e)