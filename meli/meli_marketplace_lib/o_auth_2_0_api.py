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


class OAuth20Api(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def auth(self, **kwargs):  # noqa: E501
        """Authentication Endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth(response_type=response_type_value, client_id=client_id_value, redirect_uri=redirect_uri_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str response_type: (required)
        :param str client_id: (required)
        :param str redirect_uri: (required)
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
        return self.auth_with_http_info(**kwargs)  # noqa: E501

    def auth_with_http_info(self, **kwargs):  # noqa: E501
        """Authentication Endpoint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.auth_with_http_info(response_type=response_type_value, client_id=client_id_value, redirect_uri=redirect_uri_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str response_type: (required)
        :param str client_id: (required)
        :param str redirect_uri: (required)
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
            'response_type',
            'client_id',
            'redirect_uri'
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
                    " to method auth" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'response_type' is set
        if self.api_client.client_side_validation and ('response_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['response_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `response_type` when calling `auth`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if self.api_client.client_side_validation and ('client_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['client_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `client_id` when calling `auth`")  # noqa: E501
        # verify the required parameter 'redirect_uri' is set
        if self.api_client.client_side_validation and ('redirect_uri' not in local_var_params or  # noqa: E501
                                                        local_var_params['redirect_uri'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `redirect_uri` when calling `auth`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'response_type' in local_var_params and local_var_params['response_type'] is not None:  # noqa: E501
            query_params.append(('response_type', local_var_params['response_type']))  # noqa: E501
        if 'client_id' in local_var_params and local_var_params['client_id'] is not None:  # noqa: E501
            query_params.append(('client_id', local_var_params['client_id']))  # noqa: E501
        if 'redirect_uri' in local_var_params and local_var_params['redirect_uri'] is not None:  # noqa: E501
            query_params.append(('redirect_uri', local_var_params['redirect_uri']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/authorization', 'GET',
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

    def get_token(self, **kwargs):  # noqa: E501
        """Request Access Token  # noqa: E501

        Partner makes a request to the token endpoint by adding the following parameters described below  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str grant_type:
        :param str client_id:
        :param str client_secret:
        :param str redirect_uri:
        :param str code:
        :param str refresh_token:
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
        return self.get_token_with_http_info(**kwargs)  # noqa: E501

    def get_token_with_http_info(self, **kwargs):  # noqa: E501
        """Request Access Token  # noqa: E501

        Partner makes a request to the token endpoint by adding the following parameters described below  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str grant_type:
        :param str client_id:
        :param str client_secret:
        :param str redirect_uri:
        :param str code:
        :param str refresh_token:
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
            'grant_type',
            'client_id',
            'client_secret',
            'redirect_uri',
            'code',
            'refresh_token'
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
                    " to method get_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'grant_type' in local_var_params:
            form_params.append(('grant_type', local_var_params['grant_type']))  # noqa: E501
        if 'client_id' in local_var_params:
            form_params.append(('client_id', local_var_params['client_id']))  # noqa: E501
        if 'client_secret' in local_var_params:
            form_params.append(('client_secret', local_var_params['client_secret']))  # noqa: E501
        if 'redirect_uri' in local_var_params:
            form_params.append(('redirect_uri', local_var_params['redirect_uri']))  # noqa: E501
        if 'code' in local_var_params:
            form_params.append(('code', local_var_params['code']))  # noqa: E501
        if 'refresh_token' in local_var_params:
            form_params.append(('refresh_token', local_var_params['refresh_token']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/oauth/token', 'POST',
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
