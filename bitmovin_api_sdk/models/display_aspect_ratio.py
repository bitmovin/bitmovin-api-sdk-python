# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class DisplayAspectRatio(object):
    @poscheck_model
    def __init__(self,
                 numerator=None,
                 denominator=None):
        # type: (int, int) -> None

        self._numerator = None
        self._denominator = None
        self.discriminator = None

        if numerator is not None:
            self.numerator = numerator
        if denominator is not None:
            self.denominator = denominator

    @property
    def openapi_types(self):
        types = {
            'numerator': 'int',
            'denominator': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'numerator': 'numerator',
            'denominator': 'denominator'
        }
        return attributes

    @property
    def numerator(self):
        # type: () -> int
        """Gets the numerator of this DisplayAspectRatio.

        The numerator of the display aspect ratio (DAR). For example for a DAR of 16:9, the value 16 must be used. (required)

        :return: The numerator of this DisplayAspectRatio.
        :rtype: int
        """
        return self._numerator

    @numerator.setter
    def numerator(self, numerator):
        # type: (int) -> None
        """Sets the numerator of this DisplayAspectRatio.

        The numerator of the display aspect ratio (DAR). For example for a DAR of 16:9, the value 16 must be used. (required)

        :param numerator: The numerator of this DisplayAspectRatio.
        :type: int
        """

        if numerator is not None:
            if numerator is not None and numerator < 1:
                raise ValueError("Invalid value for `numerator`, must be a value greater than or equal to `1`")
            if not isinstance(numerator, int):
                raise TypeError("Invalid type for `numerator`, type has to be `int`")

        self._numerator = numerator

    @property
    def denominator(self):
        # type: () -> int
        """Gets the denominator of this DisplayAspectRatio.

        The denominator of the display aspect ratio (DAR). For example for a DAR of 16:9, the value 9 must be used. (required)

        :return: The denominator of this DisplayAspectRatio.
        :rtype: int
        """
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        # type: (int) -> None
        """Sets the denominator of this DisplayAspectRatio.

        The denominator of the display aspect ratio (DAR). For example for a DAR of 16:9, the value 9 must be used. (required)

        :param denominator: The denominator of this DisplayAspectRatio.
        :type: int
        """

        if denominator is not None:
            if denominator is not None and denominator < 1:
                raise ValueError("Invalid value for `denominator`, must be a value greater than or equal to `1`")
            if not isinstance(denominator, int):
                raise TypeError("Invalid type for `denominator`, type has to be `int`")

        self._denominator = denominator

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
        if not isinstance(other, DisplayAspectRatio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
