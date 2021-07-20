# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input import Input
import pprint
import six


class FtpInput(Input):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 host=None,
                 port=None,
                 passive=None,
                 username=None,
                 password=None,
                 remote_verification_enabled=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, int, bool, string_types, string_types, bool) -> None
        super(FtpInput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._host = None
        self._port = None
        self._passive = None
        self._username = None
        self._password = None
        self._remote_verification_enabled = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if passive is not None:
            self.passive = passive
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if remote_verification_enabled is not None:
            self.remote_verification_enabled = remote_verification_enabled

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(FtpInput, self), 'openapi_types'):
            types = getattr(super(FtpInput, self), 'openapi_types')

        types.update({
            'host': 'string_types',
            'port': 'int',
            'passive': 'bool',
            'username': 'string_types',
            'password': 'string_types',
            'remote_verification_enabled': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(FtpInput, self), 'attribute_map'):
            attributes = getattr(super(FtpInput, self), 'attribute_map')

        attributes.update({
            'host': 'host',
            'port': 'port',
            'passive': 'passive',
            'username': 'username',
            'password': 'password',
            'remote_verification_enabled': 'remoteVerificationEnabled'
        })
        return attributes

    @property
    def host(self):
        # type: () -> string_types
        """Gets the host of this FtpInput.

        Host URL or IP of the FTP server (required)

        :return: The host of this FtpInput.
        :rtype: string_types
        """
        return self._host

    @host.setter
    def host(self, host):
        # type: (string_types) -> None
        """Sets the host of this FtpInput.

        Host URL or IP of the FTP server (required)

        :param host: The host of this FtpInput.
        :type: string_types
        """

        if host is not None:
            if not isinstance(host, string_types):
                raise TypeError("Invalid type for `host`, type has to be `string_types`")

        self._host = host

    @property
    def port(self):
        # type: () -> int
        """Gets the port of this FtpInput.

        Port to use, standard for FTP: 21

        :return: The port of this FtpInput.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        # type: (int) -> None
        """Sets the port of this FtpInput.

        Port to use, standard for FTP: 21

        :param port: The port of this FtpInput.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

        self._port = port

    @property
    def passive(self):
        # type: () -> bool
        """Gets the passive of this FtpInput.

        Use passive mode. Default is true.

        :return: The passive of this FtpInput.
        :rtype: bool
        """
        return self._passive

    @passive.setter
    def passive(self, passive):
        # type: (bool) -> None
        """Sets the passive of this FtpInput.

        Use passive mode. Default is true.

        :param passive: The passive of this FtpInput.
        :type: bool
        """

        if passive is not None:
            if not isinstance(passive, bool):
                raise TypeError("Invalid type for `passive`, type has to be `bool`")

        self._passive = passive

    @property
    def username(self):
        # type: () -> string_types
        """Gets the username of this FtpInput.

        Your FTP Username

        :return: The username of this FtpInput.
        :rtype: string_types
        """
        return self._username

    @username.setter
    def username(self, username):
        # type: (string_types) -> None
        """Sets the username of this FtpInput.

        Your FTP Username

        :param username: The username of this FtpInput.
        :type: string_types
        """

        if username is not None:
            if not isinstance(username, string_types):
                raise TypeError("Invalid type for `username`, type has to be `string_types`")

        self._username = username

    @property
    def password(self):
        # type: () -> string_types
        """Gets the password of this FtpInput.

        Your FTP password

        :return: The password of this FtpInput.
        :rtype: string_types
        """
        return self._password

    @password.setter
    def password(self, password):
        # type: (string_types) -> None
        """Sets the password of this FtpInput.

        Your FTP password

        :param password: The password of this FtpInput.
        :type: string_types
        """

        if password is not None:
            if not isinstance(password, string_types):
                raise TypeError("Invalid type for `password`, type has to be `string_types`")

        self._password = password

    @property
    def remote_verification_enabled(self):
        # type: () -> bool
        """Gets the remote_verification_enabled of this FtpInput.

        Ensure that connections originate from the declared ftp host. Default is true.

        :return: The remote_verification_enabled of this FtpInput.
        :rtype: bool
        """
        return self._remote_verification_enabled

    @remote_verification_enabled.setter
    def remote_verification_enabled(self, remote_verification_enabled):
        # type: (bool) -> None
        """Sets the remote_verification_enabled of this FtpInput.

        Ensure that connections originate from the declared ftp host. Default is true.

        :param remote_verification_enabled: The remote_verification_enabled of this FtpInput.
        :type: bool
        """

        if remote_verification_enabled is not None:
            if not isinstance(remote_verification_enabled, bool):
                raise TypeError("Invalid type for `remote_verification_enabled`, type has to be `bool`")

        self._remote_verification_enabled = remote_verification_enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(FtpInput, self), "to_dict"):
            result = super(FtpInput, self).to_dict()
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
        if not isinstance(other, FtpInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
