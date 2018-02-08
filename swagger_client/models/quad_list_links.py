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


class QuadListLinks(object):
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
        'next': 'str',
        '_self': 'str'
    }

    attribute_map = {
        'next': '_next',
        '_self': '_self'
    }

    def __init__(self, next=None, _self=None):  # noqa: E501
        """QuadListLinks - a model defined in Swagger"""  # noqa: E501

        self._next = None
        self.__self = None
        self.discriminator = None

        if next is not None:
            self.next = next
        if _self is not None:
            self._self = _self

    @property
    def next(self):
        """Gets the next of this QuadListLinks.  # noqa: E501

        RFC 3986 URI representing the location of the next page of results. Omitted when there are no results, or the current page is the last.  # noqa: E501

        :return: The next of this QuadListLinks.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this QuadListLinks.

        RFC 3986 URI representing the location of the next page of results. Omitted when there are no results, or the current page is the last.  # noqa: E501

        :param next: The next of this QuadListLinks.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def _self(self):
        """Gets the _self of this QuadListLinks.  # noqa: E501

        RFC 3986 URI representing the canonical location of this object.  # noqa: E501

        :return: The _self of this QuadListLinks.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this QuadListLinks.

        RFC 3986 URI representing the canonical location of this object.  # noqa: E501

        :param _self: The _self of this QuadListLinks.  # noqa: E501
        :type: str
        """

        self.__self = _self

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
        if not isinstance(other, QuadListLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other