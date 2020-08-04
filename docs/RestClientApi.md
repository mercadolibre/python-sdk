# meli.RestClientApi

All URIs are relative to *https://api.mercadolibre.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_get**](RestClientApi.md#resource_get) | **GET** /{resource} | Resource path GET
[**resource_post**](RestClientApi.md#resource_post) | **POST** /{resource} | Resourse path POST
[**resource_put**](RestClientApi.md#resource_put) | **PUT** /{resource} | Resourse path PUT


# **resource_get**
> resource_get(resource, access_token)

Resource path GET

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
    api_instance = meli.RestClientApi(api_client)
    resource = 'resource_example' # str | 
access_token = 'access_token_example' # str | 

    try:
        # Resource path GET
        api_instance.resource_get(resource, access_token)
    except ApiException as e:
        print("Exception when calling RestClientApi->resource_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **access_token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_post**
> resource_post(resource, access_token, body)

Resourse path POST

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
    api_instance = meli.RestClientApi(api_client)
    resource = 'resource_example' # str | 
access_token = 'access_token_example' # str | 
body = None # object | 

    try:
        # Resourse path POST
        api_instance.resource_post(resource, access_token, body)
    except ApiException as e:
        print("Exception when calling RestClientApi->resource_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **access_token** | **str**|  | 
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_put**
> resource_put(resource, access_token, body)

Resourse path PUT

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
    api_instance = meli.RestClientApi(api_client)
    resource = 'resource_example' # str | 
access_token = 'access_token_example' # str | 
body = None # object | 

    try:
        # Resourse path PUT
        api_instance.resource_put(resource, access_token, body)
    except ApiException as e:
        print("Exception when calling RestClientApi->resource_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **access_token** | **str**|  | 
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

