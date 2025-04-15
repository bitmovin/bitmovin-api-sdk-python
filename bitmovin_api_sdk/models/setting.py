# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.atmosphere import Atmosphere
from bitmovin_api_sdk.models.location import Location
import pprint
import six


class Setting(object):
    @poscheck_model
    def __init__(self,
                 location=None,
                 time_of_day=None,
                 atmosphere=None):
        # type: (Location, string_types, Atmosphere) -> None

        self._location = None
        self._time_of_day = None
        self._atmosphere = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if time_of_day is not None:
            self.time_of_day = time_of_day
        if atmosphere is not None:
            self.atmosphere = atmosphere

    @property
    def openapi_types(self):
        types = {
            'location': 'Location',
            'time_of_day': 'string_types',
            'atmosphere': 'Atmosphere'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'location': 'location',
            'time_of_day': 'timeOfDay',
            'atmosphere': 'atmosphere'
        }
        return attributes

    @property
    def location(self):
        # type: () -> Location
        """Gets the location of this Setting.


        :return: The location of this Setting.
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        # type: (Location) -> None
        """Sets the location of this Setting.


        :param location: The location of this Setting.
        :type: Location
        """

        if location is not None:
            if not isinstance(location, Location):
                raise TypeError("Invalid type for `location`, type has to be `Location`")

        self._location = location

    @property
    def time_of_day(self):
        # type: () -> string_types
        """Gets the time_of_day of this Setting.


        :return: The time_of_day of this Setting.
        :rtype: string_types
        """
        return self._time_of_day

    @time_of_day.setter
    def time_of_day(self, time_of_day):
        # type: (string_types) -> None
        """Sets the time_of_day of this Setting.


        :param time_of_day: The time_of_day of this Setting.
        :type: string_types
        """

        if time_of_day is not None:
            if not isinstance(time_of_day, string_types):
                raise TypeError("Invalid type for `time_of_day`, type has to be `string_types`")

        self._time_of_day = time_of_day

    @property
    def atmosphere(self):
        # type: () -> Atmosphere
        """Gets the atmosphere of this Setting.


        :return: The atmosphere of this Setting.
        :rtype: Atmosphere
        """
        return self._atmosphere

    @atmosphere.setter
    def atmosphere(self, atmosphere):
        # type: (Atmosphere) -> None
        """Sets the atmosphere of this Setting.


        :param atmosphere: The atmosphere of this Setting.
        :type: Atmosphere
        """

        if atmosphere is not None:
            if not isinstance(atmosphere, Atmosphere):
                raise TypeError("Invalid type for `atmosphere`, type has to be `Atmosphere`")

        self._atmosphere = atmosphere

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
        if not isinstance(other, Setting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
