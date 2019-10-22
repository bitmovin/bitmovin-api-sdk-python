# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.padding_duration_unit import PaddingDurationUnit
import pprint
import six


class PaddingSequence(object):
    @poscheck_model
    def __init__(self,
                 duration=None,
                 unit=None):
        # type: (float, PaddingDurationUnit) -> None

        self._duration = None
        self._unit = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if unit is not None:
            self.unit = unit

    @property
    def openapi_types(self):
        types = {
            'duration': 'float',
            'unit': 'PaddingDurationUnit'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'duration': 'duration',
            'unit': 'unit'
        }
        return attributes

    @property
    def duration(self):
        # type: () -> float
        """Gets the duration of this PaddingSequence.

        Duration of the padding sequence, given in the unit specified by the `unit` property. The maximum duration is 300 frames or 10 seconds. If the unit is `FRAMES`, this needs to be an integer value and will be interpreted based on the input frame rate of the main part of the ConcatenationInputStream that is used by your video output stream(s). `FRAMES` is not allowed if the encoding does not contain a video output stream. (required)

        :return: The duration of this PaddingSequence.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        # type: (float) -> None
        """Sets the duration of this PaddingSequence.

        Duration of the padding sequence, given in the unit specified by the `unit` property. The maximum duration is 300 frames or 10 seconds. If the unit is `FRAMES`, this needs to be an integer value and will be interpreted based on the input frame rate of the main part of the ConcatenationInputStream that is used by your video output stream(s). `FRAMES` is not allowed if the encoding does not contain a video output stream. (required)

        :param duration: The duration of this PaddingSequence.
        :type: float
        """

        if duration is not None:
            if duration is not None and duration <= 0:
                raise ValueError("Invalid value for `duration`, must be a value greater than `0`")
            if not isinstance(duration, (float, int)):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

        self._duration = duration

    @property
    def unit(self):
        # type: () -> PaddingDurationUnit
        """Gets the unit of this PaddingSequence.

        The unit of the `duration` property

        :return: The unit of this PaddingSequence.
        :rtype: PaddingDurationUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        # type: (PaddingDurationUnit) -> None
        """Sets the unit of this PaddingSequence.

        The unit of the `duration` property

        :param unit: The unit of this PaddingSequence.
        :type: PaddingDurationUnit
        """

        if unit is not None:
            if not isinstance(unit, PaddingDurationUnit):
                raise TypeError("Invalid type for `unit`, type has to be `PaddingDurationUnit`")

        self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
        if not isinstance(other, PaddingSequence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
