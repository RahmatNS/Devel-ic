# coding: utf-8

"""
    MarketPay API

    API for Smart Contracts and Payments  # noqa: E501

    OpenAPI spec version: v2.01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PaymentRedsysData(object):
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
        'ds_order': 'str',
        'ds_authorisation_code': 'str'
    }

    attribute_map = {
        'ds_order': 'DsOrder',
        'ds_authorisation_code': 'DsAuthorisationCode'
    }

    def __init__(self, ds_order=None, ds_authorisation_code=None):  # noqa: E501
        """PaymentRedsysData - a model defined in Swagger"""  # noqa: E501

        self._ds_order = None
        self._ds_authorisation_code = None
        self.discriminator = None

        if ds_order is not None:
            self.ds_order = ds_order
        if ds_authorisation_code is not None:
            self.ds_authorisation_code = ds_authorisation_code

    @property
    def ds_order(self):
        """Gets the ds_order of this PaymentRedsysData.  # noqa: E501


        :return: The ds_order of this PaymentRedsysData.  # noqa: E501
        :rtype: str
        """
        return self._ds_order

    @ds_order.setter
    def ds_order(self, ds_order):
        """Sets the ds_order of this PaymentRedsysData.


        :param ds_order: The ds_order of this PaymentRedsysData.  # noqa: E501
        :type: str
        """

        self._ds_order = ds_order

    @property
    def ds_authorisation_code(self):
        """Gets the ds_authorisation_code of this PaymentRedsysData.  # noqa: E501


        :return: The ds_authorisation_code of this PaymentRedsysData.  # noqa: E501
        :rtype: str
        """
        return self._ds_authorisation_code

    @ds_authorisation_code.setter
    def ds_authorisation_code(self, ds_authorisation_code):
        """Sets the ds_authorisation_code of this PaymentRedsysData.


        :param ds_authorisation_code: The ds_authorisation_code of this PaymentRedsysData.  # noqa: E501
        :type: str
        """

        self._ds_authorisation_code = ds_authorisation_code

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
        if issubclass(PaymentRedsysData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentRedsysData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
