# meli.ItemsHealthApi

All URIs are relative to *https://api.mercadolibre.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**items_id_health_actions_get**](ItemsHealthApi.md#items_id_health_actions_get) | **GET** /items/{id}/health/actions | Return item health actions by id.
[**items_id_health_get**](ItemsHealthApi.md#items_id_health_get) | **GET** /items/{id}/health | Return health by id.
[**sites_site_id_health_levels_get**](ItemsHealthApi.md#sites_site_id_health_levels_get) | **GET** /sites/{site_id}/health_levels | Return health levels.


# **items_id_health_actions_get**
> object items_id_health_actions_get(id, access_token)

Return item health actions by id.

### Example

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
    api_instance = meli.ItemsHealthApi(api_client)
    id = 'id_example' # str | 
access_token = 'access_token_example' # str | 

    try:
        # Return item health actions by id.
        api_response = api_instance.items_id_health_actions_get(id, access_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ItemsHealthApi->items_id_health_actions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **access_token** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **items_id_health_get**
> object items_id_health_get(id, access_token)

Return health by id.

### Example

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
    api_instance = meli.ItemsHealthApi(api_client)
    id = 'id_example' # str | 
access_token = 'access_token_example' # str | 

    try:
        # Return health by id.
        api_response = api_instance.items_id_health_get(id, access_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ItemsHealthApi->items_id_health_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **access_token** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_health_levels_get**
> object sites_site_id_health_levels_get(site_id)

Return health levels.

### Example

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
    api_instance = meli.ItemsHealthApi(api_client)
    site_id = 'site_id_example' # str | 

    try:
        # Return health levels.
        api_response = api_instance.sites_site_id_health_levels_get(site_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ItemsHealthApi->sites_site_id_health_levels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

