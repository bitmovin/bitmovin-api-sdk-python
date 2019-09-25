# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.output import Output
from bitmovin_api_sdk.models.transfer_version import TransferVersion
import pprint
import six


class FtpOutput(Output):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 acl=None,
                 host=None,
                 port=None,
                 passive=None,
                 username=None,
                 password=None,
                 transfer_version=None,
                 max_concurrent_connections=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, list[AclEntry], string_types, int, bool, string_types, string_types, TransferVersion, int) -> None
        super(FtpOutput, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, acl=acl)

        self._host = None
        self._port = None
        self._passive = None
        self._username = None
        self._password = None
        self._transfer_version = None
        self._max_concurrent_connections = None
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
        if transfer_version is not None:
            self.transfer_version = transfer_version
        if max_concurrent_connections is not None:
            self.max_concurrent_connections = max_concurrent_connections

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(FtpOutput, self), 'openapi_types'):
            types = getattr(super(FtpOutput, self), 'openapi_types')

        types.update({
            'host': 'string_types',
            'port': 'int',
            'passive': 'bool',
            'username': 'string_types',
            'password': 'string_types',
            'transfer_version': 'TransferVersion',
            'max_concurrent_connections': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(FtpOutput, self), 'attribute_map'):
            attributes = getattr(super(FtpOutput, self), 'attribute_map')

        attributes.update({
            'host': 'host',
            'port': 'port',
            'passive': 'passive',
            'username': 'username',
            'password': 'password',
            'transfer_version': 'transferVersion',
            'max_concurrent_connections': 'maxConcurrentConnections'
        })
        return attributes

    @property
    def host(self):
        # type: () -> string_types
        """Gets the host of this FtpOutput.

        Host URL or IP of the FTP server (required)

        :return: The host of this FtpOutput.
        :rtype: string_types
        """
        return self._host

    @host.setter
    def host(self, host):
        # type: (string_types) -> None
        """Sets the host of this FtpOutput.

        Host URL or IP of the FTP server (required)

        :param host: The host of this FtpOutput.
        :type: string_types
        """

        if host is not None:
            if not isinstance(host, string_types):
                raise TypeError("Invalid type for `host`, type has to be `string_types`")

        self._host = host

    @property
    def port(self):
        # type: () -> int
        """Gets the port of this FtpOutput.

        Port to use, standard for FTP: 21

        :return: The port of this FtpOutput.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        # type: (int) -> None
        """Sets the port of this FtpOutput.

        Port to use, standard for FTP: 21

        :param port: The port of this FtpOutput.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

        self._port = port

    @property
    def passive(self):
        # type: () -> bool
        """Gets the passive of this FtpOutput.

        Use passive mode. Default is true.

        :return: The passive of this FtpOutput.
        :rtype: bool
        """
        return self._passive

    @passive.setter
    def passive(self, passive):
        # type: (bool) -> None
        """Sets the passive of this FtpOutput.

        Use passive mode. Default is true.

        :param passive: The passive of this FtpOutput.
        :type: bool
        """

        if passive is not None:
            if not isinstance(passive, bool):
                raise TypeError("Invalid type for `passive`, type has to be `bool`")

        self._passive = passive

    @property
    def username(self):
        # type: () -> string_types
        """Gets the username of this FtpOutput.

        Your FTP Username

        :return: The username of this FtpOutput.
        :rtype: string_types
        """
        return self._username

    @username.setter
    def username(self, username):
        # type: (string_types) -> None
        """Sets the username of this FtpOutput.

        Your FTP Username

        :param username: The username of this FtpOutput.
        :type: string_types
        """

        if username is not None:
            if not isinstance(username, string_types):
                raise TypeError("Invalid type for `username`, type has to be `string_types`")

        self._username = username

    @property
    def password(self):
        # type: () -> string_types
        """Gets the password of this FtpOutput.

        Your FTP password

        :return: The password of this FtpOutput.
        :rtype: string_types
        """
        return self._password

    @password.setter
    def password(self, password):
        # type: (string_types) -> None
        """Sets the password of this FtpOutput.

        Your FTP password

        :param password: The password of this FtpOutput.
        :type: string_types
        """

        if password is not None:
            if not isinstance(password, string_types):
                raise TypeError("Invalid type for `password`, type has to be `string_types`")

        self._password = password

    @property
    def transfer_version(self):
        # type: () -> TransferVersion
        """Gets the transfer_version of this FtpOutput.

        Controls which transfer version should be used

        :return: The transfer_version of this FtpOutput.
        :rtype: TransferVersion
        """
        return self._transfer_version

    @transfer_version.setter
    def transfer_version(self, transfer_version):
        # type: (TransferVersion) -> None
        """Sets the transfer_version of this FtpOutput.

        Controls which transfer version should be used

        :param transfer_version: The transfer_version of this FtpOutput.
        :type: TransferVersion
        """

        if transfer_version is not None:
            if not isinstance(transfer_version, TransferVersion):
                raise TypeError("Invalid type for `transfer_version`, type has to be `TransferVersion`")

        self._transfer_version = transfer_version

    @property
    def max_concurrent_connections(self):
        # type: () -> int
        """Gets the max_concurrent_connections of this FtpOutput.

        Restrict maximum concurrent connections. Requires at least version 1.1.0.

        :return: The max_concurrent_connections of this FtpOutput.
        :rtype: int
        """
        return self._max_concurrent_connections

    @max_concurrent_connections.setter
    def max_concurrent_connections(self, max_concurrent_connections):
        # type: (int) -> None
        """Sets the max_concurrent_connections of this FtpOutput.

        Restrict maximum concurrent connections. Requires at least version 1.1.0.

        :param max_concurrent_connections: The max_concurrent_connections of this FtpOutput.
        :type: int
        """

        if max_concurrent_connections is not None:
            if not isinstance(max_concurrent_connections, int):
                raise TypeError("Invalid type for `max_concurrent_connections`, type has to be `int`")

        self._max_concurrent_connections = max_concurrent_connections

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(FtpOutput, self), "to_dict"):
            result = super(FtpOutput, self).to_dict()
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
        if not isinstance(other, FtpOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
