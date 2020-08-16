# meli.OAuth20Api

All URIs are relative to *https://api.mercadolibre.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth**](OAuth20Api.md#auth) | **GET** /authorization | Authentication Endpoint
[**get_token**](OAuth20Api.md#get_token) | **POST** /oauth/token | Request Access Token


# **auth**
> auth(response_type, client_id, redirect_uri)

Authentication Endpoint

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
    api_instance = meli.OAuth20Api(api_client)
    response_type = 'code' # str |  (default to 'code')
client_id = 'client_id_example' # str | 
redirect_uri = 'redirect_uri_example' # str | 

    try:
        # Authentication Endpoint
        api_instance.auth(response_type, client_id, redirect_uri)
    except ApiException as e:
        print("Exception when calling OAuth20Api->auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | **str**|  | [default to &#39;code&#39;]
 **client_id** | **str**|  | 
 **redirect_uri** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> object get_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)

Request Access Token

Partner makes a request to the token endpoint by adding the following parameters described below

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
    api_instance = meli.OAuth20Api(api_client)
    grant_type = 'grant_type_example' # str |  (optional)
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)
redirect_uri = 'redirect_uri_example' # str |  (optional)
code = 'code_example' # str |  (optional)
refresh_token = 'refresh_token_example' # str |  (optional)

    try:
        # Request Access Token
        api_response = api_instance.get_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OAuth20Api->get_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 
 **redirect_uri** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **refresh_token** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A User object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

