# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class InputFactorCodec(object):
    @poscheck_model
    def __init__(self,
                 value=None,
                 factor=None):
        # type: (string_types, float) -> None

        self._value = None
        self._factor = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if factor is not None:
            self.factor = factor

    @property
    def openapi_types(self):
        types = {
            'value': 'string_types',
            'factor': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'value': 'value',
            'factor': 'factor'
        }
        return attributes

    @property
    def value(self):
        # type: () -> string_types
        """Gets the value of this InputFactorCodec.


        :return: The value of this InputFactorCodec.
        :rtype: string_types
        """
        return self._value

    @value.setter
    def value(self, value):
        # type: (string_types) -> None
        """Sets the value of this InputFactorCodec.


        :param value: The value of this InputFactorCodec.
        :type: string_types
        """

        if value is not None:
            if not isinstance(value, string_types):
                raise TypeError("Invalid type for `value`, type has to be `string_types`")

        self._value = value

    @property
    def factor(self):
        # type: () -> float
        """Gets the factor of this InputFactorCodec.


        :return: The factor of this InputFactorCodec.
        :rtype: float
        """
        return self._factor

    @factor.setter
    def factor(self, factor):
        # type: (float) -> None
        """Sets the factor of this InputFactorCodec.


        :param factor: The factor of this InputFactorCodec.
        :type: float
        """

        if factor is not None:
            if not isinstance(factor, (float, int)):
                raise TypeError("Invalid type for `factor`, type has to be `float`")

        self._factor = factor

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
        if not isinstance(other, InputFactorCodec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
