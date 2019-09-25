# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ac3_channel_layout import Ac3ChannelLayout
from bitmovin_api_sdk.models.audio_configuration import AudioConfiguration
import pprint
import six


class Ac3AudioConfiguration(AudioConfiguration):
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
                 channel_layout=None,
                 cutoff_frequency=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, int, float, Ac3ChannelLayout, int) -> None
        super(Ac3AudioConfiguration, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, bitrate=bitrate, rate=rate)

        self._channel_layout = None
        self._cutoff_frequency = None
        self.discriminator = None

        if channel_layout is not None:
            self.channel_layout = channel_layout
        if cutoff_frequency is not None:
            self.cutoff_frequency = cutoff_frequency

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Ac3AudioConfiguration, self), 'openapi_types'):
            types = getattr(super(Ac3AudioConfiguration, self), 'openapi_types')

        types.update({
            'channel_layout': 'Ac3ChannelLayout',
            'cutoff_frequency': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Ac3AudioConfiguration, self), 'attribute_map'):
            attributes = getattr(super(Ac3AudioConfiguration, self), 'attribute_map')

        attributes.update({
            'channel_layout': 'channelLayout',
            'cutoff_frequency': 'cutoffFrequency'
        })
        return attributes

    @property
    def channel_layout(self):
        # type: () -> Ac3ChannelLayout
        """Gets the channel_layout of this Ac3AudioConfiguration.

        Channel layout of the audio codec configuration

        :return: The channel_layout of this Ac3AudioConfiguration.
        :rtype: Ac3ChannelLayout
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        # type: (Ac3ChannelLayout) -> None
        """Sets the channel_layout of this Ac3AudioConfiguration.

        Channel layout of the audio codec configuration

        :param channel_layout: The channel_layout of this Ac3AudioConfiguration.
        :type: Ac3ChannelLayout
        """

        if channel_layout is not None:
            if not isinstance(channel_layout, Ac3ChannelLayout):
                raise TypeError("Invalid type for `channel_layout`, type has to be `Ac3ChannelLayout`")

        self._channel_layout = channel_layout

    @property
    def cutoff_frequency(self):
        # type: () -> int
        """Gets the cutoff_frequency of this Ac3AudioConfiguration.

        The highest frequency that will pass the audio encoder. This value is optional.

        :return: The cutoff_frequency of this Ac3AudioConfiguration.
        :rtype: int
        """
        return self._cutoff_frequency

    @cutoff_frequency.setter
    def cutoff_frequency(self, cutoff_frequency):
        # type: (int) -> None
        """Sets the cutoff_frequency of this Ac3AudioConfiguration.

        The highest frequency that will pass the audio encoder. This value is optional.

        :param cutoff_frequency: The cutoff_frequency of this Ac3AudioConfiguration.
        :type: int
        """

        if cutoff_frequency is not None:
            if not isinstance(cutoff_frequency, int):
                raise TypeError("Invalid type for `cutoff_frequency`, type has to be `int`")

        self._cutoff_frequency = cutoff_frequency

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Ac3AudioConfiguration, self), "to_dict"):
            result = super(Ac3AudioConfiguration, self).to_dict()
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
        if not isinstance(other, Ac3AudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
