# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input import Input
import pprint
import six


class AsperaInput(Input):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 min_bandwidth=None,
                 max_bandwidth=None,
                 host=None,
                 username=None,
                 password=None,
                 token=None,
                 ssh_port=None,
                 fasp_port=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types, string_types, string_types, string_types, int, int) -> None
        super(AsperaInput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._min_bandwidth = None
        self._max_bandwidth = None
        self._host = None
        self._username = None
        self._password = None
        self._token = None
        self._ssh_port = None
        self._fasp_port = None
        self.discriminator = None

        if min_bandwidth is not None:
            self.min_bandwidth = min_bandwidth
        if max_bandwidth is not None:
            self.max_bandwidth = max_bandwidth
        if host is not None:
            self.host = host
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if token is not None:
            self.token = token
        if ssh_port is not None:
            self.ssh_port = ssh_port
        if fasp_port is not None:
            self.fasp_port = fasp_port

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AsperaInput, self), 'openapi_types'):
            types = getattr(super(AsperaInput, self), 'openapi_types')

        types.update({
            'min_bandwidth': 'string_types',
            'max_bandwidth': 'string_types',
            'host': 'string_types',
            'username': 'string_types',
            'password': 'string_types',
            'token': 'string_types',
            'ssh_port': 'int',
            'fasp_port': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AsperaInput, self), 'attribute_map'):
            attributes = getattr(super(AsperaInput, self), 'attribute_map')

        attributes.update({
            'min_bandwidth': 'minBandwidth',
            'max_bandwidth': 'maxBandwidth',
            'host': 'host',
            'username': 'username',
            'password': 'password',
            'token': 'token',
            'ssh_port': 'sshPort',
            'fasp_port': 'faspPort'
        })
        return attributes

    @property
    def min_bandwidth(self):
        # type: () -> string_types
        """Gets the min_bandwidth of this AsperaInput.

        Minimal download bandwidth. Examples: 100k, 100m, 100g

        :return: The min_bandwidth of this AsperaInput.
        :rtype: string_types
        """
        return self._min_bandwidth

    @min_bandwidth.setter
    def min_bandwidth(self, min_bandwidth):
        # type: (string_types) -> None
        """Sets the min_bandwidth of this AsperaInput.

        Minimal download bandwidth. Examples: 100k, 100m, 100g

        :param min_bandwidth: The min_bandwidth of this AsperaInput.
        :type: string_types
        """

        if min_bandwidth is not None:
            if not isinstance(min_bandwidth, string_types):
                raise TypeError("Invalid type for `min_bandwidth`, type has to be `string_types`")

        self._min_bandwidth = min_bandwidth

    @property
    def max_bandwidth(self):
        # type: () -> string_types
        """Gets the max_bandwidth of this AsperaInput.

        Maximal download bandwidth. Examples: 100k, 100m, 100g

        :return: The max_bandwidth of this AsperaInput.
        :rtype: string_types
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        # type: (string_types) -> None
        """Sets the max_bandwidth of this AsperaInput.

        Maximal download bandwidth. Examples: 100k, 100m, 100g

        :param max_bandwidth: The max_bandwidth of this AsperaInput.
        :type: string_types
        """

        if max_bandwidth is not None:
            if not isinstance(max_bandwidth, string_types):
                raise TypeError("Invalid type for `max_bandwidth`, type has to be `string_types`")

        self._max_bandwidth = max_bandwidth

    @property
    def host(self):
        # type: () -> string_types
        """Gets the host of this AsperaInput.

        Host to use for Aspera transfers (required)

        :return: The host of this AsperaInput.
        :rtype: string_types
        """
        return self._host

    @host.setter
    def host(self, host):
        # type: (string_types) -> None
        """Sets the host of this AsperaInput.

        Host to use for Aspera transfers (required)

        :param host: The host of this AsperaInput.
        :type: string_types
        """

        if host is not None:
            if not isinstance(host, string_types):
                raise TypeError("Invalid type for `host`, type has to be `string_types`")

        self._host = host

    @property
    def username(self):
        # type: () -> string_types
        """Gets the username of this AsperaInput.

        Username to log into Aspera host (either password and user must be set or token)

        :return: The username of this AsperaInput.
        :rtype: string_types
        """
        return self._username

    @username.setter
    def username(self, username):
        # type: (string_types) -> None
        """Sets the username of this AsperaInput.

        Username to log into Aspera host (either password and user must be set or token)

        :param username: The username of this AsperaInput.
        :type: string_types
        """

        if username is not None:
            if not isinstance(username, string_types):
                raise TypeError("Invalid type for `username`, type has to be `string_types`")

        self._username = username

    @property
    def password(self):
        # type: () -> string_types
        """Gets the password of this AsperaInput.

        corresponding password (either password and user must be set or token)

        :return: The password of this AsperaInput.
        :rtype: string_types
        """
        return self._password

    @password.setter
    def password(self, password):
        # type: (string_types) -> None
        """Sets the password of this AsperaInput.

        corresponding password (either password and user must be set or token)

        :param password: The password of this AsperaInput.
        :type: string_types
        """

        if password is not None:
            if not isinstance(password, string_types):
                raise TypeError("Invalid type for `password`, type has to be `string_types`")

        self._password = password

    @property
    def token(self):
        # type: () -> string_types
        """Gets the token of this AsperaInput.

        Token used for authentication (either password and user must be set or token)

        :return: The token of this AsperaInput.
        :rtype: string_types
        """
        return self._token

    @token.setter
    def token(self, token):
        # type: (string_types) -> None
        """Sets the token of this AsperaInput.

        Token used for authentication (either password and user must be set or token)

        :param token: The token of this AsperaInput.
        :type: string_types
        """

        if token is not None:
            if not isinstance(token, string_types):
                raise TypeError("Invalid type for `token`, type has to be `string_types`")

        self._token = token

    @property
    def ssh_port(self):
        # type: () -> int
        """Gets the ssh_port of this AsperaInput.

        Set the TCP port to be used for fasp session initiation

        :return: The ssh_port of this AsperaInput.
        :rtype: int
        """
        return self._ssh_port

    @ssh_port.setter
    def ssh_port(self, ssh_port):
        # type: (int) -> None
        """Sets the ssh_port of this AsperaInput.

        Set the TCP port to be used for fasp session initiation

        :param ssh_port: The ssh_port of this AsperaInput.
        :type: int
        """

        if ssh_port is not None:
            if not isinstance(ssh_port, int):
                raise TypeError("Invalid type for `ssh_port`, type has to be `int`")

        self._ssh_port = ssh_port

    @property
    def fasp_port(self):
        # type: () -> int
        """Gets the fasp_port of this AsperaInput.

        Set the UDP port to be used by fasp for data transfer

        :return: The fasp_port of this AsperaInput.
        :rtype: int
        """
        return self._fasp_port

    @fasp_port.setter
    def fasp_port(self, fasp_port):
        # type: (int) -> None
        """Sets the fasp_port of this AsperaInput.

        Set the UDP port to be used by fasp for data transfer

        :param fasp_port: The fasp_port of this AsperaInput.
        :type: int
        """

        if fasp_port is not None:
            if not isinstance(fasp_port, int):
                raise TypeError("Invalid type for `fasp_port`, type has to be `int`")

        self._fasp_port = fasp_port

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AsperaInput, self), "to_dict"):
            result = super(AsperaInput, self).to_dict()
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
        if not isinstance(other, AsperaInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
