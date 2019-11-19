# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class AccountInformation(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 email=None,
                 api_keys=None,
                 first_name=None,
                 last_name=None,
                 phone=None,
                 company=None,
                 is_verified=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, list[AccountApiKey], string_types, string_types, string_types, string_types, bool) -> None
        super(AccountInformation, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._email = None
        self._api_keys = list()
        self._first_name = None
        self._last_name = None
        self._phone = None
        self._company = None
        self._is_verified = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if api_keys is not None:
            self.api_keys = api_keys
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if phone is not None:
            self.phone = phone
        if company is not None:
            self.company = company
        if is_verified is not None:
            self.is_verified = is_verified

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AccountInformation, self), 'openapi_types'):
            types = getattr(super(AccountInformation, self), 'openapi_types')

        types.update({
            'email': 'string_types',
            'api_keys': 'list[AccountApiKey]',
            'first_name': 'string_types',
            'last_name': 'string_types',
            'phone': 'string_types',
            'company': 'string_types',
            'is_verified': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AccountInformation, self), 'attribute_map'):
            attributes = getattr(super(AccountInformation, self), 'attribute_map')

        attributes.update({
            'email': 'email',
            'api_keys': 'apiKeys',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'phone': 'phone',
            'company': 'company',
            'is_verified': 'isVerified'
        })
        return attributes

    @property
    def email(self):
        # type: () -> string_types
        """Gets the email of this AccountInformation.

        Email address of the account. (required)

        :return: The email of this AccountInformation.
        :rtype: string_types
        """
        return self._email

    @email.setter
    def email(self, email):
        # type: (string_types) -> None
        """Sets the email of this AccountInformation.

        Email address of the account. (required)

        :param email: The email of this AccountInformation.
        :type: string_types
        """

        if email is not None:
            if not isinstance(email, string_types):
                raise TypeError("Invalid type for `email`, type has to be `string_types`")

        self._email = email

    @property
    def api_keys(self):
        # type: () -> list[AccountApiKey]
        """Gets the api_keys of this AccountInformation.

        ApiKeys associated with the account (required)

        :return: The api_keys of this AccountInformation.
        :rtype: list[AccountApiKey]
        """
        return self._api_keys

    @api_keys.setter
    def api_keys(self, api_keys):
        # type: (list) -> None
        """Sets the api_keys of this AccountInformation.

        ApiKeys associated with the account (required)

        :param api_keys: The api_keys of this AccountInformation.
        :type: list[AccountApiKey]
        """

        if api_keys is not None:
            if not isinstance(api_keys, list):
                raise TypeError("Invalid type for `api_keys`, type has to be `list[AccountApiKey]`")

        self._api_keys = api_keys

    @property
    def first_name(self):
        # type: () -> string_types
        """Gets the first_name of this AccountInformation.

        First name of the tenant.

        :return: The first_name of this AccountInformation.
        :rtype: string_types
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        # type: (string_types) -> None
        """Sets the first_name of this AccountInformation.

        First name of the tenant.

        :param first_name: The first_name of this AccountInformation.
        :type: string_types
        """

        if first_name is not None:
            if not isinstance(first_name, string_types):
                raise TypeError("Invalid type for `first_name`, type has to be `string_types`")

        self._first_name = first_name

    @property
    def last_name(self):
        # type: () -> string_types
        """Gets the last_name of this AccountInformation.

        Last name of the tenant.

        :return: The last_name of this AccountInformation.
        :rtype: string_types
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        # type: (string_types) -> None
        """Sets the last_name of this AccountInformation.

        Last name of the tenant.

        :param last_name: The last_name of this AccountInformation.
        :type: string_types
        """

        if last_name is not None:
            if not isinstance(last_name, string_types):
                raise TypeError("Invalid type for `last_name`, type has to be `string_types`")

        self._last_name = last_name

    @property
    def phone(self):
        # type: () -> string_types
        """Gets the phone of this AccountInformation.

        Phone number of the tenant.

        :return: The phone of this AccountInformation.
        :rtype: string_types
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        # type: (string_types) -> None
        """Sets the phone of this AccountInformation.

        Phone number of the tenant.

        :param phone: The phone of this AccountInformation.
        :type: string_types
        """

        if phone is not None:
            if not isinstance(phone, string_types):
                raise TypeError("Invalid type for `phone`, type has to be `string_types`")

        self._phone = phone

    @property
    def company(self):
        # type: () -> string_types
        """Gets the company of this AccountInformation.

        Company name of the tenant.

        :return: The company of this AccountInformation.
        :rtype: string_types
        """
        return self._company

    @company.setter
    def company(self, company):
        # type: (string_types) -> None
        """Sets the company of this AccountInformation.

        Company name of the tenant.

        :param company: The company of this AccountInformation.
        :type: string_types
        """

        if company is not None:
            if not isinstance(company, string_types):
                raise TypeError("Invalid type for `company`, type has to be `string_types`")

        self._company = company

    @property
    def is_verified(self):
        # type: () -> bool
        """Gets the is_verified of this AccountInformation.


        :return: The is_verified of this AccountInformation.
        :rtype: bool
        """
        return self._is_verified

    @is_verified.setter
    def is_verified(self, is_verified):
        # type: (bool) -> None
        """Sets the is_verified of this AccountInformation.


        :param is_verified: The is_verified of this AccountInformation.
        :type: bool
        """

        if is_verified is not None:
            if not isinstance(is_verified, bool):
                raise TypeError("Invalid type for `is_verified`, type has to be `bool`")

        self._is_verified = is_verified

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AccountInformation, self), "to_dict"):
            result = super(AccountInformation, self).to_dict()
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
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
        if not isinstance(other, AccountInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
