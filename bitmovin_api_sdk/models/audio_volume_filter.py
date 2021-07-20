# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_volume_format import AudioVolumeFormat
from bitmovin_api_sdk.models.audio_volume_unit import AudioVolumeUnit
from bitmovin_api_sdk.models.filter import Filter
import pprint
import six


class AudioVolumeFilter(Filter):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 volume=None,
                 unit=None,
                 format_=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, float, AudioVolumeUnit, AudioVolumeFormat) -> None
        super(AudioVolumeFilter, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._volume = None
        self._unit = None
        self._format = None
        self.discriminator = None

        if volume is not None:
            self.volume = volume
        if unit is not None:
            self.unit = unit
        if format_ is not None:
            self.format = format_

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AudioVolumeFilter, self), 'openapi_types'):
            types = getattr(super(AudioVolumeFilter, self), 'openapi_types')

        types.update({
            'volume': 'float',
            'unit': 'AudioVolumeUnit',
            'format': 'AudioVolumeFormat'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AudioVolumeFilter, self), 'attribute_map'):
            attributes = getattr(super(AudioVolumeFilter, self), 'attribute_map')

        attributes.update({
            'volume': 'volume',
            'unit': 'unit',
            'format': 'format'
        })
        return attributes

    @property
    def volume(self):
        # type: () -> float
        """Gets the volume of this AudioVolumeFilter.

        Audio volume value (required)

        :return: The volume of this AudioVolumeFilter.
        :rtype: float
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        # type: (float) -> None
        """Sets the volume of this AudioVolumeFilter.

        Audio volume value (required)

        :param volume: The volume of this AudioVolumeFilter.
        :type: float
        """

        if volume is not None:
            if not isinstance(volume, (float, int)):
                raise TypeError("Invalid type for `volume`, type has to be `float`")

        self._volume = volume

    @property
    def unit(self):
        # type: () -> AudioVolumeUnit
        """Gets the unit of this AudioVolumeFilter.


        :return: The unit of this AudioVolumeFilter.
        :rtype: AudioVolumeUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        # type: (AudioVolumeUnit) -> None
        """Sets the unit of this AudioVolumeFilter.


        :param unit: The unit of this AudioVolumeFilter.
        :type: AudioVolumeUnit
        """

        if unit is not None:
            if not isinstance(unit, AudioVolumeUnit):
                raise TypeError("Invalid type for `unit`, type has to be `AudioVolumeUnit`")

        self._unit = unit

    @property
    def format(self):
        # type: () -> AudioVolumeFormat
        """Gets the format of this AudioVolumeFilter.


        :return: The format of this AudioVolumeFilter.
        :rtype: AudioVolumeFormat
        """
        return self._format

    @format.setter
    def format(self, format_):
        # type: (AudioVolumeFormat) -> None
        """Sets the format of this AudioVolumeFilter.


        :param format_: The format of this AudioVolumeFilter.
        :type: AudioVolumeFormat
        """

        if format_ is not None:
            if not isinstance(format_, AudioVolumeFormat):
                raise TypeError("Invalid type for `format`, type has to be `AudioVolumeFormat`")

        self._format = format_

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AudioVolumeFilter, self), "to_dict"):
            result = super(AudioVolumeFilter, self).to_dict()
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
        if not isinstance(other, AudioVolumeFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
