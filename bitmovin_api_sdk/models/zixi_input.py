# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input import Input
import pprint
import six


class ZixiInput(Input):
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
                 stream=None,
                 password=None,
                 latency=None,
                 min_bitrate=None,
                 decryption_type=None,
                 decryption_key=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, int, string_types, string_types, int, int, string_types, string_types) -> None
        super(ZixiInput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._host = None
        self._port = None
        self._stream = None
        self._password = None
        self._latency = None
        self._min_bitrate = None
        self._decryption_type = None
        self._decryption_key = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if stream is not None:
            self.stream = stream
        if password is not None:
            self.password = password
        if latency is not None:
            self.latency = latency
        if min_bitrate is not None:
            self.min_bitrate = min_bitrate
        if decryption_type is not None:
            self.decryption_type = decryption_type
        if decryption_key is not None:
            self.decryption_key = decryption_key

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ZixiInput, self), 'openapi_types'):
            types = getattr(super(ZixiInput, self), 'openapi_types')

        types.update({
            'host': 'string_types',
            'port': 'int',
            'stream': 'string_types',
            'password': 'string_types',
            'latency': 'int',
            'min_bitrate': 'int',
            'decryption_type': 'string_types',
            'decryption_key': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ZixiInput, self), 'attribute_map'):
            attributes = getattr(super(ZixiInput, self), 'attribute_map')

        attributes.update({
            'host': 'host',
            'port': 'port',
            'stream': 'stream',
            'password': 'password',
            'latency': 'latency',
            'min_bitrate': 'minBitrate',
            'decryption_type': 'decryptionType',
            'decryption_key': 'decryptionKey'
        })
        return attributes

    @property
    def host(self):
        # type: () -> string_types
        """Gets the host of this ZixiInput.


        :return: The host of this ZixiInput.
        :rtype: string_types
        """
        return self._host

    @host.setter
    def host(self, host):
        # type: (string_types) -> None
        """Sets the host of this ZixiInput.


        :param host: The host of this ZixiInput.
        :type: string_types
        """

        if host is not None:
            if not isinstance(host, string_types):
                raise TypeError("Invalid type for `host`, type has to be `string_types`")

        self._host = host

    @property
    def port(self):
        # type: () -> int
        """Gets the port of this ZixiInput.


        :return: The port of this ZixiInput.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        # type: (int) -> None
        """Sets the port of this ZixiInput.


        :param port: The port of this ZixiInput.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

        self._port = port

    @property
    def stream(self):
        # type: () -> string_types
        """Gets the stream of this ZixiInput.


        :return: The stream of this ZixiInput.
        :rtype: string_types
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        # type: (string_types) -> None
        """Sets the stream of this ZixiInput.


        :param stream: The stream of this ZixiInput.
        :type: string_types
        """

        if stream is not None:
            if not isinstance(stream, string_types):
                raise TypeError("Invalid type for `stream`, type has to be `string_types`")

        self._stream = stream

    @property
    def password(self):
        # type: () -> string_types
        """Gets the password of this ZixiInput.


        :return: The password of this ZixiInput.
        :rtype: string_types
        """
        return self._password

    @password.setter
    def password(self, password):
        # type: (string_types) -> None
        """Sets the password of this ZixiInput.


        :param password: The password of this ZixiInput.
        :type: string_types
        """

        if password is not None:
            if not isinstance(password, string_types):
                raise TypeError("Invalid type for `password`, type has to be `string_types`")

        self._password = password

    @property
    def latency(self):
        # type: () -> int
        """Gets the latency of this ZixiInput.


        :return: The latency of this ZixiInput.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        # type: (int) -> None
        """Sets the latency of this ZixiInput.


        :param latency: The latency of this ZixiInput.
        :type: int
        """

        if latency is not None:
            if not isinstance(latency, int):
                raise TypeError("Invalid type for `latency`, type has to be `int`")

        self._latency = latency

    @property
    def min_bitrate(self):
        # type: () -> int
        """Gets the min_bitrate of this ZixiInput.


        :return: The min_bitrate of this ZixiInput.
        :rtype: int
        """
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, min_bitrate):
        # type: (int) -> None
        """Sets the min_bitrate of this ZixiInput.


        :param min_bitrate: The min_bitrate of this ZixiInput.
        :type: int
        """

        if min_bitrate is not None:
            if not isinstance(min_bitrate, int):
                raise TypeError("Invalid type for `min_bitrate`, type has to be `int`")

        self._min_bitrate = min_bitrate

    @property
    def decryption_type(self):
        # type: () -> string_types
        """Gets the decryption_type of this ZixiInput.


        :return: The decryption_type of this ZixiInput.
        :rtype: string_types
        """
        return self._decryption_type

    @decryption_type.setter
    def decryption_type(self, decryption_type):
        # type: (string_types) -> None
        """Sets the decryption_type of this ZixiInput.


        :param decryption_type: The decryption_type of this ZixiInput.
        :type: string_types
        """

        if decryption_type is not None:
            if not isinstance(decryption_type, string_types):
                raise TypeError("Invalid type for `decryption_type`, type has to be `string_types`")

        self._decryption_type = decryption_type

    @property
    def decryption_key(self):
        # type: () -> string_types
        """Gets the decryption_key of this ZixiInput.


        :return: The decryption_key of this ZixiInput.
        :rtype: string_types
        """
        return self._decryption_key

    @decryption_key.setter
    def decryption_key(self, decryption_key):
        # type: (string_types) -> None
        """Sets the decryption_key of this ZixiInput.


        :param decryption_key: The decryption_key of this ZixiInput.
        :type: string_types
        """

        if decryption_key is not None:
            if not isinstance(decryption_key, string_types):
                raise TypeError("Invalid type for `decryption_key`, type has to be `string_types`")

        self._decryption_key = decryption_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ZixiInput, self), "to_dict"):
            result = super(ZixiInput, self).to_dict()
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
        if not isinstance(other, ZixiInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
