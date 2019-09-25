# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AudioMixChannel(object):
    @poscheck_model
    def __init__(self,
                 channel_number=None,
                 source_channels=None):
        # type: (int, list[SourceChannel]) -> None

        self._channel_number = None
        self._source_channels = list()
        self.discriminator = None

        if channel_number is not None:
            self.channel_number = channel_number
        if source_channels is not None:
            self.source_channels = source_channels

    @property
    def openapi_types(self):
        types = {
            'channel_number': 'int',
            'source_channels': 'list[SourceChannel]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'channel_number': 'channelNumber',
            'source_channels': 'sourceChannels'
        }
        return attributes

    @property
    def channel_number(self):
        # type: () -> int
        """Gets the channel_number of this AudioMixChannel.

        Channel number of this mix (starting with 0) (required)

        :return: The channel_number of this AudioMixChannel.
        :rtype: int
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        # type: (int) -> None
        """Sets the channel_number of this AudioMixChannel.

        Channel number of this mix (starting with 0) (required)

        :param channel_number: The channel_number of this AudioMixChannel.
        :type: int
        """

        if channel_number is not None:
            if not isinstance(channel_number, int):
                raise TypeError("Invalid type for `channel_number`, type has to be `int`")

        self._channel_number = channel_number

    @property
    def source_channels(self):
        # type: () -> list[SourceChannel]
        """Gets the source_channels of this AudioMixChannel.

        List of source channels to be mixed (required)

        :return: The source_channels of this AudioMixChannel.
        :rtype: list[SourceChannel]
        """
        return self._source_channels

    @source_channels.setter
    def source_channels(self, source_channels):
        # type: (list) -> None
        """Sets the source_channels of this AudioMixChannel.

        List of source channels to be mixed (required)

        :param source_channels: The source_channels of this AudioMixChannel.
        :type: list[SourceChannel]
        """

        if source_channels is not None:
            if not isinstance(source_channels, list):
                raise TypeError("Invalid type for `source_channels`, type has to be `list[SourceChannel]`")

        self._source_channels = source_channels

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
        if not isinstance(other, AudioMixChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
