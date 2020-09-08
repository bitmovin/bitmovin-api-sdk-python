# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_configuration import AudioConfiguration
from bitmovin_api_sdk.models.pcm_channel_layout import PcmChannelLayout
from bitmovin_api_sdk.models.pcm_preset_configuration import PcmPresetConfiguration
from bitmovin_api_sdk.models.pcm_sample_format import PcmSampleFormat
import pprint
import six


class PcmAudioConfiguration(AudioConfiguration):
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
                 preset_configuration=None,
                 channel_layout=None,
                 sample_format=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, int, float, PcmPresetConfiguration, PcmChannelLayout, PcmSampleFormat) -> None
        super(PcmAudioConfiguration, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, bitrate=bitrate, rate=rate)

        self._preset_configuration = None
        self._channel_layout = None
        self._sample_format = None
        self.discriminator = None

        if preset_configuration is not None:
            self.preset_configuration = preset_configuration
        if channel_layout is not None:
            self.channel_layout = channel_layout
        if sample_format is not None:
            self.sample_format = sample_format

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(PcmAudioConfiguration, self), 'openapi_types'):
            types = getattr(super(PcmAudioConfiguration, self), 'openapi_types')

        types.update({
            'preset_configuration': 'PcmPresetConfiguration',
            'channel_layout': 'PcmChannelLayout',
            'sample_format': 'PcmSampleFormat'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(PcmAudioConfiguration, self), 'attribute_map'):
            attributes = getattr(super(PcmAudioConfiguration, self), 'attribute_map')

        attributes.update({
            'preset_configuration': 'presetConfiguration',
            'channel_layout': 'channelLayout',
            'sample_format': 'sampleFormat'
        })
        return attributes

    @property
    def preset_configuration(self):
        # type: () -> PcmPresetConfiguration
        """Gets the preset_configuration of this PcmAudioConfiguration.

        Use a set of well defined configurations preset to support certain use cases. Can be overwritten with more specific values.

        :return: The preset_configuration of this PcmAudioConfiguration.
        :rtype: PcmPresetConfiguration
        """
        return self._preset_configuration

    @preset_configuration.setter
    def preset_configuration(self, preset_configuration):
        # type: (PcmPresetConfiguration) -> None
        """Sets the preset_configuration of this PcmAudioConfiguration.

        Use a set of well defined configurations preset to support certain use cases. Can be overwritten with more specific values.

        :param preset_configuration: The preset_configuration of this PcmAudioConfiguration.
        :type: PcmPresetConfiguration
        """

        if preset_configuration is not None:
            if not isinstance(preset_configuration, PcmPresetConfiguration):
                raise TypeError("Invalid type for `preset_configuration`, type has to be `PcmPresetConfiguration`")

        self._preset_configuration = preset_configuration

    @property
    def channel_layout(self):
        # type: () -> PcmChannelLayout
        """Gets the channel_layout of this PcmAudioConfiguration.

        Channel layout of the audio codec configuration

        :return: The channel_layout of this PcmAudioConfiguration.
        :rtype: PcmChannelLayout
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        # type: (PcmChannelLayout) -> None
        """Sets the channel_layout of this PcmAudioConfiguration.

        Channel layout of the audio codec configuration

        :param channel_layout: The channel_layout of this PcmAudioConfiguration.
        :type: PcmChannelLayout
        """

        if channel_layout is not None:
            if not isinstance(channel_layout, PcmChannelLayout):
                raise TypeError("Invalid type for `channel_layout`, type has to be `PcmChannelLayout`")

        self._channel_layout = channel_layout

    @property
    def sample_format(self):
        # type: () -> PcmSampleFormat
        """Gets the sample_format of this PcmAudioConfiguration.

        Sampling format of the audio codec configuration

        :return: The sample_format of this PcmAudioConfiguration.
        :rtype: PcmSampleFormat
        """
        return self._sample_format

    @sample_format.setter
    def sample_format(self, sample_format):
        # type: (PcmSampleFormat) -> None
        """Sets the sample_format of this PcmAudioConfiguration.

        Sampling format of the audio codec configuration

        :param sample_format: The sample_format of this PcmAudioConfiguration.
        :type: PcmSampleFormat
        """

        if sample_format is not None:
            if not isinstance(sample_format, PcmSampleFormat):
                raise TypeError("Invalid type for `sample_format`, type has to be `PcmSampleFormat`")

        self._sample_format = sample_format

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(PcmAudioConfiguration, self), "to_dict"):
            result = super(PcmAudioConfiguration, self).to_dict()
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
        if not isinstance(other, PcmAudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
