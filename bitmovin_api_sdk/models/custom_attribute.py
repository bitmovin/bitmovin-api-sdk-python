# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class CustomAttribute(object):
    @poscheck_model
    def __init__(self,
                 key=None,
                 value=None):
        # type: (string_types, string_types) -> None

        self._key = None
        self._value = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def openapi_types(self):
        types = {
            'key': 'string_types',
            'value': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'key': 'key',
            'value': 'value'
        }
        return attributes

    @property
    def key(self):
        # type: () -> string_types
        """Gets the key of this CustomAttribute.

        unique string identifier for the custom attribute (required)

        :return: The key of this CustomAttribute.
        :rtype: string_types
        """
        return self._key

    @key.setter
    def key(self, key):
        # type: (string_types) -> None
        """Sets the key of this CustomAttribute.

        unique string identifier for the custom attribute (required)

        :param key: The key of this CustomAttribute.
        :type: string_types
        """

        if key is not None:
            if not isinstance(key, string_types):
                raise TypeError("Invalid type for `key`, type has to be `string_types`")

        self._key = key

    @property
    def value(self):
        # type: () -> string_types
        """Gets the value of this CustomAttribute.

        value of the custom attribute

        :return: The value of this CustomAttribute.
        :rtype: string_types
        """
        return self._value

    @value.setter
    def value(self, value):
        # type: (string_types) -> None
        """Sets the value of this CustomAttribute.

        value of the custom attribute

        :param value: The value of this CustomAttribute.
        :type: string_types
        """

        if value is not None:
            if not isinstance(value, string_types):
                raise TypeError("Invalid type for `value`, type has to be `string_types`")

        self._value = value

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
        if not isinstance(other, CustomAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
