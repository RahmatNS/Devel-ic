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


class HookPost(object):
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
        'tag': 'str',
        'event_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'tag': 'Tag',
        'event_type': 'EventType',
        'url': 'Url'
    }

    def __init__(self, tag=None, event_type=None, url=None):  # noqa: E501
        """HookPost - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._event_type = None
        self._url = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if event_type is not None:
            self.event_type = event_type
        if url is not None:
            self.url = url

    @property
    def tag(self):
        """Gets the tag of this HookPost.  # noqa: E501


        :return: The tag of this HookPost.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this HookPost.


        :param tag: The tag of this HookPost.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def event_type(self):
        """Gets the event_type of this HookPost.  # noqa: E501


        :return: The event_type of this HookPost.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this HookPost.


        :param event_type: The event_type of this HookPost.  # noqa: E501
        :type: str
        """
        allowed_values = ["All", "PAYIN_NORMAL_CREATED", "PAYIN_NORMAL_SUCCEEDED", "PAYIN_NORMAL_FAILED", "PAYOUT_NORMAL_CREATED", "PAYOUT_NORMAL_SUCCEEDED", "PAYOUT_NORMAL_FAILED", "TRANSFER_NORMAL_CREATED", "TRANSFER_NORMAL_SUCCEEDED", "TRANSFER_NORMAL_FAILED", "PAYIN_REFUND_CREATED", "PAYIN_REFUND_SUCCEEDED", "PAYIN_REFUND_FAILED", "PAYOUT_REFUND_CREATED", "PAYOUT_REFUND_SUCCEEDED", "PAYOUT_REFUND_FAILED", "TRANSFER_REFUND_CREATED", "TRANSFER_REFUND_SUCCEEDED", "TRANSFER_REFUND_FAILED", "KYC_CREATED", "KYC_VALIDATION_ASKED", "KYC_SUCCEEDED", "KYC_FAILED", "PAYIN_REPUDIATION_CREATED", "PAYIN_REPUDIATION_SUCCEEDED", "PAYIN_REPUDIATION_FAILED", "DISPUTE_DOCUMENT_CREATED", "DISPUTE_DOCUMENT_VALIDATION_ASKED", "DISPUTE_DOCUMENT_SUCCEEDED", "DISPUTE_DOCUMENT_FAILED", "DISPUTE_CREATED", "DISPUTE_SUBMITTED", "DISPUTE_ACTION_REQUIRED", "DISPUTE_FURTHER_ACTION_REQUIRED", "DISPUTE_CLOSED", "DISPUTE_SENT_TO_BANK", "TRANSFER_SETTLEMENT_CREATED", "TRANSFER_SETTLEMENT_SUCCEEDED", "TRANSFER_SETTLEMENT_FAILED"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def url(self):
        """Gets the url of this HookPost.  # noqa: E501


        :return: The url of this HookPost.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HookPost.


        :param url: The url of this HookPost.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(HookPost, dict):
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
        if not isinstance(other, HookPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other