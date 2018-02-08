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

from swagger_client.models.mosaic import Mosaic  # noqa: F401,E501
from swagger_client.models.mosaic_series_mosaics_links import MosaicSeriesMosaicsLinks  # noqa: F401,E501


class MosaicSeriesMosaicsListPage(object):
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
        'links': 'MosaicSeriesMosaicsLinks',
        'mosaics': 'list[Mosaic]'
    }

    attribute_map = {
        'links': '_links',
        'mosaics': 'mosaics'
    }

    def __init__(self, links=None, mosaics=None):  # noqa: E501
        """MosaicSeriesMosaicsListPage - a model defined in Swagger"""  # noqa: E501

        self._links = None
        self._mosaics = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if mosaics is not None:
            self.mosaics = mosaics

    @property
    def links(self):
        """Gets the links of this MosaicSeriesMosaicsListPage.  # noqa: E501


        :return: The links of this MosaicSeriesMosaicsListPage.  # noqa: E501
        :rtype: MosaicSeriesMosaicsLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MosaicSeriesMosaicsListPage.


        :param links: The links of this MosaicSeriesMosaicsListPage.  # noqa: E501
        :type: MosaicSeriesMosaicsLinks
        """

        self._links = links

    @property
    def mosaics(self):
        """Gets the mosaics of this MosaicSeriesMosaicsListPage.  # noqa: E501


        :return: The mosaics of this MosaicSeriesMosaicsListPage.  # noqa: E501
        :rtype: list[Mosaic]
        """
        return self._mosaics

    @mosaics.setter
    def mosaics(self, mosaics):
        """Sets the mosaics of this MosaicSeriesMosaicsListPage.


        :param mosaics: The mosaics of this MosaicSeriesMosaicsListPage.  # noqa: E501
        :type: list[Mosaic]
        """

        self._mosaics = mosaics

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
        if not isinstance(other, MosaicSeriesMosaicsListPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
