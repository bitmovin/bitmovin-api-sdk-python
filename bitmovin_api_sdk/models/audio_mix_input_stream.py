# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_mix_input_channel_layout import AudioMixInputChannelLayout
from bitmovin_api_sdk.models.input_stream import InputStream
import pprint
import six


class AudioMixInputStream(InputStream):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 channel_layout=None,
                 audio_mix_channels=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, AudioMixInputChannelLayout, list[AudioMixInputStreamChannel]) -> None
        super(AudioMixInputStream, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._channel_layout = None
        self._audio_mix_channels = list()
        self.discriminator = None

        if channel_layout is not None:
            self.channel_layout = channel_layout
        if audio_mix_channels is not None:
            self.audio_mix_channels = audio_mix_channels

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AudioMixInputStream, self), 'openapi_types'):
            types = getattr(super(AudioMixInputStream, self), 'openapi_types')

        types.update({
            'channel_layout': 'AudioMixInputChannelLayout',
            'audio_mix_channels': 'list[AudioMixInputStreamChannel]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AudioMixInputStream, self), 'attribute_map'):
            attributes = getattr(super(AudioMixInputStream, self), 'attribute_map')

        attributes.update({
            'channel_layout': 'channelLayout',
            'audio_mix_channels': 'audioMixChannels'
        })
        return attributes

    @property
    def channel_layout(self):
        # type: () -> AudioMixInputChannelLayout
        """Gets the channel_layout of this AudioMixInputStream.

        Channel layout of the audio mix input stream

        :return: The channel_layout of this AudioMixInputStream.
        :rtype: AudioMixInputChannelLayout
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        # type: (AudioMixInputChannelLayout) -> None
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
        # type: () -> list[AudioMixInputStreamChannel]
        """Gets the audio_mix_channels of this AudioMixInputStream.


        :return: The audio_mix_channels of this AudioMixInputStream.
        :rtype: list[AudioMixInputStreamChannel]
        """
        return self._audio_mix_channels

    @audio_mix_channels.setter
    def audio_mix_channels(self, audio_mix_channels):
        # type: (list) -> None
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
        result = {}

        if hasattr(super(AudioMixInputStream, self), "to_dict"):
            result = super(AudioMixInputStream, self).to_dict()
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
        if not isinstance(other, AudioMixInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
