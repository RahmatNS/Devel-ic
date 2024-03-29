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

from swagger_client.models.address import Address  # noqa: F401,E501


class BankwirePayInBankAccount(object):
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
        'type': 'str',
        'owner_address': 'Address',
        'owner_name': 'str',
        'iban': 'str',
        'bic': 'str',
        'sort_code': 'str',
        'account_number': 'str'
    }

    attribute_map = {
        'type': 'Type',
        'owner_address': 'OwnerAddress',
        'owner_name': 'OwnerName',
        'iban': 'IBAN',
        'bic': 'BIC',
        'sort_code': 'SortCode',
        'account_number': 'AccountNumber'
    }

    def __init__(self, type=None, owner_address=None, owner_name=None, iban=None, bic=None, sort_code=None, account_number=None):  # noqa: E501
        """BankwirePayInBankAccount - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._owner_address = None
        self._owner_name = None
        self._iban = None
        self._bic = None
        self._sort_code = None
        self._account_number = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if owner_address is not None:
            self.owner_address = owner_address
        if owner_name is not None:
            self.owner_name = owner_name
        if iban is not None:
            self.iban = iban
        if bic is not None:
            self.bic = bic
        if sort_code is not None:
            self.sort_code = sort_code
        if account_number is not None:
            self.account_number = account_number

    @property
    def type(self):
        """Gets the type of this BankwirePayInBankAccount.  # noqa: E501


        :return: The type of this BankwirePayInBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BankwirePayInBankAccount.


        :param type: The type of this BankwirePayInBankAccount.  # noqa: E501
        :type: str
        """
        allowed_values = ["IBAN", "GB", "US", "CA", "OTHER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def owner_address(self):
        """Gets the owner_address of this BankwirePayInBankAccount.  # noqa: E501


        :return: The owner_address of this BankwirePayInBankAccount.  # noqa: E501
        :rtype: Address
        """
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address):
        """Sets the owner_address of this BankwirePayInBankAccount.


        :param owner_address: The owner_address of this BankwirePayInBankAccount.  # noqa: E501
        :type: Address
        """

        self._owner_address = owner_address

    @property
    def owner_name(self):
        """Gets the owner_name of this BankwirePayInBankAccount.  # noqa: E501


        :return: The owner_name of this BankwirePayInBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this BankwirePayInBankAccount.


        :param owner_name: The owner_name of this BankwirePayInBankAccount.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def iban(self):
        """Gets the iban of this BankwirePayInBankAccount.  # noqa: E501


        :return: The iban of this BankwirePayInBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this BankwirePayInBankAccount.


        :param iban: The iban of this BankwirePayInBankAccount.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def bic(self):
        """Gets the bic of this BankwirePayInBankAccount.  # noqa: E501


        :return: The bic of this BankwirePayInBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this BankwirePayInBankAccount.


        :param bic: The bic of this BankwirePayInBankAccount.  # noqa: E501
        :type: str
        """

        self._bic = bic

    @property
    def sort_code(self):
        """Gets the sort_code of this BankwirePayInBankAccount.  # noqa: E501


        :return: The sort_code of this BankwirePayInBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """Sets the sort_code of this BankwirePayInBankAccount.


        :param sort_code: The sort_code of this BankwirePayInBankAccount.  # noqa: E501
        :type: str
        """

        self._sort_code = sort_code

    @property
    def account_number(self):
        """Gets the account_number of this BankwirePayInBankAccount.  # noqa: E501


        :return: The account_number of this BankwirePayInBankAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this BankwirePayInBankAccount.


        :param account_number: The account_number of this BankwirePayInBankAccount.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

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
        if issubclass(BankwirePayInBankAccount, dict):
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
        if not isinstance(other, BankwirePayInBankAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
