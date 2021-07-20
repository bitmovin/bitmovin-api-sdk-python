# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.backup_srt_inputs import BackupSrtInputs
from bitmovin_api_sdk.models.input import Input
from bitmovin_api_sdk.models.srt_mode import SrtMode
import pprint
import six


class SrtInput(Input):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 mode=None,
                 host=None,
                 port=None,
                 path=None,
                 latency=None,
                 passphrase=None,
                 key_length=None,
                 backup_srt_inputs=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, SrtMode, string_types, int, string_types, int, string_types, int, BackupSrtInputs) -> None
        super(SrtInput, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._mode = None
        self._host = None
        self._port = None
        self._path = None
        self._latency = None
        self._passphrase = None
        self._key_length = None
        self._backup_srt_inputs = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if host is not None:
            self.host = host
        if port is not None:
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
    def openapi_types(self):
        types = {}

        if hasattr(super(SrtInput, self), 'openapi_types'):
            types = getattr(super(SrtInput, self), 'openapi_types')

        types.update({
            'mode': 'SrtMode',
            'host': 'string_types',
            'port': 'int',
            'path': 'string_types',
            'latency': 'int',
            'passphrase': 'string_types',
            'key_length': 'int',
            'backup_srt_inputs': 'BackupSrtInputs'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SrtInput, self), 'attribute_map'):
            attributes = getattr(super(SrtInput, self), 'attribute_map')

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

    @property
    def mode(self):
        # type: () -> SrtMode
        """Gets the mode of this SrtInput.

        The SRT mode to use (required)

        :return: The mode of this SrtInput.
        :rtype: SrtMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        # type: (SrtMode) -> None
        """Sets the mode of this SrtInput.

        The SRT mode to use (required)

        :param mode: The mode of this SrtInput.
        :type: SrtMode
        """

        if mode is not None:
            if not isinstance(mode, SrtMode):
                raise TypeError("Invalid type for `mode`, type has to be `SrtMode`")

        self._mode = mode

    @property
    def host(self):
        # type: () -> string_types
        """Gets the host of this SrtInput.

        The name or IP of the host providing the SRT stream (only used in CALLER mode)

        :return: The host of this SrtInput.
        :rtype: string_types
        """
        return self._host

    @host.setter
    def host(self, host):
        # type: (string_types) -> None
        """Sets the host of this SrtInput.

        The name or IP of the host providing the SRT stream (only used in CALLER mode)

        :param host: The host of this SrtInput.
        :type: string_types
        """

        if host is not None:
            if not isinstance(host, string_types):
                raise TypeError("Invalid type for `host`, type has to be `string_types`")

        self._host = host

    @property
    def port(self):
        # type: () -> int
        """Gets the port of this SrtInput.

        The port to connect to or listen on. Has to be one of [2088, 2089, 2090, 2091] when using LISTENER mode. (required)

        :return: The port of this SrtInput.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        # type: (int) -> None
        """Sets the port of this SrtInput.

        The port to connect to or listen on. Has to be one of [2088, 2089, 2090, 2091] when using LISTENER mode. (required)

        :param port: The port of this SrtInput.
        :type: int
        """

        if port is not None:
            if not isinstance(port, int):
                raise TypeError("Invalid type for `port`, type has to be `int`")

        self._port = port

    @property
    def path(self):
        # type: () -> string_types
        """Gets the path of this SrtInput.

        The path parameter of the SRT stream

        :return: The path of this SrtInput.
        :rtype: string_types
        """
        return self._path

    @path.setter
    def path(self, path):
        # type: (string_types) -> None
        """Sets the path of this SrtInput.

        The path parameter of the SRT stream

        :param path: The path of this SrtInput.
        :type: string_types
        """

        if path is not None:
            if not isinstance(path, string_types):
                raise TypeError("Invalid type for `path`, type has to be `string_types`")

        self._path = path

    @property
    def latency(self):
        # type: () -> int
        """Gets the latency of this SrtInput.

        The maximum accepted transmission latency in milliseconds (when both parties set different values, the maximum of the two is used for both)

        :return: The latency of this SrtInput.
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        # type: (int) -> None
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
        # type: () -> string_types
        """Gets the passphrase of this SrtInput.

        The passphrase used to secure the SRT stream. For AES-128 encryption, you must enter a 16-character passphrase; for AES-256, you must enter a 32-character passphrase

        :return: The passphrase of this SrtInput.
        :rtype: string_types
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        # type: (string_types) -> None
        """Sets the passphrase of this SrtInput.

        The passphrase used to secure the SRT stream. For AES-128 encryption, you must enter a 16-character passphrase; for AES-256, you must enter a 32-character passphrase

        :param passphrase: The passphrase of this SrtInput.
        :type: string_types
        """

        if passphrase is not None:
            if not isinstance(passphrase, string_types):
                raise TypeError("Invalid type for `passphrase`, type has to be `string_types`")

        self._passphrase = passphrase

    @property
    def key_length(self):
        # type: () -> int
        """Gets the key_length of this SrtInput.

        The type of AES encryption determines the length of the key (passphrase). AES-128 uses a 16-character (128-bit) passphrase, and AES-256 uses a 32-character (256-bit) passphrase.

        :return: The key_length of this SrtInput.
        :rtype: int
        """
        return self._key_length

    @key_length.setter
    def key_length(self, key_length):
        # type: (int) -> None
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
        # type: () -> BackupSrtInputs
        """Gets the backup_srt_inputs of this SrtInput.


        :return: The backup_srt_inputs of this SrtInput.
        :rtype: BackupSrtInputs
        """
        return self._backup_srt_inputs

    @backup_srt_inputs.setter
    def backup_srt_inputs(self, backup_srt_inputs):
        # type: (BackupSrtInputs) -> None
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
        result = {}

        if hasattr(super(SrtInput, self), "to_dict"):
            result = super(SrtInput, self).to_dict()
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
        if not isinstance(other, SrtInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
