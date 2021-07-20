# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.output import Output
import pprint
import six


class AkamaiNetStorageOutput(Output):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 acl=None,
                 host=None,
                 username=None,
                 password=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[AclEntry], string_types, string_types, string_types) -> None
        super(AkamaiNetStorageOutput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, acl=acl)

        self._host = None
        self._username = None
        self._password = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AkamaiNetStorageOutput, self), 'openapi_types'):
            types = getattr(super(AkamaiNetStorageOutput, self), 'openapi_types')

        types.update({
            'host': 'string_types',
            'username': 'string_types',
            'password': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AkamaiNetStorageOutput, self), 'attribute_map'):
            attributes = getattr(super(AkamaiNetStorageOutput, self), 'attribute_map')

        attributes.update({
            'host': 'host',
            'username': 'username',
            'password': 'password'
        })
        return attributes

    @property
    def host(self):
        # type: () -> string_types
        """Gets the host of this AkamaiNetStorageOutput.

        Host to use for Akamai NetStorage transfers (required)

        :return: The host of this AkamaiNetStorageOutput.
        :rtype: string_types
        """
        return self._host

    @host.setter
    def host(self, host):
        # type: (string_types) -> None
        """Sets the host of this AkamaiNetStorageOutput.

        Host to use for Akamai NetStorage transfers (required)

        :param host: The host of this AkamaiNetStorageOutput.
        :type: string_types
        """

        if host is not None:
            if not isinstance(host, string_types):
                raise TypeError("Invalid type for `host`, type has to be `string_types`")

        self._host = host

    @property
    def username(self):
        # type: () -> string_types
        """Gets the username of this AkamaiNetStorageOutput.

        Your Akamai NetStorage Username (required)

        :return: The username of this AkamaiNetStorageOutput.
        :rtype: string_types
        """
        return self._username

    @username.setter
    def username(self, username):
        # type: (string_types) -> None
        """Sets the username of this AkamaiNetStorageOutput.

        Your Akamai NetStorage Username (required)

        :param username: The username of this AkamaiNetStorageOutput.
        :type: string_types
        """

        if username is not None:
            if not isinstance(username, string_types):
                raise TypeError("Invalid type for `username`, type has to be `string_types`")

        self._username = username

    @property
    def password(self):
        # type: () -> string_types
        """Gets the password of this AkamaiNetStorageOutput.

        Your Akamai NetStorage password (required)

        :return: The password of this AkamaiNetStorageOutput.
        :rtype: string_types
        """
        return self._password

    @password.setter
    def password(self, password):
        # type: (string_types) -> None
        """Sets the password of this AkamaiNetStorageOutput.

        Your Akamai NetStorage password (required)

        :param password: The password of this AkamaiNetStorageOutput.
        :type: string_types
        """

        if password is not None:
            if not isinstance(password, string_types):
                raise TypeError("Invalid type for `password`, type has to be `string_types`")

        self._password = password

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AkamaiNetStorageOutput, self), "to_dict"):
            result = super(AkamaiNetStorageOutput, self).to_dict()
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
        if not isinstance(other, AkamaiNetStorageOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
