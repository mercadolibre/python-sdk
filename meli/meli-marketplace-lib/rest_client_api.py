# coding: utf-8

"""
    MELI Markeplace SDK

    This is a the codebase to generate a SDK for Open Platform Marketplace  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from meli.api_client import ApiClient
from meli.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RestClientApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resource_get(self, resource, access_token, **kwargs):  # noqa: E501
        """Resource path GET  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resource_get(resource, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str resource: (required)
        :param str access_token: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.resource_get_with_http_info(resource, access_token, **kwargs)  # noqa: E501

    def resource_get_with_http_info(self, resource, access_token, **kwargs):  # noqa: E501
        """Resource path GET  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resource_get_with_http_info(resource, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str resource: (required)
        :param str access_token: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'resource',
            'access_token'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'resource' is set
        if self.api_client.client_side_validation and ('resource' not in local_var_params or  # noqa: E501
                                                        local_var_params['resource'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `resource` when calling `resource_get`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if self.api_client.client_side_validation and ('access_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['access_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `access_token` when calling `resource_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'resource' in local_var_params and local_var_params['resource'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `resource` when calling `resource_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'access_token' in local_var_params and local_var_params['access_token'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `access_token` when calling `resource_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'resource' in local_var_params:
            path_params['resource'] = local_var_params['resource']  # noqa: E501

        query_params = []
        if 'access_token' in local_var_params and local_var_params['access_token'] is not None:  # noqa: E501
            query_params.append(('access_token', local_var_params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{resource}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_post(self, resource, access_token, body, **kwargs):  # noqa: E501
        """Resourse path POST  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resource_post(resource, access_token, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str resource: (required)
        :param str access_token: (required)
        :param object body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.resource_post_with_http_info(resource, access_token, body, **kwargs)  # noqa: E501

    def resource_post_with_http_info(self, resource, access_token, body, **kwargs):  # noqa: E501
        """Resourse path POST  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resource_post_with_http_info(resource, access_token, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str resource: (required)
        :param str access_token: (required)
        :param object body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'resource',
            'access_token',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'resource' is set
        if self.api_client.client_side_validation and ('resource' not in local_var_params or  # noqa: E501
                                                        local_var_params['resource'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `resource` when calling `resource_post`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if self.api_client.client_side_validation and ('access_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['access_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `access_token` when calling `resource_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in local_var_params or  # noqa: E501
                                                        local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `resource_post`")  # noqa: E501

        if self.api_client.client_side_validation and 'resource' in local_var_params and local_var_params['resource'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `resource` when calling `resource_post`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'access_token' in local_var_params and local_var_params['access_token'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `access_token` when calling `resource_post`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'resource' in local_var_params:
            path_params['resource'] = local_var_params['resource']  # noqa: E501

        query_params = []
        if 'access_token' in local_var_params and local_var_params['access_token'] is not None:  # noqa: E501
            query_params.append(('access_token', local_var_params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{resource}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_put(self, resource, access_token, body, **kwargs):  # noqa: E501
        """Resourse path PUT  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resource_put(resource, access_token, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str resource: (required)
        :param str access_token: (required)
        :param object body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.resource_put_with_http_info(resource, access_token, body, **kwargs)  # noqa: E501

    def resource_put_with_http_info(self, resource, access_token, body, **kwargs):  # noqa: E501
        """Resourse path PUT  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resource_put_with_http_info(resource, access_token, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str resource: (required)
        :param str access_token: (required)
        :param object body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'resource',
            'access_token',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'resource' is set
        if self.api_client.client_side_validation and ('resource' not in local_var_params or  # noqa: E501
                                                        local_var_params['resource'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `resource` when calling `resource_put`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if self.api_client.client_side_validation and ('access_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['access_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `access_token` when calling `resource_put`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in local_var_params or  # noqa: E501
                                                        local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `resource_put`")  # noqa: E501

        if self.api_client.client_side_validation and 'resource' in local_var_params and local_var_params['resource'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `resource` when calling `resource_put`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'access_token' in local_var_params and local_var_params['access_token'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `access_token` when calling `resource_put`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'resource' in local_var_params:
            path_params['resource'] = local_var_params['resource']  # noqa: E501

        query_params = []
        if 'access_token' in local_var_params and local_var_params['access_token'] is not None:  # noqa: E501
            query_params.append(('access_token', local_var_params['access_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/{resource}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
