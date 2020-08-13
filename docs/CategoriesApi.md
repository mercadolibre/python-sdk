# meli.CategoriesApi

All URIs are relative to *https://api.mercadolibre.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories_category_id_get**](CategoriesApi.md#categories_category_id_get) | **GET** /categories/{category_id} | Return by category.
[**sites_site_id_categories_get**](CategoriesApi.md#sites_site_id_categories_get) | **GET** /sites/{site_id}/categories | Return a categories by site.
[**sites_site_id_domain_discovery_search_get**](CategoriesApi.md#sites_site_id_domain_discovery_search_get) | **GET** /sites/{site_id}/domain_discovery/search | Predictor


# **categories_category_id_get**
> object categories_category_id_get(category_id)

Return by category.

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
    api_instance = meli.CategoriesApi(api_client)
    category_id = 'category_id_example' # str | 

    try:
        # Return by category.
        api_response = api_instance.categories_category_id_get(category_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->categories_category_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 

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

# **sites_site_id_categories_get**
> object sites_site_id_categories_get(site_id)

Return a categories by site.

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
    api_instance = meli.CategoriesApi(api_client)
    site_id = 'site_id_example' # str | 

    try:
        # Return a categories by site.
        api_response = api_instance.sites_site_id_categories_get(site_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->sites_site_id_categories_get: %s\n" % e)
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

# **sites_site_id_domain_discovery_search_get**
> object sites_site_id_domain_discovery_search_get(site_id, q, limit)

Predictor

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
    api_instance = meli.CategoriesApi(api_client)
    site_id = 'site_id_example' # str | 
q = 'q_example' # str | 
limit = 'limit_example' # str | 

    try:
        # Predictor
        api_response = api_instance.sites_site_id_domain_discovery_search_get(site_id, q, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CategoriesApi->sites_site_id_domain_discovery_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**|  | 
 **q** | **str**|  | 
 **limit** | **str**|  | 

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

