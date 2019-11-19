# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.media_stream import MediaStream
import pprint
import six


class AudioStream(MediaStream):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 position=None,
                 duration=None,
                 codec=None,
                 sample_rate=None,
                 bitrate=None,
                 rate=None,
                 channel_format=None,
                 language=None,
                 hearing_impaired=None):
        # type: (string_types, int, float, string_types, int, string_types, int, string_types, string_types, bool) -> None
        super(AudioStream, self).__init__(id_=id_, position=position, duration=duration, codec=codec)

        self._sample_rate = None
        self._bitrate = None
        self._rate = None
        self._channel_format = None
        self._language = None
        self._hearing_impaired = None
        self.discriminator = None

        if sample_rate is not None:
            self.sample_rate = sample_rate
        if bitrate is not None:
            self.bitrate = bitrate
        if rate is not None:
            self.rate = rate
        if channel_format is not None:
            self.channel_format = channel_format
        if language is not None:
            self.language = language
        if hearing_impaired is not None:
            self.hearing_impaired = hearing_impaired

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AudioStream, self), 'openapi_types'):
            types = getattr(super(AudioStream, self), 'openapi_types')

        types.update({
            'sample_rate': 'int',
            'bitrate': 'string_types',
            'rate': 'int',
            'channel_format': 'string_types',
            'language': 'string_types',
            'hearing_impaired': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AudioStream, self), 'attribute_map'):
            attributes = getattr(super(AudioStream, self), 'attribute_map')

        attributes.update({
            'sample_rate': 'sampleRate',
            'bitrate': 'bitrate',
            'rate': 'rate',
            'channel_format': 'channelFormat',
            'language': 'language',
            'hearing_impaired': 'hearingImpaired'
        })
        return attributes

    @property
    def sample_rate(self):
        # type: () -> int
        """Gets the sample_rate of this AudioStream.

        Audio sampling rate in Hz

        :return: The sample_rate of this AudioStream.
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        # type: (int) -> None
        """Sets the sample_rate of this AudioStream.

        Audio sampling rate in Hz

        :param sample_rate: The sample_rate of this AudioStream.
        :type: int
        """

        if sample_rate is not None:
            if not isinstance(sample_rate, int):
                raise TypeError("Invalid type for `sample_rate`, type has to be `int`")

        self._sample_rate = sample_rate

    @property
    def bitrate(self):
        # type: () -> string_types
        """Gets the bitrate of this AudioStream.

        Bitrate in bps

        :return: The bitrate of this AudioStream.
        :rtype: string_types
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        # type: (string_types) -> None
        """Sets the bitrate of this AudioStream.

        Bitrate in bps

        :param bitrate: The bitrate of this AudioStream.
        :type: string_types
        """

        if bitrate is not None:
            if not isinstance(bitrate, string_types):
                raise TypeError("Invalid type for `bitrate`, type has to be `string_types`")

        self._bitrate = bitrate

    @property
    def rate(self):
        # type: () -> int
        """Gets the rate of this AudioStream.

        Bitrate in bps

        :return: The rate of this AudioStream.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        # type: (int) -> None
        """Sets the rate of this AudioStream.

        Bitrate in bps

        :param rate: The rate of this AudioStream.
        :type: int
        """

        if rate is not None:
            if not isinstance(rate, int):
                raise TypeError("Invalid type for `rate`, type has to be `int`")

        self._rate = rate

    @property
    def channel_format(self):
        # type: () -> string_types
        """Gets the channel_format of this AudioStream.

        Audio channel format

        :return: The channel_format of this AudioStream.
        :rtype: string_types
        """
        return self._channel_format

    @channel_format.setter
    def channel_format(self, channel_format):
        # type: (string_types) -> None
        """Sets the channel_format of this AudioStream.

        Audio channel format

        :param channel_format: The channel_format of this AudioStream.
        :type: string_types
        """

        if channel_format is not None:
            if not isinstance(channel_format, string_types):
                raise TypeError("Invalid type for `channel_format`, type has to be `string_types`")

        self._channel_format = channel_format

    @property
    def language(self):
        # type: () -> string_types
        """Gets the language of this AudioStream.

        Language of the stream

        :return: The language of this AudioStream.
        :rtype: string_types
        """
        return self._language

    @language.setter
    def language(self, language):
        # type: (string_types) -> None
        """Sets the language of this AudioStream.

        Language of the stream

        :param language: The language of this AudioStream.
        :type: string_types
        """

        if language is not None:
            if not isinstance(language, string_types):
                raise TypeError("Invalid type for `language`, type has to be `string_types`")

        self._language = language

    @property
    def hearing_impaired(self):
        # type: () -> bool
        """Gets the hearing_impaired of this AudioStream.

        Hearing impaired support

        :return: The hearing_impaired of this AudioStream.
        :rtype: bool
        """
        return self._hearing_impaired

    @hearing_impaired.setter
    def hearing_impaired(self, hearing_impaired):
        # type: (bool) -> None
        """Sets the hearing_impaired of this AudioStream.

        Hearing impaired support

        :param hearing_impaired: The hearing_impaired of this AudioStream.
        :type: bool
        """

        if hearing_impaired is not None:
            if not isinstance(hearing_impaired, bool):
                raise TypeError("Invalid type for `hearing_impaired`, type has to be `bool`")

        self._hearing_impaired = hearing_impaired

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AudioStream, self), "to_dict"):
            result = super(AudioStream, self).to_dict()
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
        if not isinstance(other, AudioStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
