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


class HookResponse(object):
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
        'url': 'str',
        'status': 'str',
        'validity': 'str',
        'event_type': 'str',
        'id': 'str',
        'creation_date': 'int',
        'tag': 'str'
    }

    attribute_map = {
        'url': 'Url',
        'status': 'Status',
        'validity': 'Validity',
        'event_type': 'EventType',
        'id': 'Id',
        'creation_date': 'CreationDate',
        'tag': 'Tag'
    }

    def __init__(self, url=None, status=None, validity=None, event_type=None, id=None, creation_date=None, tag=None):  # noqa: E501
        """HookResponse - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._status = None
        self._validity = None
        self._event_type = None
        self._id = None
        self._creation_date = None
        self._tag = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if status is not None:
            self.status = status
        if validity is not None:
            self.validity = validity
        if event_type is not None:
            self.event_type = event_type
        if id is not None:
            self.id = id
        if creation_date is not None:
            self.creation_date = creation_date
        if tag is not None:
            self.tag = tag

    @property
    def url(self):
        """Gets the url of this HookResponse.  # noqa: E501


        :return: The url of this HookResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this HookResponse.


        :param url: The url of this HookResponse.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def status(self):
        """Gets the status of this HookResponse.  # noqa: E501


        :return: The status of this HookResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HookResponse.


        :param status: The status of this HookResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSpecified", "DISABLED", "ENABLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def validity(self):
        """Gets the validity of this HookResponse.  # noqa: E501


        :return: The validity of this HookResponse.  # noqa: E501
        :rtype: str
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this HookResponse.


        :param validity: The validity of this HookResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSpecified", "UNKNOWN", "VALID", "INVALID"]  # noqa: E501
        if validity not in allowed_values:
            raise ValueError(
                "Invalid value for `validity` ({0}), must be one of {1}"  # noqa: E501
                .format(validity, allowed_values)
            )

        self._validity = validity

    @property
    def event_type(self):
        """Gets the event_type of this HookResponse.  # noqa: E501


        :return: The event_type of this HookResponse.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this HookResponse.


        :param event_type: The event_type of this HookResponse.  # noqa: E501
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
    def id(self):
        """Gets the id of this HookResponse.  # noqa: E501

        The item's ID  # noqa: E501

        :return: The id of this HookResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HookResponse.

        The item's ID  # noqa: E501

        :param id: The id of this HookResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def creation_date(self):
        """Gets the creation_date of this HookResponse.  # noqa: E501

        When the item was created  # noqa: E501

        :return: The creation_date of this HookResponse.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this HookResponse.

        When the item was created  # noqa: E501

        :param creation_date: The creation_date of this HookResponse.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def tag(self):
        """Gets the tag of this HookResponse.  # noqa: E501

        Custom data that you can add to this item  # noqa: E501

        :return: The tag of this HookResponse.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this HookResponse.

        Custom data that you can add to this item  # noqa: E501

        :param tag: The tag of this HookResponse.  # noqa: E501
        :type: str
        """

        self._tag = tag

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
        if issubclass(HookResponse, dict):
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
        if not isinstance(other, HookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
