import unittest
import re
import sys
sys.path.append('../lib')
from meli import Meli
import requests
import json

class MeliTest(unittest.TestCase):

    def setUp(self):
        self.CLIENT_ID = "123"
        self.CLIENT_SECRET = "a secret"
        self.ACCESS_TOKEN = "a access_token"
        self.REFRESH_TOKEN = "a refresh_token"
        self.NEW_ACCESS_TOKEN = "a new access_token"
        self.NEW_REFRESH_TOKEN = "a new refresh_token"
        self.meli =  Meli(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, access_token=self.ACCESS_TOKEN, refresh_token=self.REFRESH_TOKEN)


    #constructor tests
    def testClientId(self):
        self.assertEqual(self.meli.client_id, self.CLIENT_ID)

    def testClientSecret(self):
        self.assertEqual(self.meli.client_secret, self.CLIENT_SECRET)

    def testAccessToken(self):
        self.assertEqual(self.meli.access_token, self.ACCESS_TOKEN)

    def testRefreshToken(self):
        self.assertEqual(self.meli.refresh_token, self.REFRESH_TOKEN)

    #auth_url tests
    def testAuthUrl(self):
        callback = "http://test.com/callback"
        self.assertTrue(re.search("^http", self.meli.auth_url(redirect_URI=callback)))
        self.assertTrue(re.search("^https\:\/\/auth.mercadolibre.com\/authorization", self.meli.auth_url(redirect_URI=callback)))
        self.assertTrue(re.search("redirect_uri", self.meli.auth_url(redirect_URI=callback)))
        self.assertTrue(re.search(self.CLIENT_ID,self.meli.auth_url(redirect_URI=callback)))
        self.assertTrue(re.search("response_type", self.meli.auth_url(redirect_URI=callback)))

    #Mock requests
    def mockGet(url, path=None, params={},headers={}, data=None, body=None):

        response = requests.Response()

        if re.search("/users/me", url):
            if "access_token" in params:
                response.status_code = 200
            else:
                response.status_code = 403
        elif re.search("/authorization", url):
            response.status_code = 200
        else:
            response.status_code = 200
        return response

    def mockPost(url, path=None, body=None, params={},headers={}, data=None):
        response = requests.Response()

        if re.search("/oauth/token", url):
            if "grant_type" not in params or "client_id" not in params or "client_secret" not in params:
                response.status_code = 403
            else:
                if re.search("grant_type=authorization_code", params):
                    content = {'access_token' : 'a access_token', 'refresh_token' : 'a refresh_token'}
                elif re.search("grant_type=refresh_token", params):
                    content = {'access_token' : 'a new access_token', 'refresh_token' : 'a new refresh_token'}
                response._content = json.dumps(content)
                response.status_code = 200
        else:
            if "access_token" in params:
                response.status_code = 200
            else:
                response.status_code = 403

        return response

    def mockPut(url, path=None, body=None, params={},headers={}, data=None):
        response = requests.Response()
        if "access_token" in params:
            response.status_code = 200
        else:
            response.status_code = 403
        return response

    def mockDelete(url, path=None, params={},headers={}, data=None, body=None):
        response = requests.Response()
        if "access_token" in params:
            response.status_code = 200
        else:
            response.status_code = 403
        return response

    requests.get    = mockGet
    requests.post   = mockPost
    requests.put    = mockPut
    requests.delete = mockDelete

    #requests tests
    def testGet(self):
        response = self.meli.get(path="/items/test1")
        self.assertEqual(response.status_code, requests.codes.ok)

    def testPost(self):
        body = {"condition":"new", "warranty":"60 dias", "currency_id":"BRL", "accepts_mercadopago":True, "description":"Lindo Ray_Ban_Original_Wayfarer", "listing_type_id":"bronze", "title":"oculos Ray Ban Aviador  Que Troca As Lentes  Lancamento!", "available_quantity":64, "price":289, "subtitle":"Acompanha 3 Pares De Lentes!! Compra 100% Segura", "buying_mode":"buy_it_now", "category_id":"MLB5125", "pictures":[{"source":"http://upload.wikimedia.org/wikipedia/commons/f/fd/Ray_Ban_Original_Wayfarer.jpg"}, {"source":"http://en.wikipedia.org/wiki/File:Teashades.gif"}] }
        response = self.meli.post(path="/items",body=body,params={'access_token' : self.meli.access_token})
        self.assertEqual(response.status_code, requests.codes.ok)

    def testPut(self):
        body = {"title":"oculos edicao especial!", "price":1000 }
        response = self.meli.put(path="/items/test1",body=body,params={'access_token' : self.meli.access_token})
        self.assertEqual(response.status_code, requests.codes.ok)

    def testDelete(self):
        response = self.meli.delete(path="/questions/123",params={'access_token' : self.meli.access_token})
        self.assertEqual(response.status_code, requests.codes.ok)

    def testWithoutAccessToken(self):
        response = self.meli.get(path="/users/me")
        self.assertEqual(response.status_code, requests.codes.forbidden)

    def testWithAccessToken(self):
        response = self.meli.get(path="/users/me",params={'access_token' : self.meli.access_token})
        self.assertEqual(response.status_code, requests.codes.ok)

    #auth tests
    def testAuthorize(self):
        self.meli.access_token = None
        self.meli.refresh_token = None
        response = self.meli.authorize(code="a code from get param", redirect_URI="A redirect Uri")
        self.assertEqual(self.meli.access_token, self.ACCESS_TOKEN)
        self.assertEqual(self.meli.refresh_token, self.REFRESH_TOKEN)


    def testDoRefreshToken(self):
        response = self.meli.get_refresh_token()
        self.assertEqual(self.meli.access_token, self.NEW_ACCESS_TOKEN)
        self.assertEqual(self.meli.refresh_token, self.NEW_REFRESH_TOKEN)


if __name__ == '__main__':
    unittest.main()
