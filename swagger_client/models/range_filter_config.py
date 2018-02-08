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


class RangeFilterConfig(object):
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
        'gt': 'float',
        'gte': 'float',
        'lt': 'float',
        'lte': 'float'
    }

    attribute_map = {
        'gt': 'gt',
        'gte': 'gte',
        'lt': 'lt',
        'lte': 'lte'
    }

    def __init__(self, gt=None, gte=None, lt=None, lte=None):  # noqa: E501
        """RangeFilterConfig - a model defined in Swagger"""  # noqa: E501

        self._gt = None
        self._gte = None
        self._lt = None
        self._lte = None
        self.discriminator = None

        if gt is not None:
            self.gt = gt
        if gte is not None:
            self.gte = gte
        if lt is not None:
            self.lt = lt
        if lte is not None:
            self.lte = lte

    @property
    def gt(self):
        """Gets the gt of this RangeFilterConfig.  # noqa: E501


        :return: The gt of this RangeFilterConfig.  # noqa: E501
        :rtype: float
        """
        return self._gt

    @gt.setter
    def gt(self, gt):
        """Sets the gt of this RangeFilterConfig.


        :param gt: The gt of this RangeFilterConfig.  # noqa: E501
        :type: float
        """

        self._gt = gt

    @property
    def gte(self):
        """Gets the gte of this RangeFilterConfig.  # noqa: E501


        :return: The gte of this RangeFilterConfig.  # noqa: E501
        :rtype: float
        """
        return self._gte

    @gte.setter
    def gte(self, gte):
        """Sets the gte of this RangeFilterConfig.


        :param gte: The gte of this RangeFilterConfig.  # noqa: E501
        :type: float
        """

        self._gte = gte

    @property
    def lt(self):
        """Gets the lt of this RangeFilterConfig.  # noqa: E501


        :return: The lt of this RangeFilterConfig.  # noqa: E501
        :rtype: float
        """
        return self._lt

    @lt.setter
    def lt(self, lt):
        """Sets the lt of this RangeFilterConfig.


        :param lt: The lt of this RangeFilterConfig.  # noqa: E501
        :type: float
        """

        self._lt = lt

    @property
    def lte(self):
        """Gets the lte of this RangeFilterConfig.  # noqa: E501


        :return: The lte of this RangeFilterConfig.  # noqa: E501
        :rtype: float
        """
        return self._lte

    @lte.setter
    def lte(self, lte):
        """Sets the lte of this RangeFilterConfig.


        :param lte: The lte of this RangeFilterConfig.  # noqa: E501
        :type: float
        """

        self._lte = lte

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
        if not isinstance(other, RangeFilterConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
