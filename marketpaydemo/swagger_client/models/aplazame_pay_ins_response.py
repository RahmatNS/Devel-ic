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

from swagger_client.models.money import Money  # noqa: F401,E501


class AplazamePayInsResponse(object):
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
        'debited_funds': 'Money',
        'credited_funds': 'Money',
        'fees': 'Money',
        'credited_wallet_id': 'str',
        'nature': 'str',
        'status': 'str',
        'execution_date': 'int',
        'result_code': 'str',
        'result_message': 'str',
        'type': 'str',
        'payment_type': 'str',
        'execution_type': 'str',
        'card_id': 'str',
        'statement_descriptor': 'str',
        'author_id': 'str',
        'credited_user_id': 'str',
        'id': 'str',
        'creation_date': 'int',
        'tag': 'str'
    }

    attribute_map = {
        'debited_funds': 'DebitedFunds',
        'credited_funds': 'CreditedFunds',
        'fees': 'Fees',
        'credited_wallet_id': 'CreditedWalletId',
        'nature': 'Nature',
        'status': 'Status',
        'execution_date': 'ExecutionDate',
        'result_code': 'ResultCode',
        'result_message': 'ResultMessage',
        'type': 'Type',
        'payment_type': 'PaymentType',
        'execution_type': 'ExecutionType',
        'card_id': 'CardId',
        'statement_descriptor': 'StatementDescriptor',
        'author_id': 'AuthorId',
        'credited_user_id': 'CreditedUserId',
        'id': 'Id',
        'creation_date': 'CreationDate',
        'tag': 'Tag'
    }

    def __init__(self, debited_funds=None, credited_funds=None, fees=None, credited_wallet_id=None, nature=None, status=None, execution_date=None, result_code=None, result_message=None, type=None, payment_type=None, execution_type=None, card_id=None, statement_descriptor=None, author_id=None, credited_user_id=None, id=None, creation_date=None, tag=None):  # noqa: E501
        """AplazamePayInsResponse - a model defined in Swagger"""  # noqa: E501

        self._debited_funds = None
        self._credited_funds = None
        self._fees = None
        self._credited_wallet_id = None
        self._nature = None
        self._status = None
        self._execution_date = None
        self._result_code = None
        self._result_message = None
        self._type = None
        self._payment_type = None
        self._execution_type = None
        self._card_id = None
        self._statement_descriptor = None
        self._author_id = None
        self._credited_user_id = None
        self._id = None
        self._creation_date = None
        self._tag = None
        self.discriminator = None

        if debited_funds is not None:
            self.debited_funds = debited_funds
        if credited_funds is not None:
            self.credited_funds = credited_funds
        if fees is not None:
            self.fees = fees
        if credited_wallet_id is not None:
            self.credited_wallet_id = credited_wallet_id
        if nature is not None:
            self.nature = nature
        if status is not None:
            self.status = status
        if execution_date is not None:
            self.execution_date = execution_date
        if result_code is not None:
            self.result_code = result_code
        if result_message is not None:
            self.result_message = result_message
        if type is not None:
            self.type = type
        if payment_type is not None:
            self.payment_type = payment_type
        if execution_type is not None:
            self.execution_type = execution_type
        if card_id is not None:
            self.card_id = card_id
        if statement_descriptor is not None:
            self.statement_descriptor = statement_descriptor
        if author_id is not None:
            self.author_id = author_id
        if credited_user_id is not None:
            self.credited_user_id = credited_user_id
        if id is not None:
            self.id = id
        if creation_date is not None:
            self.creation_date = creation_date
        if tag is not None:
            self.tag = tag

    @property
    def debited_funds(self):
        """Gets the debited_funds of this AplazamePayInsResponse.  # noqa: E501


        :return: The debited_funds of this AplazamePayInsResponse.  # noqa: E501
        :rtype: Money
        """
        return self._debited_funds

    @debited_funds.setter
    def debited_funds(self, debited_funds):
        """Sets the debited_funds of this AplazamePayInsResponse.


        :param debited_funds: The debited_funds of this AplazamePayInsResponse.  # noqa: E501
        :type: Money
        """

        self._debited_funds = debited_funds

    @property
    def credited_funds(self):
        """Gets the credited_funds of this AplazamePayInsResponse.  # noqa: E501


        :return: The credited_funds of this AplazamePayInsResponse.  # noqa: E501
        :rtype: Money
        """
        return self._credited_funds

    @credited_funds.setter
    def credited_funds(self, credited_funds):
        """Sets the credited_funds of this AplazamePayInsResponse.


        :param credited_funds: The credited_funds of this AplazamePayInsResponse.  # noqa: E501
        :type: Money
        """

        self._credited_funds = credited_funds

    @property
    def fees(self):
        """Gets the fees of this AplazamePayInsResponse.  # noqa: E501


        :return: The fees of this AplazamePayInsResponse.  # noqa: E501
        :rtype: Money
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this AplazamePayInsResponse.


        :param fees: The fees of this AplazamePayInsResponse.  # noqa: E501
        :type: Money
        """

        self._fees = fees

    @property
    def credited_wallet_id(self):
        """Gets the credited_wallet_id of this AplazamePayInsResponse.  # noqa: E501


        :return: The credited_wallet_id of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._credited_wallet_id

    @credited_wallet_id.setter
    def credited_wallet_id(self, credited_wallet_id):
        """Sets the credited_wallet_id of this AplazamePayInsResponse.


        :param credited_wallet_id: The credited_wallet_id of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """

        self._credited_wallet_id = credited_wallet_id

    @property
    def nature(self):
        """Gets the nature of this AplazamePayInsResponse.  # noqa: E501


        :return: The nature of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._nature

    @nature.setter
    def nature(self, nature):
        """Sets the nature of this AplazamePayInsResponse.


        :param nature: The nature of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["REGULAR", "REFUND", "REPUDIATION", "SETTLEMENT"]  # noqa: E501
        if nature not in allowed_values:
            raise ValueError(
                "Invalid value for `nature` ({0}), must be one of {1}"  # noqa: E501
                .format(nature, allowed_values)
            )

        self._nature = nature

    @property
    def status(self):
        """Gets the status of this AplazamePayInsResponse.  # noqa: E501


        :return: The status of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AplazamePayInsResponse.


        :param status: The status of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "SUCCEEDED", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def execution_date(self):
        """Gets the execution_date of this AplazamePayInsResponse.  # noqa: E501


        :return: The execution_date of this AplazamePayInsResponse.  # noqa: E501
        :rtype: int
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date):
        """Sets the execution_date of this AplazamePayInsResponse.


        :param execution_date: The execution_date of this AplazamePayInsResponse.  # noqa: E501
        :type: int
        """

        self._execution_date = execution_date

    @property
    def result_code(self):
        """Gets the result_code of this AplazamePayInsResponse.  # noqa: E501


        :return: The result_code of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this AplazamePayInsResponse.


        :param result_code: The result_code of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """

        self._result_code = result_code

    @property
    def result_message(self):
        """Gets the result_message of this AplazamePayInsResponse.  # noqa: E501


        :return: The result_message of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_message

    @result_message.setter
    def result_message(self, result_message):
        """Sets the result_message of this AplazamePayInsResponse.


        :param result_message: The result_message of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """

        self._result_message = result_message

    @property
    def type(self):
        """Gets the type of this AplazamePayInsResponse.  # noqa: E501


        :return: The type of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AplazamePayInsResponse.


        :param type: The type of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["PAYIN", "PAYOUT", "TRANSFER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def payment_type(self):
        """Gets the payment_type of this AplazamePayInsResponse.  # noqa: E501


        :return: The payment_type of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this AplazamePayInsResponse.


        :param payment_type: The payment_type of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSpecified", "CARD", "BANK_WIRE", "DIRECT_DEBIT", "PREAUTHORIZED", "PLUGIN"]  # noqa: E501
        if payment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_type, allowed_values)
            )

        self._payment_type = payment_type

    @property
    def execution_type(self):
        """Gets the execution_type of this AplazamePayInsResponse.  # noqa: E501


        :return: The execution_type of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._execution_type

    @execution_type.setter
    def execution_type(self, execution_type):
        """Sets the execution_type of this AplazamePayInsResponse.


        :param execution_type: The execution_type of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSpecified", "WEB", "DIRECT"]  # noqa: E501
        if execution_type not in allowed_values:
            raise ValueError(
                "Invalid value for `execution_type` ({0}), must be one of {1}"  # noqa: E501
                .format(execution_type, allowed_values)
            )

        self._execution_type = execution_type

    @property
    def card_id(self):
        """Gets the card_id of this AplazamePayInsResponse.  # noqa: E501


        :return: The card_id of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this AplazamePayInsResponse.


        :param card_id: The card_id of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """

        self._card_id = card_id

    @property
    def statement_descriptor(self):
        """Gets the statement_descriptor of this AplazamePayInsResponse.  # noqa: E501


        :return: The statement_descriptor of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._statement_descriptor

    @statement_descriptor.setter
    def statement_descriptor(self, statement_descriptor):
        """Sets the statement_descriptor of this AplazamePayInsResponse.


        :param statement_descriptor: The statement_descriptor of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """

        self._statement_descriptor = statement_descriptor

    @property
    def author_id(self):
        """Gets the author_id of this AplazamePayInsResponse.  # noqa: E501


        :return: The author_id of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this AplazamePayInsResponse.


        :param author_id: The author_id of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """

        self._author_id = author_id

    @property
    def credited_user_id(self):
        """Gets the credited_user_id of this AplazamePayInsResponse.  # noqa: E501


        :return: The credited_user_id of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._credited_user_id

    @credited_user_id.setter
    def credited_user_id(self, credited_user_id):
        """Sets the credited_user_id of this AplazamePayInsResponse.


        :param credited_user_id: The credited_user_id of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """

        self._credited_user_id = credited_user_id

    @property
    def id(self):
        """Gets the id of this AplazamePayInsResponse.  # noqa: E501

        The item's ID  # noqa: E501

        :return: The id of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AplazamePayInsResponse.

        The item's ID  # noqa: E501

        :param id: The id of this AplazamePayInsResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def creation_date(self):
        """Gets the creation_date of this AplazamePayInsResponse.  # noqa: E501

        When the item was created  # noqa: E501

        :return: The creation_date of this AplazamePayInsResponse.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this AplazamePayInsResponse.

        When the item was created  # noqa: E501

        :param creation_date: The creation_date of this AplazamePayInsResponse.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def tag(self):
        """Gets the tag of this AplazamePayInsResponse.  # noqa: E501

        Custom data that you can add to this item  # noqa: E501

        :return: The tag of this AplazamePayInsResponse.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this AplazamePayInsResponse.

        Custom data that you can add to this item  # noqa: E501

        :param tag: The tag of this AplazamePayInsResponse.  # noqa: E501
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
        if issubclass(AplazamePayInsResponse, dict):
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
        if not isinstance(other, AplazamePayInsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
