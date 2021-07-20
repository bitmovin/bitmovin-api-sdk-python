# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.codec_configuration import CodecConfiguration
import pprint
import six


class AudioConfiguration(CodecConfiguration):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 bitrate=None,
                 rate=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, float) -> None
        super(AudioConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._bitrate = None
        self._rate = None
        self.discriminator = None

        if bitrate is not None:
            self.bitrate = bitrate
        if rate is not None:
            self.rate = rate

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AudioConfiguration, self), 'openapi_types'):
            types = getattr(super(AudioConfiguration, self), 'openapi_types')

        types.update({
            'bitrate': 'int',
            'rate': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AudioConfiguration, self), 'attribute_map'):
            attributes = getattr(super(AudioConfiguration, self), 'attribute_map')

        attributes.update({
            'bitrate': 'bitrate',
            'rate': 'rate'
        })
        return attributes

    @property
    def bitrate(self):
        # type: () -> int
        """Gets the bitrate of this AudioConfiguration.

        Target bitrate for the encoded audio in bps (required)

        :return: The bitrate of this AudioConfiguration.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        # type: (int) -> None
        """Sets the bitrate of this AudioConfiguration.

        Target bitrate for the encoded audio in bps (required)

        :param bitrate: The bitrate of this AudioConfiguration.
        :type: int
        """

        if bitrate is not None:
            if not isinstance(bitrate, int):
                raise TypeError("Invalid type for `bitrate`, type has to be `int`")

        self._bitrate = bitrate

    @property
    def rate(self):
        # type: () -> float
        """Gets the rate of this AudioConfiguration.

        Audio sampling rate in Hz

        :return: The rate of this AudioConfiguration.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        # type: (float) -> None
        """Sets the rate of this AudioConfiguration.

        Audio sampling rate in Hz

        :param rate: The rate of this AudioConfiguration.
        :type: float
        """

        if rate is not None:
            if not isinstance(rate, (float, int)):
                raise TypeError("Invalid type for `rate`, type has to be `float`")

        self._rate = rate

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AudioConfiguration, self), "to_dict"):
            result = super(AudioConfiguration, self).to_dict()
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
        if not isinstance(other, AudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
