# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AdPosition(object):
    @poscheck_model
    def __init__(self,
                 position=None):
        # type: (float) -> None

        self._position = None
        self.discriminator = None

        if position is not None:
            self.position = position

    @property
    def openapi_types(self):
        types = {
            'position': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'position': 'position'
        }
        return attributes

    @property
    def position(self):
        # type: () -> float
        """Gets the position of this AdPosition.


        :return: The position of this AdPosition.
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        # type: (float) -> None
        """Sets the position of this AdPosition.


        :param position: The position of this AdPosition.
        :type: float
        """

        if position is not None:
            if not isinstance(position, (float, int)):
                raise TypeError("Invalid type for `position`, type has to be `float`")

        self._position = position

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
        if not isinstance(other, AdPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
