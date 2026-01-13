# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.esam_direction import EsamDirection
import pprint
import six


class EsamCondition(object):
    @poscheck_model
    def __init__(self,
                 offset=None,
                 direction=None):
        # type: (string_types, EsamDirection) -> None

        self._offset = None
        self._direction = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if direction is not None:
            self.direction = direction

    @property
    def openapi_types(self):
        types = {
            'offset': 'string_types',
            'direction': 'EsamDirection'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'direction': 'direction'
        }
        return attributes

    @property
    def offset(self):
        # type: () -> string_types
        """Gets the offset of this EsamCondition.

        The offset from the matched signal when this condition applies in ISO 8601 duration format, accurate to milliseconds (required)

        :return: The offset of this EsamCondition.
        :rtype: string_types
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        # type: (string_types) -> None
        """Sets the offset of this EsamCondition.

        The offset from the matched signal when this condition applies in ISO 8601 duration format, accurate to milliseconds (required)

        :param offset: The offset of this EsamCondition.
        :type: string_types
        """

        if offset is not None:
            if not isinstance(offset, string_types):
                raise TypeError("Invalid type for `offset`, type has to be `string_types`")

        self._offset = offset

    @property
    def direction(self):
        # type: () -> EsamDirection
        """Gets the direction of this EsamCondition.

        Direction marker indicating the boundary type (OUT for start, IN for end) (required)

        :return: The direction of this EsamCondition.
        :rtype: EsamDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        # type: (EsamDirection) -> None
        """Sets the direction of this EsamCondition.

        Direction marker indicating the boundary type (OUT for start, IN for end) (required)

        :param direction: The direction of this EsamCondition.
        :type: EsamDirection
        """

        if direction is not None:
            if not isinstance(direction, EsamDirection):
                raise TypeError("Invalid type for `direction`, type has to be `EsamDirection`")

        self._direction = direction

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
        if not isinstance(other, EsamCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
