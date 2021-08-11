# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_configuration import AudioConfiguration
from bitmovin_api_sdk.models.dts_mode import DtsMode
import pprint
import six


class DtsAudioConfiguration(AudioConfiguration):
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
                 mode=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, float, DtsMode) -> None
        super(DtsAudioConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, bitrate=bitrate, rate=rate)

        self._mode = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DtsAudioConfiguration, self), 'openapi_types'):
            types = getattr(super(DtsAudioConfiguration, self), 'openapi_types')

        types.update({
            'mode': 'DtsMode'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DtsAudioConfiguration, self), 'attribute_map'):
            attributes = getattr(super(DtsAudioConfiguration, self), 'attribute_map')

        attributes.update({
            'mode': 'mode'
        })
        return attributes

    @property
    def mode(self):
        # type: () -> DtsMode
        """Gets the mode of this DtsAudioConfiguration.

        There are two DTS modes available: DTS Express Audio (EXPRESS_AUDIO) and DTS Digital Surround (DIGITAL_SURROUND)

        :return: The mode of this DtsAudioConfiguration.
        :rtype: DtsMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        # type: (DtsMode) -> None
        """Sets the mode of this DtsAudioConfiguration.

        There are two DTS modes available: DTS Express Audio (EXPRESS_AUDIO) and DTS Digital Surround (DIGITAL_SURROUND)

        :param mode: The mode of this DtsAudioConfiguration.
        :type: DtsMode
        """

        if mode is not None:
            if not isinstance(mode, DtsMode):
                raise TypeError("Invalid type for `mode`, type has to be `DtsMode`")

        self._mode = mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(DtsAudioConfiguration, self), "to_dict"):
            result = super(DtsAudioConfiguration, self).to_dict()
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
        if not isinstance(other, DtsAudioConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
