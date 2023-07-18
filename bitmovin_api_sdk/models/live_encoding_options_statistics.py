# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_options_type import LiveOptionsType
import pprint
import six


class LiveEncodingOptionsStatistics(object):
    @poscheck_model
    def __init__(self,
                 encoding_id=None,
                 units_used=None,
                 type_=None):
        # type: (string_types, float, LiveOptionsType) -> None

        self._encoding_id = None
        self._units_used = None
        self._type = None
        self.discriminator = None

        if encoding_id is not None:
            self.encoding_id = encoding_id
        if units_used is not None:
            self.units_used = units_used
        if type_ is not None:
            self.type = type_

    @property
    def openapi_types(self):
        types = {
            'encoding_id': 'string_types',
            'units_used': 'float',
            'type': 'LiveOptionsType'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'encoding_id': 'encodingId',
            'units_used': 'unitsUsed',
            'type': 'type'
        }
        return attributes

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this LiveEncodingOptionsStatistics.

        The ID of the encoding (required)

        :return: The encoding_id of this LiveEncodingOptionsStatistics.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this LiveEncodingOptionsStatistics.

        The ID of the encoding (required)

        :param encoding_id: The encoding_id of this LiveEncodingOptionsStatistics.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def units_used(self):
        # type: () -> float
        """Gets the units_used of this LiveEncodingOptionsStatistics.

        Live option units used (required)

        :return: The units_used of this LiveEncodingOptionsStatistics.
        :rtype: float
        """
        return self._units_used

    @units_used.setter
    def units_used(self, units_used):
        # type: (float) -> None
        """Sets the units_used of this LiveEncodingOptionsStatistics.

        Live option units used (required)

        :param units_used: The units_used of this LiveEncodingOptionsStatistics.
        :type: float
        """

        if units_used is not None:
            if not isinstance(units_used, (float, int)):
                raise TypeError("Invalid type for `units_used`, type has to be `float`")

        self._units_used = units_used

    @property
    def type(self):
        # type: () -> LiveOptionsType
        """Gets the type of this LiveEncodingOptionsStatistics.


        :return: The type of this LiveEncodingOptionsStatistics.
        :rtype: LiveOptionsType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (LiveOptionsType) -> None
        """Sets the type of this LiveEncodingOptionsStatistics.


        :param type_: The type of this LiveEncodingOptionsStatistics.
        :type: LiveOptionsType
        """

        if type_ is not None:
            if not isinstance(type_, LiveOptionsType):
                raise TypeError("Invalid type for `type`, type has to be `LiveOptionsType`")

        self._type = type_

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
        if not isinstance(other, LiveEncodingOptionsStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
