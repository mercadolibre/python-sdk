# mercadolibre_python_sdk
This is a the codebase to generate a SDK for Open Platform Marketplace

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

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

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
with meli.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = meli.CategoriesApi(api_client)
    category_id = 'category_id_example' # str | 

    try:
        # Return by category.
        api_instance.categories_category_id_get(category_id)
    except ApiException as e:
        print("Exception when calling CategoriesApi->categories_category_id_get: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.mercadolibre.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CategoriesApi* | [**categories_category_id_get**](docs/CategoriesApi.md#categories_category_id_get) | **GET** /categories/{category_id} | Return by category.
*CategoriesApi* | [**sites_site_id_categories_get**](docs/CategoriesApi.md#sites_site_id_categories_get) | **GET** /sites/{site_id}/categories | Return a categories by site.
*CategoriesApi* | [**sites_site_id_domain_discovery_search_get**](docs/CategoriesApi.md#sites_site_id_domain_discovery_search_get) | **GET** /sites/{site_id}/domain_discovery/search | Predictor
*ItemsApi* | [**items_id_get**](docs/ItemsApi.md#items_id_get) | **GET** /items/{id} | Return a Item.
*ItemsApi* | [**items_id_put**](docs/ItemsApi.md#items_id_put) | **PUT** /items/{id} | Update a Item.
*ItemsApi* | [**items_post**](docs/ItemsApi.md#items_post) | **POST** /items | Create a Item.
*ItemsHealthApi* | [**items_id_health_actions_get**](docs/ItemsHealthApi.md#items_id_health_actions_get) | **GET** /items/{id}/health/actions | Return item health actions by id.
*ItemsHealthApi* | [**items_id_health_get**](docs/ItemsHealthApi.md#items_id_health_get) | **GET** /items/{id}/health | Return health by id.
*ItemsHealthApi* | [**sites_site_id_health_levels_get**](docs/ItemsHealthApi.md#sites_site_id_health_levels_get) | **GET** /sites/{site_id}/health_levels | Return health levels.
*OAuth20Api* | [**auth**](docs/OAuth20Api.md#auth) | **GET** /authorization | Authentication Endpoint
*OAuth20Api* | [**get_token**](docs/OAuth20Api.md#get_token) | **POST** /oauth/token | Request Access Token
*RestClientApi* | [**resource_delete**](docs/RestClientApi.md#resource_delete) | **DELETE** /{resource} | Resource path DELETE
*RestClientApi* | [**resource_get**](docs/RestClientApi.md#resource_get) | **GET** /{resource} | Resource path GET
*RestClientApi* | [**resource_post**](docs/RestClientApi.md#resource_post) | **POST** /{resource} | Resourse path POST
*RestClientApi* | [**resource_put**](docs/RestClientApi.md#resource_put) | **PUT** /{resource} | Resourse path PUT


## Documentation For Models

 - [Attributes](docs/Attributes.md)
 - [AttributesValueStruct](docs/AttributesValueStruct.md)
 - [AttributesValues](docs/AttributesValues.md)
 - [InlineObject](docs/InlineObject.md)
 - [Item](docs/Item.md)
 - [ItemPictures](docs/ItemPictures.md)
 - [Variations](docs/Variations.md)
 - [VariationsAttributeCombinations](docs/VariationsAttributeCombinations.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author



