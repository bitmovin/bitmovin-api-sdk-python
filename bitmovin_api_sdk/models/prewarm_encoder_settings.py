# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.log_level import LogLevel
import pprint
import six


class PrewarmEncoderSettings(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 encoder_version=None,
                 min_prewarmed=None,
                 max_prewarmed=None,
                 log_level=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types, int, int, LogLevel) -> None
        super(PrewarmEncoderSettings, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._encoder_version = None
        self._min_prewarmed = None
        self._max_prewarmed = None
        self._log_level = None
        self.discriminator = None

        if encoder_version is not None:
            self.encoder_version = encoder_version
        if min_prewarmed is not None:
            self.min_prewarmed = min_prewarmed
        if max_prewarmed is not None:
            self.max_prewarmed = max_prewarmed
        if log_level is not None:
            self.log_level = log_level

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(PrewarmEncoderSettings, self), 'openapi_types'):
            types = getattr(super(PrewarmEncoderSettings, self), 'openapi_types')

        types.update({
            'encoder_version': 'string_types',
            'min_prewarmed': 'int',
            'max_prewarmed': 'int',
            'log_level': 'LogLevel'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(PrewarmEncoderSettings, self), 'attribute_map'):
            attributes = getattr(super(PrewarmEncoderSettings, self), 'attribute_map')

        attributes.update({
            'encoder_version': 'encoderVersion',
            'min_prewarmed': 'minPrewarmed',
            'max_prewarmed': 'maxPrewarmed',
            'log_level': 'logLevel'
        })
        return attributes

    @property
    def encoder_version(self):
        # type: () -> string_types
        """Gets the encoder_version of this PrewarmEncoderSettings.

        Encoder Version to be prewarmed. Only one encoder of this version can be prewarmed per cluster. (required)

        :return: The encoder_version of this PrewarmEncoderSettings.
        :rtype: string_types
        """
        return self._encoder_version

    @encoder_version.setter
    def encoder_version(self, encoder_version):
        # type: (string_types) -> None
        """Sets the encoder_version of this PrewarmEncoderSettings.

        Encoder Version to be prewarmed. Only one encoder of this version can be prewarmed per cluster. (required)

        :param encoder_version: The encoder_version of this PrewarmEncoderSettings.
        :type: string_types
        """

        if encoder_version is not None:
            if not isinstance(encoder_version, string_types):
                raise TypeError("Invalid type for `encoder_version`, type has to be `string_types`")

        self._encoder_version = encoder_version

    @property
    def min_prewarmed(self):
        # type: () -> int
        """Gets the min_prewarmed of this PrewarmEncoderSettings.

        The minimum number of prewarmed encoders of this Version (required)

        :return: The min_prewarmed of this PrewarmEncoderSettings.
        :rtype: int
        """
        return self._min_prewarmed

    @min_prewarmed.setter
    def min_prewarmed(self, min_prewarmed):
        # type: (int) -> None
        """Sets the min_prewarmed of this PrewarmEncoderSettings.

        The minimum number of prewarmed encoders of this Version (required)

        :param min_prewarmed: The min_prewarmed of this PrewarmEncoderSettings.
        :type: int
        """

        if min_prewarmed is not None:
            if not isinstance(min_prewarmed, int):
                raise TypeError("Invalid type for `min_prewarmed`, type has to be `int`")

        self._min_prewarmed = min_prewarmed

    @property
    def max_prewarmed(self):
        # type: () -> int
        """Gets the max_prewarmed of this PrewarmEncoderSettings.

        The maximum number of concurrent prewarmed encoders of this Version

        :return: The max_prewarmed of this PrewarmEncoderSettings.
        :rtype: int
        """
        return self._max_prewarmed

    @max_prewarmed.setter
    def max_prewarmed(self, max_prewarmed):
        # type: (int) -> None
        """Sets the max_prewarmed of this PrewarmEncoderSettings.

        The maximum number of concurrent prewarmed encoders of this Version

        :param max_prewarmed: The max_prewarmed of this PrewarmEncoderSettings.
        :type: int
        """

        if max_prewarmed is not None:
            if not isinstance(max_prewarmed, int):
                raise TypeError("Invalid type for `max_prewarmed`, type has to be `int`")

        self._max_prewarmed = max_prewarmed

    @property
    def log_level(self):
        # type: () -> LogLevel
        """Gets the log_level of this PrewarmEncoderSettings.


        :return: The log_level of this PrewarmEncoderSettings.
        :rtype: LogLevel
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        # type: (LogLevel) -> None
        """Sets the log_level of this PrewarmEncoderSettings.


        :param log_level: The log_level of this PrewarmEncoderSettings.
        :type: LogLevel
        """

        if log_level is not None:
            if not isinstance(log_level, LogLevel):
                raise TypeError("Invalid type for `log_level`, type has to be `LogLevel`")

        self._log_level = log_level

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(PrewarmEncoderSettings, self), "to_dict"):
            result = super(PrewarmEncoderSettings, self).to_dict()
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
        if not isinstance(other, PrewarmEncoderSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
