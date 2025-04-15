# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class Atmosphere(object):
    @poscheck_model
    def __init__(self,
                 mood=None,
                 lighting=None,
                 weather=None):
        # type: (string_types, string_types, string_types) -> None

        self._mood = None
        self._lighting = None
        self._weather = None
        self.discriminator = None

        if mood is not None:
            self.mood = mood
        if lighting is not None:
            self.lighting = lighting
        if weather is not None:
            self.weather = weather

    @property
    def openapi_types(self):
        types = {
            'mood': 'string_types',
            'lighting': 'string_types',
            'weather': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'mood': 'mood',
            'lighting': 'lighting',
            'weather': 'weather'
        }
        return attributes

    @property
    def mood(self):
        # type: () -> string_types
        """Gets the mood of this Atmosphere.


        :return: The mood of this Atmosphere.
        :rtype: string_types
        """
        return self._mood

    @mood.setter
    def mood(self, mood):
        # type: (string_types) -> None
        """Sets the mood of this Atmosphere.


        :param mood: The mood of this Atmosphere.
        :type: string_types
        """

        if mood is not None:
            if not isinstance(mood, string_types):
                raise TypeError("Invalid type for `mood`, type has to be `string_types`")

        self._mood = mood

    @property
    def lighting(self):
        # type: () -> string_types
        """Gets the lighting of this Atmosphere.


        :return: The lighting of this Atmosphere.
        :rtype: string_types
        """
        return self._lighting

    @lighting.setter
    def lighting(self, lighting):
        # type: (string_types) -> None
        """Sets the lighting of this Atmosphere.


        :param lighting: The lighting of this Atmosphere.
        :type: string_types
        """

        if lighting is not None:
            if not isinstance(lighting, string_types):
                raise TypeError("Invalid type for `lighting`, type has to be `string_types`")

        self._lighting = lighting

    @property
    def weather(self):
        # type: () -> string_types
        """Gets the weather of this Atmosphere.


        :return: The weather of this Atmosphere.
        :rtype: string_types
        """
        return self._weather

    @weather.setter
    def weather(self, weather):
        # type: (string_types) -> None
        """Sets the weather of this Atmosphere.


        :param weather: The weather of this Atmosphere.
        :type: string_types
        """

        if weather is not None:
            if not isinstance(weather, string_types):
                raise TypeError("Invalid type for `weather`, type has to be `string_types`")

        self._weather = weather

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
        if not isinstance(other, Atmosphere):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
