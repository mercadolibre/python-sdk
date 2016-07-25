# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import re
import ssl
from ConfigParser import SafeConfigParser
from urllib import urlencode

import requests

from ssl_helper import SSLAdapter


class Meli(object):
    def __init__(self, client_id, client_secret, access_token=None, refresh_token=None, site_id='MLA'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = None
        auth_urls = {'MLA': "https://auth.mercadolibre.com.ar",  # Argentina
                     'MLB': "https://auth.mercadolivre.com.br",  # Brasil
                     'MCO': "https://auth.mercadolibre.com.co",  # Colombia
                     'MCR': "https://auth.mercadolibre.com.cr",  # Costa Rica
                     'MEC': "https://auth.mercadolibre.com.ec",  # Ecuador
                     'MLC': "https://auth.mercadolibre.cl",  # Chile
                     'MLM': "https://auth.mercadolibre.com.mx",  # Mexico
                     'MLU': "https://auth.mercadolibre.com.uy",  # Uruguay
                     'MLV': "https://auth.mercadolibre.com.ve",  # Venezuela
                     'MPA': "https://auth.mercadolibre.com.pa",  # Panama
                     'MPE': "https://auth.mercadolibre.com.pe",  # Peru
                     'MPT': "https://auth.mercadolibre.com.pt",  # Prtugal
                     'MRD': "https://auth.mercadolibre.com.do"}  # Dominicana
        parser = SafeConfigParser()
        parser.read(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')

        self._requests = requests.Session()
        try:
            self.SSL_VERSION = parser.get('config', 'ssl_version')
            self._requests.mount('https://', SSLAdapter(ssl_version=getattr(ssl, self.SSL_VERSION)))
        except:
            self._requests = requests

        self.API_ROOT_URL = parser.get('config', 'api_root_url')
        self.SDK_VERSION = parser.get('config', 'sdk_version')
        self.AUTH_URL = auth_urls.get(site_id.upper(), site_id['MLA'])
        self.OAUTH_URL = parser.get('config', 'oauth_url')

    # AUTH METHODS
    def auth_url(self, redirect_URI):
        params = {'client_id': self.client_id, 'response_type': 'code', 'redirect_uri': redirect_URI}
        url = self.AUTH_URL + '/authorization' + '?' + urlencode(params)
        return url

    def authorize(self, code, redirect_URI):
        params = {'grant_type': 'authorization_code', 'client_id': self.client_id, 'client_secret': self.client_secret,
                  'code': code, 'redirect_uri': redirect_URI}
        headers = {'Accept': 'application/json', 'User-Agent': self.SDK_VERSION, 'Content-type': 'application/json'}
        uri = self.make_path(self.OAUTH_URL)

        response = self._requests.post(uri, params=urlencode(params), headers=headers)

        if response.status_code == requests.codes.ok:
            response_info = response.json()
            self.access_token = response_info['access_token']
            if 'refresh_token' in response_info:
                self.refresh_token = response_info['refresh_token']
            else:
                self.refresh_token = ''  # offline_access not set up
                self.expires_in = response_info['expires_in']

            return self.access_token
        else:
            # response code isn't a 200; raise an exception
            response.raise_for_status()

    def get_refresh_token(self):
        if self.refresh_token:
            params = {'grant_type': 'refresh_token', 'client_id': self.client_id, 'client_secret': self.client_secret,
                      'refresh_token': self.refresh_token}
            headers = {'Accept': 'application/json', 'User-Agent': self.SDK_VERSION, 'Content-type': 'application/json'}
            uri = self.make_path(self.OAUTH_URL)

            response = self._requests.post(uri, params=urlencode(params), headers=headers, data=params)

            if response.status_code == requests.codes.ok:
                response_info = response.json()
                self.access_token = response_info['access_token']
                self.refresh_token = response_info['refresh_token']
                self.expires_in = response_info['expires_in']
                return self.access_token
            else:
                # response code isn't a 200; raise an exception
                response.raise_for_status()
        else:
            raise Exception, "Offline-Access is not allowed."

    # REQUEST METHODS
    def get(self, path, params={}):
        headers = {'Accept': 'application/json', 'User-Agent': self.SDK_VERSION, 'Content-type': 'application/json'}
        uri = self.make_path(path)
        response = self._requests.get(uri, params=urlencode(params), headers=headers)
        return response

    def post(self, path, body=None, params={}):
        headers = {'Accept': 'application/json', 'User-Agent': self.SDK_VERSION, 'Content-type': 'application/json'}
        uri = self.make_path(path)
        if body:
            body = json.dumps(body)

        response = self._requests.post(uri, data=body, params=urlencode(params), headers=headers)
        return response

    def put(self, path, body=None, params={}):
        headers = {'Accept': 'application/json', 'User-Agent': self.SDK_VERSION, 'Content-type': 'application/json'}
        uri = self.make_path(path)
        if body:
            body = json.dumps(body)

        response = self._requests.put(uri, data=body, params=urlencode(params), headers=headers)
        return response

    def delete(self, path, params={}):
        headers = {'Accept': 'application/json', 'User-Agent': self.SDK_VERSION, 'Content-type': 'application/json'}
        uri = self.make_path(path)
        response = self._requests.delete(uri, params=params, headers=headers)
        return response

    def options(self, path, params={}):
        headers = {'Accept': 'application/json', 'User-Agent': self.SDK_VERSION, 'Content-type': 'application/json'}
        uri = self.make_path(path)
        response = self._requests.options(uri, params=urlencode(params), headers=headers)
        return response

    def make_path(self, path, params={}):
        # Making Path and add a leading / if not exist
        if not (re.search("^http", path)):
            if not (re.search("^\/", path)):
                path = "/" + path
            path = self.API_ROOT_URL + path
        if params:
            path = path + "?" + urlencode(params)
        return path
