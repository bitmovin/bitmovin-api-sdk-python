# coding: utf-8

from bitmovin.models.audio_mix_input_channel_layout import AudioMixInputChannelLayout
from bitmovin.models.audio_mix_input_stream_channel import AudioMixInputStreamChannel
from bitmovin.models.basic_input_stream import BasicInputStream
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioMixInputStream(BasicInputStream):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(AudioMixInputStream, self).openapi_types
        types.update({
            'channel_layout': 'AudioMixInputChannelLayout',
            'audio_mix_channels': 'list[AudioMixInputStreamChannel]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(AudioMixInputStream, self).attribute_map
        attributes.update({
            'channel_layout': 'channelLayout',
            'audio_mix_channels': 'audioMixChannels'
        })
        return attributes

    def __init__(self, channel_layout=None, audio_mix_channels=None, *args, **kwargs):
        super(AudioMixInputStream, self).__init__(*args, **kwargs)

        self._channel_layout = None
        self._audio_mix_channels = None
        self.discriminator = None

        if channel_layout is not None:
            self.channel_layout = channel_layout
        if audio_mix_channels is not None:
            self.audio_mix_channels = audio_mix_channels

    @property
    def channel_layout(self):
        """Gets the channel_layout of this AudioMixInputStream.

        Channel layout of the audio mix input stream

        :return: The channel_layout of this AudioMixInputStream.
        :rtype: AudioMixInputChannelLayout
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        """Sets the channel_layout of this AudioMixInputStream.

        Channel layout of the audio mix input stream

        :param channel_layout: The channel_layout of this AudioMixInputStream.
        :type: AudioMixInputChannelLayout
        """

        if channel_layout is not None:
            if not isinstance(channel_layout, AudioMixInputChannelLayout):
                raise TypeError("Invalid type for `channel_layout`, type has to be `AudioMixInputChannelLayout`")

            self._channel_layout = channel_layout


    @property
    def audio_mix_channels(self):
        """Gets the audio_mix_channels of this AudioMixInputStream.


        :return: The audio_mix_channels of this AudioMixInputStream.
        :rtype: list[AudioMixInputStreamChannel]
        """
        return self._audio_mix_channels

    @audio_mix_channels.setter
    def audio_mix_channels(self, audio_mix_channels):
        """Sets the audio_mix_channels of this AudioMixInputStream.


        :param audio_mix_channels: The audio_mix_channels of this AudioMixInputStream.
        :type: list[AudioMixInputStreamChannel]
        """

        if audio_mix_channels is not None:
            if not isinstance(audio_mix_channels, list):
                raise TypeError("Invalid type for `audio_mix_channels`, type has to be `list[AudioMixInputStreamChannel]`")

            self._audio_mix_channels = audio_mix_channels

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(AudioMixInputStream, self).to_dict()

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
            if issubclass(AudioMixInputStream, dict):
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
        if not isinstance(other, AudioMixInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
