# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AutomaticAdPlacementPosition(object):
    @poscheck_model
    def __init__(self,
                 position=None,
                 max_deviation=None,
                 duration=None):
        # type: (float, float, float) -> None

        self._position = None
        self._max_deviation = None
        self._duration = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if max_deviation is not None:
            self.max_deviation = max_deviation
        if duration is not None:
            self.duration = duration

    @property
    def openapi_types(self):
        types = {
            'position': 'float',
            'max_deviation': 'float',
            'duration': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'position': 'position',
            'max_deviation': 'maxDeviation',
            'duration': 'duration'
        }
        return attributes

    @property
    def position(self):
        # type: () -> float
        """Gets the position of this AutomaticAdPlacementPosition.

        Position of the ad placement in seconds.

        :return: The position of this AutomaticAdPlacementPosition.
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        # type: (float) -> None
        """Sets the position of this AutomaticAdPlacementPosition.

        Position of the ad placement in seconds.

        :param position: The position of this AutomaticAdPlacementPosition.
        :type: float
        """

        if position is not None:
            if not isinstance(position, (float, int)):
                raise TypeError("Invalid type for `position`, type has to be `float`")

        self._position = position

    @property
    def max_deviation(self):
        # type: () -> float
        """Gets the max_deviation of this AutomaticAdPlacementPosition.

        Maximum deviation in seconds to the ad placement position.

        :return: The max_deviation of this AutomaticAdPlacementPosition.
        :rtype: float
        """
        return self._max_deviation

    @max_deviation.setter
    def max_deviation(self, max_deviation):
        # type: (float) -> None
        """Sets the max_deviation of this AutomaticAdPlacementPosition.

        Maximum deviation in seconds to the ad placement position.

        :param max_deviation: The max_deviation of this AutomaticAdPlacementPosition.
        :type: float
        """

        if max_deviation is not None:
            if not isinstance(max_deviation, (float, int)):
                raise TypeError("Invalid type for `max_deviation`, type has to be `float`")

        self._max_deviation = max_deviation

    @property
    def duration(self):
        # type: () -> float
        """Gets the duration of this AutomaticAdPlacementPosition.

        The desired duration in seconds of the ad to be inserted.

        :return: The duration of this AutomaticAdPlacementPosition.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        # type: (float) -> None
        """Sets the duration of this AutomaticAdPlacementPosition.

        The desired duration in seconds of the ad to be inserted.

        :param duration: The duration of this AutomaticAdPlacementPosition.
        :type: float
        """

        if duration is not None:
            if duration is not None and duration < 0:
                raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `0`")
            if not isinstance(duration, (float, int)):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

        self._duration = duration

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
        if not isinstance(other, AutomaticAdPlacementPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
