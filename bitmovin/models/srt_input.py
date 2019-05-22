# coding: utf-8

from bitmovin.models.backup_srt_inputs import BackupSrtInputs
from bitmovin.models.input import Input
from bitmovin.models.srt_mode import SrtMode
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class SrtInput(Input):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(SrtInput, self).openapi_types
        types.update({
            'mode': 'SrtMode',
            'host': 'str',
            'port': 'int',
            'path': 'str',
            'latency': 'int',
            'passphrase': 'str',
            'key_length': 'int',
            'backup_srt_inputs': 'BackupSrtInputs'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(SrtInput, self).attribute_map
        attributes.update({
            'mode': 'mode',
            'host': 'host',
            'port': 'port',
            'path': 'path',
            'latency': 'latency',
            'passphrase': 'passphrase',
            'key_length': 'keyLength',
            'backup_srt_inputs': 'backupSrtInputs'
        })
        return attributes

    def __init__(self, mode=None, host=None, port=None, path=None, latency=None, passphrase=None, key_length=None, backup_srt_inputs=None, *args, **kwargs):
        super(SrtInput, self).__init__(*args, **kwargs)

        self._mode = None
        self._host = None
        self._port = None
        self._path = None
        self._latency = None
        self._passphrase = None
        self._key_length = None
        self._backup_srt_inputs = None
        self.discriminator = None

        self.mode = mode
        if host is not None:
            self.host = host
        self.port = port
        if path is not None:
            self.path = path
        if latency is not None:
            self.latency = latency
        if passphrase is not None:
            self.passphrase = passphrase
        if key_length is not None:
            self.key_length = key_length
        if backup_srt_inputs is not None:
            self.backup_srt_inputs = backup_srt_inputs

    @property
    def mode(self):
        """Gets the mode of this SrtInput.

        The SRT mode to use

        :return: The mode of this SrtInput.
        :rtype: SrtMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this SrtInput.

        The SRT mode to use

        :param mode: The mode of this SrtInput.
        :type: SrtMode
        """

        if mode is not None:
            if not isinstance(mode, SrtMode):
                raise TypeError("Invalid type for `mode`, type has to be `SrtMode`")

            self._mode = mode


    @property
    def host(self):
        """Gets the host of this SrtInput.

        The name or IP of the host providing the SRT stream (only used in CALLER mode)

        :return: The host of this SrtInput.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SrtInput.

        The name or IP of the host providing the SRT stream (only used in CALLER mode)

        :param host: The host of this SrtInput.
        :type: str
        """

        if host is not None:
            if not isinstance(host, str):
                raise TypeError("Invalid type for `host`, type has to be `str`")

            self._host = host


    @property
    def port(self):
        """Gets the port of this SrtInput.

        The port to connect to or listen on. Has to be one of [2088, 2089, 2090, 2091] when using LISTENER mode.

        :return: The port of this SrtInput.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SrtInput.

        The port to connect to or listen on. Has to be one of [2088, 2089, 2090, 2091] when using LISTENER mode.

        :param port: The port of this SrtInput.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

            self._port = port


    @property
    def path(self):
        """Gets the path of this SrtInput.

        The path parameter of the SRT stream

        :return: The path of this SrtInput.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SrtInput.

        The path parameter of the SRT stream

        :param path: The path of this SrtInput.
        :type: str
        """

        if path is not None:
            if not isinstance(path, str):
                raise TypeError("Invalid type for `path`, type has to be `str`")

            self._path = path


    @property
    def latency(self):
        """Gets the latency of this SrtInput.

        The maximum accepted transmission latency in milliseconds (when both parties set different values, the maximum of the two is used for both)

        :return: The latency of this SrtInput.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this SrtInput.

        The maximum accepted transmission latency in milliseconds (when both parties set different values, the maximum of the two is used for both)

        :param latency: The latency of this SrtInput.
        :type: int
        """

        if latency is not None:
            if not isinstance(latency, int):
                raise TypeError("Invalid type for `latency`, type has to be `int`")

            self._latency = latency


    @property
    def passphrase(self):
        """Gets the passphrase of this SrtInput.

        The passphrase used to secure the SRT stream. For AES-128 encryption, you must enter a 16-character passphrase; for AES-256, you must enter a 32-character passphrase

        :return: The passphrase of this SrtInput.
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """Sets the passphrase of this SrtInput.

        The passphrase used to secure the SRT stream. For AES-128 encryption, you must enter a 16-character passphrase; for AES-256, you must enter a 32-character passphrase

        :param passphrase: The passphrase of this SrtInput.
        :type: str
        """

        if passphrase is not None:
            if not isinstance(passphrase, str):
                raise TypeError("Invalid type for `passphrase`, type has to be `str`")

            self._passphrase = passphrase


    @property
    def key_length(self):
        """Gets the key_length of this SrtInput.

        The type of AES encryption determines the length of the key (passphrase). AES-128 uses a 16-character (128-bit) passphrase, and AES-256 uses a 32-character (256-bit) passphrase.

        :return: The key_length of this SrtInput.
        :rtype: int
        """
        return self._key_length

    @key_length.setter
    def key_length(self, key_length):
        """Sets the key_length of this SrtInput.

        The type of AES encryption determines the length of the key (passphrase). AES-128 uses a 16-character (128-bit) passphrase, and AES-256 uses a 32-character (256-bit) passphrase.

        :param key_length: The key_length of this SrtInput.
        :type: int
        """

        if key_length is not None:
            if not isinstance(key_length, int):
                raise TypeError("Invalid type for `key_length`, type has to be `int`")

            self._key_length = key_length


    @property
    def backup_srt_inputs(self):
        """Gets the backup_srt_inputs of this SrtInput.


        :return: The backup_srt_inputs of this SrtInput.
        :rtype: BackupSrtInputs
        """
        return self._backup_srt_inputs

    @backup_srt_inputs.setter
    def backup_srt_inputs(self, backup_srt_inputs):
        """Sets the backup_srt_inputs of this SrtInput.


        :param backup_srt_inputs: The backup_srt_inputs of this SrtInput.
        :type: BackupSrtInputs
        """

        if backup_srt_inputs is not None:
            if not isinstance(backup_srt_inputs, BackupSrtInputs):
                raise TypeError("Invalid type for `backup_srt_inputs`, type has to be `BackupSrtInputs`")

            self._backup_srt_inputs = backup_srt_inputs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(SrtInput, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(SrtInput, dict):
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
        if not isinstance(other, SrtInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
