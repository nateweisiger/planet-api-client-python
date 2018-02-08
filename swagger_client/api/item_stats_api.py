# coding: utf-8

"""
    Planet API

    Top level description of the API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ItemStatsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def stats(self, search, **kwargs):  # noqa: E501
        """Search Stats  # noqa: E501

        Returns a date bucketed histogram of items matching a filter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.stats(search, async=True)
        >>> result = thread.get()

        :param async bool
        :param Stats search: The structured search criteria. (required)
        :return: StatsResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.stats_with_http_info(search, **kwargs)  # noqa: E501
        else:
            (data) = self.stats_with_http_info(search, **kwargs)  # noqa: E501
            return data

    def stats_with_http_info(self, search, **kwargs):  # noqa: E501
        """Search Stats  # noqa: E501

        Returns a date bucketed histogram of items matching a filter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.stats_with_http_info(search, async=True)
        >>> result = thread.get()

        :param async bool
        :param Stats search: The structured search criteria. (required)
        :return: StatsResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search' is set
        if ('search' not in params or
                params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search' in params:
            body_params = params['search']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/data/v1/stats', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatsResults',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
