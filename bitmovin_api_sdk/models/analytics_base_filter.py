# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsBaseFilter(object):
    @poscheck_model
    def __init__(self,
                 name=None,
                 operator=None):
        # type: (string_types, string_types) -> None

        self._name = None
        self._operator = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if operator is not None:
            self.operator = operator

    @property
    def openapi_types(self):
        types = {
            'name': 'string_types',
            'operator': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'operator': 'operator'
        }
        return attributes

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this AnalyticsBaseFilter.


        :return: The name of this AnalyticsBaseFilter.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this AnalyticsBaseFilter.


        :param name: The name of this AnalyticsBaseFilter.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def operator(self):
        # type: () -> string_types
        """Gets the operator of this AnalyticsBaseFilter.


        :return: The operator of this AnalyticsBaseFilter.
        :rtype: string_types
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        # type: (string_types) -> None
        """Sets the operator of this AnalyticsBaseFilter.


        :param operator: The operator of this AnalyticsBaseFilter.
        :type: string_types
        """

        if operator is not None:
            if not isinstance(operator, string_types):
                raise TypeError("Invalid type for `operator`, type has to be `string_types`")

        self._operator = operator

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
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
        if not isinstance(other, AnalyticsBaseFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
