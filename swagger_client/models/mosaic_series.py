# coding: utf-8

"""
    Planet API

    Top level description of the API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.mosaic_series_links import MosaicSeriesLinks  # noqa: F401,E501


class MosaicSeries(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'links': 'MosaicSeriesLinks',
        'first_acquired': 'datetime',
        'id': 'str',
        'interval': 'str',
        'last_acquired': 'datetime',
        'name': 'str',
        'product_type': 'str',
        'selector': 'str'
    }

    attribute_map = {
        'links': '_links',
        'first_acquired': 'first_acquired',
        'id': 'id',
        'interval': 'interval',
        'last_acquired': 'last_acquired',
        'name': 'name',
        'product_type': 'product_type',
        'selector': 'selector'
    }

    def __init__(self, links=None, first_acquired=None, id=None, interval=None, last_acquired=None, name=None, product_type=None, selector=None):  # noqa: E501
        """MosaicSeries - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._first_acquired = None
        self._id = None
        self._interval = None
        self._last_acquired = None
        self._name = None
        self._product_type = None
        self._selector = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if first_acquired is not None:
            self.first_acquired = first_acquired
        if id is not None:
            self.id = id
        self.interval = interval
        if last_acquired is not None:
            self.last_acquired = last_acquired
        self.name = name
        self.product_type = product_type
        self.selector = selector

    @property
    def links(self):
        """Gets the links of this MosaicSeries.  # noqa: E501


        :return: The links of this MosaicSeries.  # noqa: E501
        :rtype: MosaicSeriesLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MosaicSeries.


        :param links: The links of this MosaicSeries.  # noqa: E501
        :type: MosaicSeriesLinks
        """

        self._links = links

    @property
    def first_acquired(self):
        """Gets the first_acquired of this MosaicSeries.  # noqa: E501

        The acquisition date of the oldest scene that contributed to this series.  # noqa: E501

        :return: The first_acquired of this MosaicSeries.  # noqa: E501
        :rtype: datetime
        """
        return self._first_acquired

    @first_acquired.setter
    def first_acquired(self, first_acquired):
        """Sets the first_acquired of this MosaicSeries.

        The acquisition date of the oldest scene that contributed to this series.  # noqa: E501

        :param first_acquired: The first_acquired of this MosaicSeries.  # noqa: E501
        :type: datetime
        """

        self._first_acquired = first_acquired

    @property
    def id(self):
        """Gets the id of this MosaicSeries.  # noqa: E501

        Mosaic series identifier.  # noqa: E501

        :return: The id of this MosaicSeries.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MosaicSeries.

        Mosaic series identifier.  # noqa: E501

        :param id: The id of this MosaicSeries.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def interval(self):
        """Gets the interval of this MosaicSeries.  # noqa: E501

        The interval for the mosaics in the series.  # noqa: E501

        :return: The interval of this MosaicSeries.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this MosaicSeries.

        The interval for the mosaics in the series.  # noqa: E501

        :param interval: The interval of this MosaicSeries.  # noqa: E501
        :type: str
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def last_acquired(self):
        """Gets the last_acquired of this MosaicSeries.  # noqa: E501

        The acquisition date of the newest scene that contributed to this series.  # noqa: E501

        :return: The last_acquired of this MosaicSeries.  # noqa: E501
        :rtype: datetime
        """
        return self._last_acquired

    @last_acquired.setter
    def last_acquired(self, last_acquired):
        """Sets the last_acquired of this MosaicSeries.

        The acquisition date of the newest scene that contributed to this series.  # noqa: E501

        :param last_acquired: The last_acquired of this MosaicSeries.  # noqa: E501
        :type: datetime
        """

        self._last_acquired = last_acquired

    @property
    def name(self):
        """Gets the name of this MosaicSeries.  # noqa: E501

        A human readable name for this series.  # noqa: E501

        :return: The name of this MosaicSeries.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MosaicSeries.

        A human readable name for this series.  # noqa: E501

        :param name: The name of this MosaicSeries.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def product_type(self):
        """Gets the product_type of this MosaicSeries.  # noqa: E501

        The type of product this mosaic is.  # noqa: E501

        :return: The product_type of this MosaicSeries.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this MosaicSeries.

        The type of product this mosaic is.  # noqa: E501

        :param product_type: The product_type of this MosaicSeries.  # noqa: E501
        :type: str
        """
        if product_type is None:
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501
        allowed_values = ["basemap", "timelapse", "l3m"]  # noqa: E501
        if product_type not in allowed_values:
            raise ValueError(
                "Invalid value for `product_type` ({0}), must be one of {1}"  # noqa: E501
                .format(product_type, allowed_values)
            )

        self._product_type = product_type

    @property
    def selector(self):
        """Gets the selector of this MosaicSeries.  # noqa: E501

        A regular expression to match mosaic names.  # noqa: E501

        :return: The selector of this MosaicSeries.  # noqa: E501
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this MosaicSeries.

        A regular expression to match mosaic names.  # noqa: E501

        :param selector: The selector of this MosaicSeries.  # noqa: E501
        :type: str
        """
        if selector is None:
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MosaicSeries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
