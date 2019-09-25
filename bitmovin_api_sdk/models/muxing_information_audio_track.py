# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class MuxingInformationAudioTrack(object):
    @poscheck_model
    def __init__(self,
                 index=None,
                 codec=None,
                 codec_iso=None,
                 bit_rate=None,
                 rate=None,
                 sample_rate=None,
                 channels=None,
                 duration=None):
        # type: (int, string_types, string_types, int, int, int, int, float) -> None

        self._index = None
        self._codec = None
        self._codec_iso = None
        self._bit_rate = None
        self._rate = None
        self._sample_rate = None
        self._channels = None
        self._duration = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if codec is not None:
            self.codec = codec
        if codec_iso is not None:
            self.codec_iso = codec_iso
        if bit_rate is not None:
            self.bit_rate = bit_rate
        if rate is not None:
            self.rate = rate
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if channels is not None:
            self.channels = channels
        if duration is not None:
            self.duration = duration

    @property
    def openapi_types(self):
        types = {
            'index': 'int',
            'codec': 'string_types',
            'codec_iso': 'string_types',
            'bit_rate': 'int',
            'rate': 'int',
            'sample_rate': 'int',
            'channels': 'int',
            'duration': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'index': 'index',
            'codec': 'codec',
            'codec_iso': 'codecIso',
            'bit_rate': 'bitRate',
            'rate': 'rate',
            'sample_rate': 'sampleRate',
            'channels': 'channels',
            'duration': 'duration'
        }
        return attributes

    @property
    def index(self):
        # type: () -> int
        """Gets the index of this MuxingInformationAudioTrack.

        The stream index in the container

        :return: The index of this MuxingInformationAudioTrack.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        # type: (int) -> None
        """Sets the index of this MuxingInformationAudioTrack.

        The stream index in the container

        :param index: The index of this MuxingInformationAudioTrack.
        :type: int
        """

        if index is not None:
            if not isinstance(index, int):
                raise TypeError("Invalid type for `index`, type has to be `int`")

        self._index = index

    @property
    def codec(self):
        # type: () -> string_types
        """Gets the codec of this MuxingInformationAudioTrack.

        The codec used for the track

        :return: The codec of this MuxingInformationAudioTrack.
        :rtype: string_types
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (string_types) -> None
        """Sets the codec of this MuxingInformationAudioTrack.

        The codec used for the track

        :param codec: The codec of this MuxingInformationAudioTrack.
        :type: string_types
        """

        if codec is not None:
            if not isinstance(codec, string_types):
                raise TypeError("Invalid type for `codec`, type has to be `string_types`")

        self._codec = codec

    @property
    def codec_iso(self):
        # type: () -> string_types
        """Gets the codec_iso of this MuxingInformationAudioTrack.

        The codec string of the track

        :return: The codec_iso of this MuxingInformationAudioTrack.
        :rtype: string_types
        """
        return self._codec_iso

    @codec_iso.setter
    def codec_iso(self, codec_iso):
        # type: (string_types) -> None
        """Sets the codec_iso of this MuxingInformationAudioTrack.

        The codec string of the track

        :param codec_iso: The codec_iso of this MuxingInformationAudioTrack.
        :type: string_types
        """

        if codec_iso is not None:
            if not isinstance(codec_iso, string_types):
                raise TypeError("Invalid type for `codec_iso`, type has to be `string_types`")

        self._codec_iso = codec_iso

    @property
    def bit_rate(self):
        # type: () -> int
        """Gets the bit_rate of this MuxingInformationAudioTrack.

        The bitrate of the audio track

        :return: The bit_rate of this MuxingInformationAudioTrack.
        :rtype: int
        """
        return self._bit_rate

    @bit_rate.setter
    def bit_rate(self, bit_rate):
        # type: (int) -> None
        """Sets the bit_rate of this MuxingInformationAudioTrack.

        The bitrate of the audio track

        :param bit_rate: The bit_rate of this MuxingInformationAudioTrack.
        :type: int
        """

        if bit_rate is not None:
            if not isinstance(bit_rate, int):
                raise TypeError("Invalid type for `bit_rate`, type has to be `int`")

        self._bit_rate = bit_rate

    @property
    def rate(self):
        # type: () -> int
        """Gets the rate of this MuxingInformationAudioTrack.


        :return: The rate of this MuxingInformationAudioTrack.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        # type: (int) -> None
        """Sets the rate of this MuxingInformationAudioTrack.


        :param rate: The rate of this MuxingInformationAudioTrack.
        :type: int
        """

        if rate is not None:
            if not isinstance(rate, int):
                raise TypeError("Invalid type for `rate`, type has to be `int`")

        self._rate = rate

    @property
    def sample_rate(self):
        # type: () -> int
        """Gets the sample_rate of this MuxingInformationAudioTrack.

        The sampling rate of the audio stream

        :return: The sample_rate of this MuxingInformationAudioTrack.
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        # type: (int) -> None
        """Sets the sample_rate of this MuxingInformationAudioTrack.

        The sampling rate of the audio stream

        :param sample_rate: The sample_rate of this MuxingInformationAudioTrack.
        :type: int
        """

        if sample_rate is not None:
            if not isinstance(sample_rate, int):
                raise TypeError("Invalid type for `sample_rate`, type has to be `int`")

        self._sample_rate = sample_rate

    @property
    def channels(self):
        # type: () -> int
        """Gets the channels of this MuxingInformationAudioTrack.

        The number of channels in this audio stream

        :return: The channels of this MuxingInformationAudioTrack.
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        # type: (int) -> None
        """Sets the channels of this MuxingInformationAudioTrack.

        The number of channels in this audio stream

        :param channels: The channels of this MuxingInformationAudioTrack.
        :type: int
        """

        if channels is not None:
            if not isinstance(channels, int):
                raise TypeError("Invalid type for `channels`, type has to be `int`")

        self._channels = channels

    @property
    def duration(self):
        # type: () -> float
        """Gets the duration of this MuxingInformationAudioTrack.

        TODO add description

        :return: The duration of this MuxingInformationAudioTrack.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        # type: (float) -> None
        """Sets the duration of this MuxingInformationAudioTrack.

        TODO add description

        :param duration: The duration of this MuxingInformationAudioTrack.
        :type: float
        """

        if duration is not None:
            if not isinstance(duration, (float, int)):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

        self._duration = duration

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
        if not isinstance(other, MuxingInformationAudioTrack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
