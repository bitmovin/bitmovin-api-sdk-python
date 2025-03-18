# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PoisEndpointCredentials(object):
    @poscheck_model
    def __init__(self,
                 username=None,
                 password=None):
        # type: (string_types, string_types) -> None

        self._username = None
        self._password = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def openapi_types(self):
        types = {
            'username': 'string_types',
            'password': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'username': 'username',
            'password': 'password'
        }
        return attributes

    @property
    def username(self):
        # type: () -> string_types
        """Gets the username of this PoisEndpointCredentials.

        The username required to authenticate with the POIS server. 

        :return: The username of this PoisEndpointCredentials.
        :rtype: string_types
        """
        return self._username

    @username.setter
    def username(self, username):
        # type: (string_types) -> None
        """Sets the username of this PoisEndpointCredentials.

        The username required to authenticate with the POIS server. 

        :param username: The username of this PoisEndpointCredentials.
        :type: string_types
        """

        if username is not None:
            if not isinstance(username, string_types):
                raise TypeError("Invalid type for `username`, type has to be `string_types`")

        self._username = username

    @property
    def password(self):
        # type: () -> string_types
        """Gets the password of this PoisEndpointCredentials.

        The password required for authentication with the POIS server. 

        :return: The password of this PoisEndpointCredentials.
        :rtype: string_types
        """
        return self._password

    @password.setter
    def password(self, password):
        # type: (string_types) -> None
        """Sets the password of this PoisEndpointCredentials.

        The password required for authentication with the POIS server. 

        :param password: The password of this PoisEndpointCredentials.
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
        if not isinstance(other, PoisEndpointCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
