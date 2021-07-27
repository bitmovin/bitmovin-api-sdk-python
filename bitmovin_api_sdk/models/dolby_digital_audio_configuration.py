# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_configuration import AudioConfiguration
from bitmovin_api_sdk.models.dolby_digital_bitstream_info import DolbyDigitalBitstreamInfo
from bitmovin_api_sdk.models.dolby_digital_channel_layout import DolbyDigitalChannelLayout
from bitmovin_api_sdk.models.dolby_digital_downmixing import DolbyDigitalDownmixing
from bitmovin_api_sdk.models.dolby_digital_evolution_framework_control import DolbyDigitalEvolutionFrameworkControl
from bitmovin_api_sdk.models.dolby_digital_loudness_control import DolbyDigitalLoudnessControl
from bitmovin_api_sdk.models.dolby_digital_preprocessing import DolbyDigitalPreprocessing
import pprint
import six


class DolbyDigitalAudioConfiguration(AudioConfiguration):
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
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, float, DolbyDigitalBitstreamInfo, DolbyDigitalChannelLayout, DolbyDigitalDownmixing, DolbyDigitalEvolutionFrameworkControl, DolbyDigitalLoudnessControl, DolbyDigitalPreprocessing) -> None
        super(DolbyDigitalAudioConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, bitrate=bitrate, rate=rate)

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

        if hasattr(super(DolbyDigitalAudioConfiguration, self), 'openapi_types'):
            types = getattr(super(DolbyDigitalAudioConfiguration, self), 'openapi_types')

        types.update({
            'bitstream_info': 'DolbyDigitalBitstreamInfo',
            'channel_layout': 'DolbyDigitalChannelLayout',
            'downmixing': 'DolbyDigitalDownmixing',
            'evolution_framework_control': 'DolbyDigitalEvolutionFrameworkControl',
            'loudness_control': 'DolbyDigitalLoudnessControl',
            'preprocessing': 'DolbyDigitalPreprocessing'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DolbyDigitalAudioConfiguration, self), 'attribute_map'):
            attributes = getattr(super(DolbyDigitalAudioConfiguration, self), 'attribute_map')

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
        # type: () -> DolbyDigitalBitstreamInfo
        """Gets the bitstream_info of this DolbyDigitalAudioConfiguration.

        BitstreamInfo defines metadata parameters contained in the Dolby Digital audio bitstream

        :return: The bitstream_info of this DolbyDigitalAudioConfiguration.
        :rtype: DolbyDigitalBitstreamInfo
        """
        return self._bitstream_info

    @bitstream_info.setter
    def bitstream_info(self, bitstream_info):
        # type: (DolbyDigitalBitstreamInfo) -> None
        """Sets the bitstream_info of this DolbyDigitalAudioConfiguration.

        BitstreamInfo defines metadata parameters contained in the Dolby Digital audio bitstream

        :param bitstream_info: The bitstream_info of this DolbyDigitalAudioConfiguration.
        :type: DolbyDigitalBitstreamInfo
        """

        if bitstream_info is not None:
            if not isinstance(bitstream_info, DolbyDigitalBitstreamInfo):
                raise TypeError("Invalid type for `bitstream_info`, type has to be `DolbyDigitalBitstreamInfo`")

        self._bitstream_info = bitstream_info

    @property
    def channel_layout(self):
        # type: () -> DolbyDigitalChannelLayout
        """Gets the channel_layout of this DolbyDigitalAudioConfiguration.

        Channel layout of the audio codec configuration.

        :return: The channel_layout of this DolbyDigitalAudioConfiguration.
        :rtype: DolbyDigitalChannelLayout
        """
        return self._channel_layout

    @channel_layout.setter
    def channel_layout(self, channel_layout):
        # type: (DolbyDigitalChannelLayout) -> None
        """Sets the channel_layout of this DolbyDigitalAudioConfiguration.

        Channel layout of the audio codec configuration.

        :param channel_layout: The channel_layout of this DolbyDigitalAudioConfiguration.
        :type: DolbyDigitalChannelLayout
        """

        if channel_layout is not None:
            if not isinstance(channel_layout, DolbyDigitalChannelLayout):
                raise TypeError("Invalid type for `channel_layout`, type has to be `DolbyDigitalChannelLayout`")

        self._channel_layout = channel_layout

    @property
    def downmixing(self):
        # type: () -> DolbyDigitalDownmixing
        """Gets the downmixing of this DolbyDigitalAudioConfiguration.


        :return: The downmixing of this DolbyDigitalAudioConfiguration.
        :rtype: DolbyDigitalDownmixing
        """
        return self._downmixing

    @downmixing.setter
    def downmixing(self, downmixing):
        # type: (DolbyDigitalDownmixing) -> None
        """Sets the downmixing of this DolbyDigitalAudioConfiguration.


        :param downmixing: The downmixing of this DolbyDigitalAudioConfiguration.
        :type: DolbyDigitalDownmixing
        """

        if downmixing is not None:
            if not isinstance(downmixing, DolbyDigitalDownmixing):
                raise TypeError("Invalid type for `downmixing`, type has to be `DolbyDigitalDownmixing`")

        self._downmixing = downmixing

    @property
    def evolution_framework_control(self):
        # type: () -> DolbyDigitalEvolutionFrameworkControl
        """Gets the evolution_framework_control of this DolbyDigitalAudioConfiguration.

        It provides a framework for signaling new evolution framework applications, such as Intelligent Loudness, in each Dolby codec. 

        :return: The evolution_framework_control of this DolbyDigitalAudioConfiguration.
        :rtype: DolbyDigitalEvolutionFrameworkControl
        """
        return self._evolution_framework_control

    @evolution_framework_control.setter
    def evolution_framework_control(self, evolution_framework_control):
        # type: (DolbyDigitalEvolutionFrameworkControl) -> None
        """Sets the evolution_framework_control of this DolbyDigitalAudioConfiguration.

        It provides a framework for signaling new evolution framework applications, such as Intelligent Loudness, in each Dolby codec. 

        :param evolution_framework_control: The evolution_framework_control of this DolbyDigitalAudioConfiguration.
        :type: DolbyDigitalEvolutionFrameworkControl
        """

        if evolution_framework_control is not None:
            if not isinstance(evolution_framework_control, DolbyDigitalEvolutionFrameworkControl):
                raise TypeError("Invalid type for `evolution_framework_control`, type has to be `DolbyDigitalEvolutionFrameworkControl`")

        self._evolution_framework_control = evolution_framework_control

    @property
    def loudness_control(self):
        # type: () -> DolbyDigitalLoudnessControl
        """Gets the loudness_control of this DolbyDigitalAudioConfiguration.

        Settings for loudness control (required)

        :return: The loudness_control of this DolbyDigitalAudioConfiguration.
        :rtype: DolbyDigitalLoudnessControl
        """
        return self._loudness_control

    @loudness_control.setter
    def loudness_control(self, loudness_control):
        # type: (DolbyDigitalLoudnessControl) -> None
        """Sets the loudness_control of this DolbyDigitalAudioConfiguration.

        Settings for loudness control (required)

        :param loudness_control: The loudness_control of this DolbyDigitalAudioConfiguration.
        :type: DolbyDigitalLoudnessControl
        """

        if loudness_control is not None:
            if not isinstance(loudness_control, DolbyDigitalLoudnessControl):
                raise TypeError("Invalid type for `loudness_control`, type has to be `DolbyDigitalLoudnessControl`")

        self._loudness_control = loudness_control

    @property
    def preprocessing(self):
        # type: () -> DolbyDigitalPreprocessing
        """Gets the preprocessing of this DolbyDigitalAudioConfiguration.


        :return: The preprocessing of this DolbyDigitalAudioConfiguration.
        :rtype: DolbyDigitalPreprocessing
        """
        return self._preprocessing

    @preprocessing.setter
    def preprocessing(self, preprocessing):
        # type: (DolbyDigitalPreprocessing) -> None
        """Sets the preprocessing of this DolbyDigitalAudioConfiguration.


        :param preprocessing: The preprocessing of this DolbyDigitalAudioConfiguration.
        :type: DolbyDigitalPreprocessing
        """

        if preprocessing is not None:
            if not isinstance(preprocessing, DolbyDigitalPreprocessing):
                raise TypeError("Invalid type for `preprocessing`, type has to be `DolbyDigitalPreprocessing`")

        self._preprocessing = preprocessing

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DolbyDigitalAudioConfiguration, self), "to_dict"):
            result = super(DolbyDigitalAudioConfiguration, self).to_dict()
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
        if not isinstance(other, DolbyDigitalAudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
