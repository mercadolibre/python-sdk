# coding: utf-8

"""
    MELI Markeplace SDK

    This is a the codebase to generate a SDK for Open Platform Marketplace  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import meli
from meli_marketplace_lib.categories_api import CategoriesApi  # noqa: E501
from meli.rest import ApiException


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self):
        self.api = meli_marketplace_lib.categories_api.CategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_categories_category_id_get(self):
        """Test case for categories_category_id_get

        Return by category.  # noqa: E501
        """
        pass

    def test_sites_site_id_categories_get(self):
        """Test case for sites_site_id_categories_get

        Return a categories by site.  # noqa: E501
        """
        pass

    def test_sites_site_id_domain_discovery_search_get(self):
        """Test case for sites_site_id_domain_discovery_search_get

        Predictor  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
