 #!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager


class SSLAdapter(HTTPAdapter):
    """"Transport adapter" that allows us to use SSLv3."""
    def __init__(self, ssl_version=None, **kwargs):
        self.ssl_version = ssl_version
        super(SSLAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=self.ssl_version)

