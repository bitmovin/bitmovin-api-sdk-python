# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamFilter(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 position=None):
        # type: (string_types, int) -> None

        self._id = None
        self._position = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if position is not None:
            self.position = position

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'position': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'position': 'position'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this StreamFilter.

        The id of the filter that should be used in the stream (required)

        :return: The id of this StreamFilter.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this StreamFilter.

        The id of the filter that should be used in the stream (required)

        :param id_: The id of this StreamFilter.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def position(self):
        # type: () -> int
        """Gets the position of this StreamFilter.

        Defines the order in which filters are applied. Filters are applied in ascending order. (required)

        :return: The position of this StreamFilter.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        # type: (int) -> None
        """Sets the position of this StreamFilter.

        Defines the order in which filters are applied. Filters are applied in ascending order. (required)

        :param position: The position of this StreamFilter.
        :type: int
        """

        if position is not None:
            if not isinstance(position, int):
                raise TypeError("Invalid type for `position`, type has to be `int`")

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
        if not isinstance(other, StreamFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
