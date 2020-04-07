# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_mix_source_channel_type import AudioMixSourceChannelType
import pprint
import six


class AudioMixInputStreamSourceChannel(object):
    @poscheck_model
    def __init__(self,
                 gain=None,
                 type_=None,
                 channel_number=None):
        # type: (float, AudioMixSourceChannelType, int) -> None

        self._gain = None
        self._type = None
        self._channel_number = None
        self.discriminator = None

        if gain is not None:
            self.gain = gain
        if type_ is not None:
            self.type = type_
        if channel_number is not None:
            self.channel_number = channel_number

    @property
    def openapi_types(self):
        types = {
            'gain': 'float',
            'type': 'AudioMixSourceChannelType',
            'channel_number': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'gain': 'gain',
            'type': 'type',
            'channel_number': 'channelNumber'
        }
        return attributes

    @property
    def gain(self):
        # type: () -> float
        """Gets the gain of this AudioMixInputStreamSourceChannel.

        Gain for this source channel. Default is 1.0.

        :return: The gain of this AudioMixInputStreamSourceChannel.
        :rtype: float
        """
        return self._gain

    @gain.setter
    def gain(self, gain):
        # type: (float) -> None
        """Sets the gain of this AudioMixInputStreamSourceChannel.

        Gain for this source channel. Default is 1.0.

        :param gain: The gain of this AudioMixInputStreamSourceChannel.
        :type: float
        """

        if gain is not None:
            if not isinstance(gain, (float, int)):
                raise TypeError("Invalid type for `gain`, type has to be `float`")

        self._gain = gain

    @property
    def type(self):
        # type: () -> AudioMixSourceChannelType
        """Gets the type of this AudioMixInputStreamSourceChannel.


        :return: The type of this AudioMixInputStreamSourceChannel.
        :rtype: AudioMixSourceChannelType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (AudioMixSourceChannelType) -> None
        """Sets the type of this AudioMixInputStreamSourceChannel.


        :param type_: The type of this AudioMixInputStreamSourceChannel.
        :type: AudioMixSourceChannelType
        """

        if type_ is not None:
            if not isinstance(type_, AudioMixSourceChannelType):
                raise TypeError("Invalid type for `type`, type has to be `AudioMixSourceChannelType`")

        self._type = type_

    @property
    def channel_number(self):
        # type: () -> int
        """Gets the channel_number of this AudioMixInputStreamSourceChannel.

        Number of this source channel. If type is 'CHANNEL_NUMBER', this must be set.

        :return: The channel_number of this AudioMixInputStreamSourceChannel.
        :rtype: int
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        # type: (int) -> None
        """Sets the channel_number of this AudioMixInputStreamSourceChannel.

        Number of this source channel. If type is 'CHANNEL_NUMBER', this must be set.

        :param channel_number: The channel_number of this AudioMixInputStreamSourceChannel.
        :type: int
        """

        if channel_number is not None:
            if not isinstance(channel_number, int):
                raise TypeError("Invalid type for `channel_number`, type has to be `int`")

        self._channel_number = channel_number

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
        if not isinstance(other, AudioMixInputStreamSourceChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
