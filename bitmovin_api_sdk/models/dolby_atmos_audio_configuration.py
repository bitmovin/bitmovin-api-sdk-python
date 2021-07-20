# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_configuration import AudioConfiguration
from bitmovin_api_sdk.models.dolby_atmos_loudness_control import DolbyAtmosLoudnessControl
import pprint
import six


class DolbyAtmosAudioConfiguration(AudioConfiguration):
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
                 loudness_control=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, float, DolbyAtmosLoudnessControl) -> None
        super(DolbyAtmosAudioConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, bitrate=bitrate, rate=rate)

        self._loudness_control = None
        self.discriminator = None

        if loudness_control is not None:
            self.loudness_control = loudness_control

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DolbyAtmosAudioConfiguration, self), 'openapi_types'):
            types = getattr(super(DolbyAtmosAudioConfiguration, self), 'openapi_types')

        types.update({
            'loudness_control': 'DolbyAtmosLoudnessControl'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DolbyAtmosAudioConfiguration, self), 'attribute_map'):
            attributes = getattr(super(DolbyAtmosAudioConfiguration, self), 'attribute_map')

        attributes.update({
            'loudness_control': 'loudnessControl'
        })
        return attributes

    @property
    def loudness_control(self):
        # type: () -> DolbyAtmosLoudnessControl
        """Gets the loudness_control of this DolbyAtmosAudioConfiguration.

        Settings for loudness control (required)

        :return: The loudness_control of this DolbyAtmosAudioConfiguration.
        :rtype: DolbyAtmosLoudnessControl
        """
        return self._loudness_control

    @loudness_control.setter
    def loudness_control(self, loudness_control):
        # type: (DolbyAtmosLoudnessControl) -> None
        """Sets the loudness_control of this DolbyAtmosAudioConfiguration.

        Settings for loudness control (required)

        :param loudness_control: The loudness_control of this DolbyAtmosAudioConfiguration.
        :type: DolbyAtmosLoudnessControl
        """

        if loudness_control is not None:
            if not isinstance(loudness_control, DolbyAtmosLoudnessControl):
                raise TypeError("Invalid type for `loudness_control`, type has to be `DolbyAtmosLoudnessControl`")

        self._loudness_control = loudness_control

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DolbyAtmosAudioConfiguration, self), "to_dict"):
            result = super(DolbyAtmosAudioConfiguration, self).to_dict()
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
        if not isinstance(other, DolbyAtmosAudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
