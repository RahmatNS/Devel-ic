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
from swagger_client.models.kyc_document_details import KycDocumentDetails  # noqa: F401,E501
from swagger_client.models.telephone import Telephone  # noqa: F401,E501


class KycUserValidationBoardMemberPost(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'birthday': 'int',
        'nationality': 'str',
        'country_of_residence': 'str',
        'telephone': 'Telephone',
        'id_card': 'str',
        'occupation': 'str',
        'id_card_document': 'KycDocumentDetails',
        'address': 'Address'
    }

    attribute_map = {
        'email': 'Email',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'birthday': 'Birthday',
        'nationality': 'Nationality',
        'country_of_residence': 'CountryOfResidence',
        'telephone': 'Telephone',
        'id_card': 'IdCard',
        'occupation': 'Occupation',
        'id_card_document': 'IdCardDocument',
        'address': 'Address'
    }

    def __init__(self, email=None, first_name=None, last_name=None, birthday=None, nationality=None, country_of_residence=None, telephone=None, id_card=None, occupation=None, id_card_document=None, address=None):  # noqa: E501
        """KycUserValidationBoardMemberPost - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._first_name = None
        self._last_name = None
        self._birthday = None
        self._nationality = None
        self._country_of_residence = None
        self._telephone = None
        self._id_card = None
        self._occupation = None
        self._id_card_document = None
        self._address = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if birthday is not None:
            self.birthday = birthday
        if nationality is not None:
            self.nationality = nationality
        if country_of_residence is not None:
            self.country_of_residence = country_of_residence
        if telephone is not None:
            self.telephone = telephone
        if id_card is not None:
            self.id_card = id_card
        if occupation is not None:
            self.occupation = occupation
        if id_card_document is not None:
            self.id_card_document = id_card_document
        if address is not None:
            self.address = address

    @property
    def email(self):
        """Gets the email of this KycUserValidationBoardMemberPost.  # noqa: E501

        The user's email address - must be a valid email  # noqa: E501

        :return: The email of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this KycUserValidationBoardMemberPost.

        The user's email address - must be a valid email  # noqa: E501

        :param email: The email of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this KycUserValidationBoardMemberPost.  # noqa: E501

        The name of the user  # noqa: E501

        :return: The first_name of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this KycUserValidationBoardMemberPost.

        The name of the user  # noqa: E501

        :param first_name: The first_name of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this KycUserValidationBoardMemberPost.  # noqa: E501

        The last name of the user  # noqa: E501

        :return: The last_name of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this KycUserValidationBoardMemberPost.

        The last name of the user  # noqa: E501

        :param last_name: The last_name of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def birthday(self):
        """Gets the birthday of this KycUserValidationBoardMemberPost.  # noqa: E501

        The date of birth of the user - be careful to set the right timezone (should be UTC) to avoid 00h becoming 23h (and hence interpreted as the day before)  # noqa: E501

        :return: The birthday of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: int
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this KycUserValidationBoardMemberPost.

        The date of birth of the user - be careful to set the right timezone (should be UTC) to avoid 00h becoming 23h (and hence interpreted as the day before)  # noqa: E501

        :param birthday: The birthday of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: int
        """

        self._birthday = birthday

    @property
    def nationality(self):
        """Gets the nationality of this KycUserValidationBoardMemberPost.  # noqa: E501

        The user’s nationality. ISO 3166-1 alpha-2 format is expected  # noqa: E501

        :return: The nationality of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this KycUserValidationBoardMemberPost.

        The user’s nationality. ISO 3166-1 alpha-2 format is expected  # noqa: E501

        :param nationality: The nationality of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSpecified", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW"]  # noqa: E501
        if nationality not in allowed_values:
            raise ValueError(
                "Invalid value for `nationality` ({0}), must be one of {1}"  # noqa: E501
                .format(nationality, allowed_values)
            )

        self._nationality = nationality

    @property
    def country_of_residence(self):
        """Gets the country_of_residence of this KycUserValidationBoardMemberPost.  # noqa: E501

        The user’s country of residence. ISO 3166-1 alpha-2 format is expected  # noqa: E501

        :return: The country_of_residence of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: str
        """
        return self._country_of_residence

    @country_of_residence.setter
    def country_of_residence(self, country_of_residence):
        """Sets the country_of_residence of this KycUserValidationBoardMemberPost.

        The user’s country of residence. ISO 3166-1 alpha-2 format is expected  # noqa: E501

        :param country_of_residence: The country_of_residence of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: str
        """
        allowed_values = ["NotSpecified", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW"]  # noqa: E501
        if country_of_residence not in allowed_values:
            raise ValueError(
                "Invalid value for `country_of_residence` ({0}), must be one of {1}"  # noqa: E501
                .format(country_of_residence, allowed_values)
            )

        self._country_of_residence = country_of_residence

    @property
    def telephone(self):
        """Gets the telephone of this KycUserValidationBoardMemberPost.  # noqa: E501


        :return: The telephone of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: Telephone
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this KycUserValidationBoardMemberPost.


        :param telephone: The telephone of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: Telephone
        """

        self._telephone = telephone

    @property
    def id_card(self):
        """Gets the id_card of this KycUserValidationBoardMemberPost.  # noqa: E501


        :return: The id_card of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: str
        """
        return self._id_card

    @id_card.setter
    def id_card(self, id_card):
        """Sets the id_card of this KycUserValidationBoardMemberPost.


        :param id_card: The id_card of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: str
        """

        self._id_card = id_card

    @property
    def occupation(self):
        """Gets the occupation of this KycUserValidationBoardMemberPost.  # noqa: E501


        :return: The occupation of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: str
        """
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        """Sets the occupation of this KycUserValidationBoardMemberPost.


        :param occupation: The occupation of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: str
        """

        self._occupation = occupation

    @property
    def id_card_document(self):
        """Gets the id_card_document of this KycUserValidationBoardMemberPost.  # noqa: E501


        :return: The id_card_document of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: KycDocumentDetails
        """
        return self._id_card_document

    @id_card_document.setter
    def id_card_document(self, id_card_document):
        """Sets the id_card_document of this KycUserValidationBoardMemberPost.


        :param id_card_document: The id_card_document of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: KycDocumentDetails
        """

        self._id_card_document = id_card_document

    @property
    def address(self):
        """Gets the address of this KycUserValidationBoardMemberPost.  # noqa: E501

        The address  # noqa: E501

        :return: The address of this KycUserValidationBoardMemberPost.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this KycUserValidationBoardMemberPost.

        The address  # noqa: E501

        :param address: The address of this KycUserValidationBoardMemberPost.  # noqa: E501
        :type: Address
        """

        self._address = address

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
        if issubclass(KycUserValidationBoardMemberPost, dict):
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
        if not isinstance(other, KycUserValidationBoardMemberPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
