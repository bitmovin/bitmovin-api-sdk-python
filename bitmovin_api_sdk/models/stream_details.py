# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamDetails(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 codec=None,
                 duration=None,
                 position=None):
        # type: (string_types, string_types, int, int) -> None

        self._id = None
        self._codec = None
        self._duration = None
        self._position = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if codec is not None:
            self.codec = codec
        if duration is not None:
            self.duration = duration
        if position is not None:
            self.position = position

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'codec': 'string_types',
            'duration': 'int',
            'position': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'codec': 'codec',
            'duration': 'duration',
            'position': 'position'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this StreamDetails.


        :return: The id of this StreamDetails.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this StreamDetails.


        :param id_: The id of this StreamDetails.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def codec(self):
        # type: () -> string_types
        """Gets the codec of this StreamDetails.


        :return: The codec of this StreamDetails.
        :rtype: string_types
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (string_types) -> None
        """Sets the codec of this StreamDetails.


        :param codec: The codec of this StreamDetails.
        :type: string_types
        """

        if codec is not None:
            if not isinstance(codec, string_types):
                raise TypeError("Invalid type for `codec`, type has to be `string_types`")

        self._codec = codec

    @property
    def duration(self):
        # type: () -> int
        """Gets the duration of this StreamDetails.


        :return: The duration of this StreamDetails.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        # type: (int) -> None
        """Sets the duration of this StreamDetails.


        :param duration: The duration of this StreamDetails.
        :type: int
        """

        if duration is not None:
            if not isinstance(duration, int):
                raise TypeError("Invalid type for `duration`, type has to be `int`")

        self._duration = duration

    @property
    def position(self):
        # type: () -> int
        """Gets the position of this StreamDetails.


        :return: The position of this StreamDetails.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        # type: (int) -> None
        """Sets the position of this StreamDetails.


        :param position: The position of this StreamDetails.
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
        if not isinstance(other, StreamDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
