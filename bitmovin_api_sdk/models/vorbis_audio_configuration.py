# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_configuration import AudioConfiguration
from bitmovin_api_sdk.models.vorbis_channel_layout import VorbisChannelLayout
import pprint
import six


class VorbisAudioConfiguration(AudioConfiguration):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 bitrate=None,
                 rate=None,
                 channel_layout=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, int, float, VorbisChannelLayout) -> None
        super(VorbisAudioConfiguration, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, bitrate=bitrate, rate=rate)

        self._channel_layout = None
        self.discriminator = None

        if channel_layout is not None:
            self.channel_layout = channel_layout

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(VorbisAudioConfiguration, self), 'openapi_types'):
            types = getattr(super(VorbisAudioConfiguration, self), 'openapi_types')

        types.update({
            'channel_layout': 'VorbisChannelLayout'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(VorbisAudioConfiguration, self), 'attribute_map'):
            attributes = getattr(super(VorbisAudioConfiguration, self), 'attribute_map')

        attributes.update({
            'channel_layout': 'channelLayout'
        })
        return attributes

    @property
    def channel_layout(self):
        # type: () -> VorbisChannelLayout
        """Gets the channel_layout of this VorbisAudioConfiguration.

        Channel layout of the audio codec configuration

        :return: The channel_layout of this VorbisAudioConfiguration.
        :rtype: VorbisChannelLayout
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        # type: (VorbisChannelLayout) -> None
        """Sets the channel_layout of this VorbisAudioConfiguration.

        Channel layout of the audio codec configuration

        :param channel_layout: The channel_layout of this VorbisAudioConfiguration.
        :type: VorbisChannelLayout
        """

        if channel_layout is not None:
            if not isinstance(channel_layout, VorbisChannelLayout):
                raise TypeError("Invalid type for `channel_layout`, type has to be `VorbisChannelLayout`")

        self._channel_layout = channel_layout

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(VorbisAudioConfiguration, self), "to_dict"):
            result = super(VorbisAudioConfiguration, self).to_dict()
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
        if not isinstance(other, VorbisAudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
