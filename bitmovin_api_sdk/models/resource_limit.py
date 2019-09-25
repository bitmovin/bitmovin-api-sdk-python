# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class ResourceLimit(object):
    @poscheck_model
    def __init__(self,
                 name=None,
                 value=None,
                 effective_value=None):
        # type: (string_types, string_types, string_types) -> None

        self._name = None
        self._value = None
        self._effective_value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if effective_value is not None:
            self.effective_value = effective_value

    @property
    def openapi_types(self):
        types = {
            'name': 'string_types',
            'value': 'string_types',
            'effective_value': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'value': 'value',
            'effective_value': 'effectiveValue'
        }
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this ResourceLimit.


        :return: The name of this ResourceLimit.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this ResourceLimit.


        :param name: The name of this ResourceLimit.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def value(self):
        # type: () -> string_types
        """Gets the value of this ResourceLimit.


        :return: The value of this ResourceLimit.
        :rtype: string_types
        """
        return self._value

    @value.setter
    def value(self, value):
        # type: (string_types) -> None
        """Sets the value of this ResourceLimit.


        :param value: The value of this ResourceLimit.
        :type: string_types
        """

        if value is not None:
            if not isinstance(value, string_types):
                raise TypeError("Invalid type for `value`, type has to be `string_types`")

        self._value = value

    @property
    def effective_value(self):
        # type: () -> string_types
        """Gets the effective_value of this ResourceLimit.

        Specifies the remaining limit value for limits divided to sub-organizations. This property is returned only for parent organizations and only for mentioned limits.

        :return: The effective_value of this ResourceLimit.
        :rtype: string_types
        """
        return self._effective_value

    @effective_value.setter
    def effective_value(self, effective_value):
        # type: (string_types) -> None
        """Sets the effective_value of this ResourceLimit.

        Specifies the remaining limit value for limits divided to sub-organizations. This property is returned only for parent organizations and only for mentioned limits.

        :param effective_value: The effective_value of this ResourceLimit.
        :type: string_types
        """

        if effective_value is not None:
            if not isinstance(effective_value, string_types):
                raise TypeError("Invalid type for `effective_value`, type has to be `string_types`")

        self._effective_value = effective_value

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
        if not isinstance(other, ResourceLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
