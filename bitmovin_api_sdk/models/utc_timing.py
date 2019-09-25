# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class UtcTiming(object):
    @poscheck_model
    def __init__(self,
                 value=None,
                 scheme_id_uri=None):
        # type: (string_types, string_types) -> None

        self._value = None
        self._scheme_id_uri = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if scheme_id_uri is not None:
            self.scheme_id_uri = scheme_id_uri

    @property
    def openapi_types(self):
        types = {
            'value': 'string_types',
            'scheme_id_uri': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'value': 'value',
            'scheme_id_uri': 'schemeIdUri'
        }
        return attributes

    @property
    def value(self):
        # type: () -> string_types
        """Gets the value of this UtcTiming.

        The server to get the time from (required)

        :return: The value of this UtcTiming.
        :rtype: string_types
        """
        return self._value

    @value.setter
    def value(self, value):
        # type: (string_types) -> None
        """Sets the value of this UtcTiming.

        The server to get the time from (required)

        :param value: The value of this UtcTiming.
        :type: string_types
        """

        if value is not None:
            if not isinstance(value, string_types):
                raise TypeError("Invalid type for `value`, type has to be `string_types`")

        self._value = value

    @property
    def scheme_id_uri(self):
        # type: () -> string_types
        """Gets the scheme_id_uri of this UtcTiming.

        The scheme id to use. Please refer to the DASH standard. (required)

        :return: The scheme_id_uri of this UtcTiming.
        :rtype: string_types
        """
        return self._scheme_id_uri

    @scheme_id_uri.setter
    def scheme_id_uri(self, scheme_id_uri):
        # type: (string_types) -> None
        """Sets the scheme_id_uri of this UtcTiming.

        The scheme id to use. Please refer to the DASH standard. (required)

        :param scheme_id_uri: The scheme_id_uri of this UtcTiming.
        :type: string_types
        """

        if scheme_id_uri is not None:
            if not isinstance(scheme_id_uri, string_types):
                raise TypeError("Invalid type for `scheme_id_uri`, type has to be `string_types`")

        self._scheme_id_uri = scheme_id_uri

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
        if not isinstance(other, UtcTiming):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
