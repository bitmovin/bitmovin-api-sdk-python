# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_configuration import AudioConfiguration
from bitmovin_api_sdk.models.dolby_digital_plus_bitstream_info import DolbyDigitalPlusBitstreamInfo
from bitmovin_api_sdk.models.dolby_digital_plus_channel_layout import DolbyDigitalPlusChannelLayout
from bitmovin_api_sdk.models.dolby_digital_plus_downmixing import DolbyDigitalPlusDownmixing
from bitmovin_api_sdk.models.dolby_digital_plus_evolution_framework_control import DolbyDigitalPlusEvolutionFrameworkControl
from bitmovin_api_sdk.models.dolby_digital_plus_loudness_control import DolbyDigitalPlusLoudnessControl
from bitmovin_api_sdk.models.dolby_digital_plus_preprocessing import DolbyDigitalPlusPreprocessing
import pprint
import six


class DolbyDigitalPlusAudioConfiguration(AudioConfiguration):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 bitrate=None,
                 rate=None,
                 bitstream_info=None,
                 channel_layout=None,
                 downmixing=None,
                 evolution_framework_control=None,
                 loudness_control=None,
                 preprocessing=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, float, DolbyDigitalPlusBitstreamInfo, DolbyDigitalPlusChannelLayout, DolbyDigitalPlusDownmixing, DolbyDigitalPlusEvolutionFrameworkControl, DolbyDigitalPlusLoudnessControl, DolbyDigitalPlusPreprocessing) -> None
        super(DolbyDigitalPlusAudioConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, bitrate=bitrate, rate=rate)

        self._bitstream_info = None
        self._channel_layout = None
        self._downmixing = None
        self._evolution_framework_control = None
        self._loudness_control = None
        self._preprocessing = None
        self.discriminator = None

        if bitstream_info is not None:
            self.bitstream_info = bitstream_info
        if channel_layout is not None:
            self.channel_layout = channel_layout
        if downmixing is not None:
            self.downmixing = downmixing
        if evolution_framework_control is not None:
            self.evolution_framework_control = evolution_framework_control
        if loudness_control is not None:
            self.loudness_control = loudness_control
        if preprocessing is not None:
            self.preprocessing = preprocessing

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DolbyDigitalPlusAudioConfiguration, self), 'openapi_types'):
            types = getattr(super(DolbyDigitalPlusAudioConfiguration, self), 'openapi_types')

        types.update({
            'bitstream_info': 'DolbyDigitalPlusBitstreamInfo',
            'channel_layout': 'DolbyDigitalPlusChannelLayout',
            'downmixing': 'DolbyDigitalPlusDownmixing',
            'evolution_framework_control': 'DolbyDigitalPlusEvolutionFrameworkControl',
            'loudness_control': 'DolbyDigitalPlusLoudnessControl',
            'preprocessing': 'DolbyDigitalPlusPreprocessing'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DolbyDigitalPlusAudioConfiguration, self), 'attribute_map'):
            attributes = getattr(super(DolbyDigitalPlusAudioConfiguration, self), 'attribute_map')

        attributes.update({
            'bitstream_info': 'bitstreamInfo',
            'channel_layout': 'channelLayout',
            'downmixing': 'downmixing',
            'evolution_framework_control': 'evolutionFrameworkControl',
            'loudness_control': 'loudnessControl',
            'preprocessing': 'preprocessing'
        })
        return attributes

    @property
    def bitstream_info(self):
        # type: () -> DolbyDigitalPlusBitstreamInfo
        """Gets the bitstream_info of this DolbyDigitalPlusAudioConfiguration.

        BitstreamInfo defines metadata parameters contained in the Dolby Digital Plus audio bitstream

        :return: The bitstream_info of this DolbyDigitalPlusAudioConfiguration.
        :rtype: DolbyDigitalPlusBitstreamInfo
        """
        return self._bitstream_info

    @bitstream_info.setter
    def bitstream_info(self, bitstream_info):
        # type: (DolbyDigitalPlusBitstreamInfo) -> None
        """Sets the bitstream_info of this DolbyDigitalPlusAudioConfiguration.

        BitstreamInfo defines metadata parameters contained in the Dolby Digital Plus audio bitstream

        :param bitstream_info: The bitstream_info of this DolbyDigitalPlusAudioConfiguration.
        :type: DolbyDigitalPlusBitstreamInfo
        """

        if bitstream_info is not None:
            if not isinstance(bitstream_info, DolbyDigitalPlusBitstreamInfo):
                raise TypeError("Invalid type for `bitstream_info`, type has to be `DolbyDigitalPlusBitstreamInfo`")

        self._bitstream_info = bitstream_info

    @property
    def channel_layout(self):
        # type: () -> DolbyDigitalPlusChannelLayout
        """Gets the channel_layout of this DolbyDigitalPlusAudioConfiguration.

        Channel layout of the audio codec configuration.

        :return: The channel_layout of this DolbyDigitalPlusAudioConfiguration.
        :rtype: DolbyDigitalPlusChannelLayout
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        # type: (DolbyDigitalPlusChannelLayout) -> None
        """Sets the channel_layout of this DolbyDigitalPlusAudioConfiguration.

        Channel layout of the audio codec configuration.

        :param channel_layout: The channel_layout of this DolbyDigitalPlusAudioConfiguration.
        :type: DolbyDigitalPlusChannelLayout
        """

        if channel_layout is not None:
            if not isinstance(channel_layout, DolbyDigitalPlusChannelLayout):
                raise TypeError("Invalid type for `channel_layout`, type has to be `DolbyDigitalPlusChannelLayout`")

        self._channel_layout = channel_layout

    @property
    def downmixing(self):
        # type: () -> DolbyDigitalPlusDownmixing
        """Gets the downmixing of this DolbyDigitalPlusAudioConfiguration.


        :return: The downmixing of this DolbyDigitalPlusAudioConfiguration.
        :rtype: DolbyDigitalPlusDownmixing
        """
        return self._downmixing

    @downmixing.setter
    def downmixing(self, downmixing):
        # type: (DolbyDigitalPlusDownmixing) -> None
        """Sets the downmixing of this DolbyDigitalPlusAudioConfiguration.


        :param downmixing: The downmixing of this DolbyDigitalPlusAudioConfiguration.
        :type: DolbyDigitalPlusDownmixing
        """

        if downmixing is not None:
            if not isinstance(downmixing, DolbyDigitalPlusDownmixing):
                raise TypeError("Invalid type for `downmixing`, type has to be `DolbyDigitalPlusDownmixing`")

        self._downmixing = downmixing

    @property
    def evolution_framework_control(self):
        # type: () -> DolbyDigitalPlusEvolutionFrameworkControl
        """Gets the evolution_framework_control of this DolbyDigitalPlusAudioConfiguration.

        It provides a framework for signaling new evolution framework applications, such as Intelligent Loudness, in each Dolby codec. 

        :return: The evolution_framework_control of this DolbyDigitalPlusAudioConfiguration.
        :rtype: DolbyDigitalPlusEvolutionFrameworkControl
        """
        return self._evolution_framework_control

    @evolution_framework_control.setter
    def evolution_framework_control(self, evolution_framework_control):
        # type: (DolbyDigitalPlusEvolutionFrameworkControl) -> None
        """Sets the evolution_framework_control of this DolbyDigitalPlusAudioConfiguration.

        It provides a framework for signaling new evolution framework applications, such as Intelligent Loudness, in each Dolby codec. 

        :param evolution_framework_control: The evolution_framework_control of this DolbyDigitalPlusAudioConfiguration.
        :type: DolbyDigitalPlusEvolutionFrameworkControl
        """

        if evolution_framework_control is not None:
            if not isinstance(evolution_framework_control, DolbyDigitalPlusEvolutionFrameworkControl):
                raise TypeError("Invalid type for `evolution_framework_control`, type has to be `DolbyDigitalPlusEvolutionFrameworkControl`")

        self._evolution_framework_control = evolution_framework_control

    @property
    def loudness_control(self):
        # type: () -> DolbyDigitalPlusLoudnessControl
        """Gets the loudness_control of this DolbyDigitalPlusAudioConfiguration.

        Settings for loudness control (required)

        :return: The loudness_control of this DolbyDigitalPlusAudioConfiguration.
        :rtype: DolbyDigitalPlusLoudnessControl
        """
        return self._loudness_control

    @loudness_control.setter
    def loudness_control(self, loudness_control):
        # type: (DolbyDigitalPlusLoudnessControl) -> None
        """Sets the loudness_control of this DolbyDigitalPlusAudioConfiguration.

        Settings for loudness control (required)

        :param loudness_control: The loudness_control of this DolbyDigitalPlusAudioConfiguration.
        :type: DolbyDigitalPlusLoudnessControl
        """

        if loudness_control is not None:
            if not isinstance(loudness_control, DolbyDigitalPlusLoudnessControl):
                raise TypeError("Invalid type for `loudness_control`, type has to be `DolbyDigitalPlusLoudnessControl`")

        self._loudness_control = loudness_control

    @property
    def preprocessing(self):
        # type: () -> DolbyDigitalPlusPreprocessing
        """Gets the preprocessing of this DolbyDigitalPlusAudioConfiguration.


        :return: The preprocessing of this DolbyDigitalPlusAudioConfiguration.
        :rtype: DolbyDigitalPlusPreprocessing
        """
        return self._preprocessing

    @preprocessing.setter
    def preprocessing(self, preprocessing):
        # type: (DolbyDigitalPlusPreprocessing) -> None
        """Sets the preprocessing of this DolbyDigitalPlusAudioConfiguration.


        :param preprocessing: The preprocessing of this DolbyDigitalPlusAudioConfiguration.
        :type: DolbyDigitalPlusPreprocessing
        """

        if preprocessing is not None:
            if not isinstance(preprocessing, DolbyDigitalPlusPreprocessing):
                raise TypeError("Invalid type for `preprocessing`, type has to be `DolbyDigitalPlusPreprocessing`")

        self._preprocessing = preprocessing

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DolbyDigitalPlusAudioConfiguration, self), "to_dict"):
            result = super(DolbyDigitalPlusAudioConfiguration, self).to_dict()
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
        if not isinstance(other, DolbyDigitalPlusAudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
