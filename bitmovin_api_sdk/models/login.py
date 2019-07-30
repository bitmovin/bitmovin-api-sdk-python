# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Login(object):
    @poscheck_model
    def __init__(self,
                 e_mail=None,
                 password=None):
        # type: (string_types, string_types) -> None

        self._e_mail = None
        self._password = None
        self.discriminator = None

        if e_mail is not None:
            self.e_mail = e_mail
        if password is not None:
            self.password = password

    @property
    def openapi_types(self):
        types = {
            'e_mail': 'string_types',
            'password': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'e_mail': 'eMail',
            'password': 'password'
        }
        return attributes

    @property
    def e_mail(self):
        # type: () -> string_types
        """Gets the e_mail of this Login.

        Email address of the account. (required)

        :return: The e_mail of this Login.
        :rtype: string_types
        """
        return self._e_mail

    @e_mail.setter
    def e_mail(self, e_mail):
        # type: (string_types) -> None
        """Sets the e_mail of this Login.

        Email address of the account. (required)

        :param e_mail: The e_mail of this Login.
        :type: string_types
        """

        if e_mail is not None:
            if not isinstance(e_mail, string_types):
                raise TypeError("Invalid type for `e_mail`, type has to be `string_types`")

        self._e_mail = e_mail

    @property
    def password(self):
        # type: () -> string_types
        """Gets the password of this Login.

        Password of the account. (required)

        :return: The password of this Login.
        :rtype: string_types
        """
        return self._password

    @password.setter
    def password(self, password):
        # type: (string_types) -> None
        """Sets the password of this Login.

        Password of the account. (required)

        :param password: The password of this Login.
        :type: string_types
        """

        if password is not None:
            if not isinstance(password, string_types):
                raise TypeError("Invalid type for `password`, type has to be `string_types`")

        self._password = password

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Login):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
