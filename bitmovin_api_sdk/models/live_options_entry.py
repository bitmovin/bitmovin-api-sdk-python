# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveOptionsEntry(object):
    @poscheck_model
    def __init__(self,
                 units_used=None):
        # type: (int) -> None

        self._units_used = None
        self.discriminator = None

        if units_used is not None:
            self.units_used = units_used

    @property
    def openapi_types(self):
        types = {
            'units_used': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'units_used': 'unitsUsed'
        }
        return attributes

    @property
    def units_used(self):
        # type: () -> int
        """Gets the units_used of this LiveOptionsEntry.

        Live option units used (required)

        :return: The units_used of this LiveOptionsEntry.
        :rtype: int
        """
        return self._units_used

    @units_used.setter
    def units_used(self, units_used):
        # type: (int) -> None
        """Sets the units_used of this LiveOptionsEntry.

        Live option units used (required)

        :param units_used: The units_used of this LiveOptionsEntry.
        :type: int
        """

        if units_used is not None:
            if not isinstance(units_used, int):
                raise TypeError("Invalid type for `units_used`, type has to be `int`")

        self._units_used = units_used

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
        if not isinstance(other, LiveOptionsEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
