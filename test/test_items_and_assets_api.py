# coding: utf-8

"""
    Planet API

    Top level description of the API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.items_and_assets_api import ItemsAndAssetsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestItemsAndAssetsApi(unittest.TestCase):
    """ItemsAndAssetsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.items_and_assets_api.ItemsAndAssetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_asset_type(self):
        """Test case for get_asset_type

        Get Asset Type  # noqa: E501
        """
        pass

    def test_get_item(self):
        """Test case for get_item

        Get Item  # noqa: E501
        """
        pass

    def test_get_item_type(self):
        """Test case for get_item_type

        Get Item Type  # noqa: E501
        """
        pass

    def test_list_asset_types(self):
        """Test case for list_asset_types

        List Asset Types  # noqa: E501
        """
        pass

    def test_list_item_assets(self):
        """Test case for list_item_assets

        List Item Assets  # noqa: E501
        """
        pass

    def test_list_item_types(self):
        """Test case for list_item_types

        List Item Types  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
