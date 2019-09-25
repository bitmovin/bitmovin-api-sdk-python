# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class ConcatenationInputConfiguration(object):
    @poscheck_model
    def __init__(self,
                 input_stream_id=None,
                 is_main=None,
                 position=None):
        # type: (string_types, bool, int) -> None

        self._input_stream_id = None
        self._is_main = None
        self._position = None
        self.discriminator = None

        if input_stream_id is not None:
            self.input_stream_id = input_stream_id
        if is_main is not None:
            self.is_main = is_main
        if position is not None:
            self.position = position

    @property
    def openapi_types(self):
        types = {
            'input_stream_id': 'string_types',
            'is_main': 'bool',
            'position': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'input_stream_id': 'inputStreamId',
            'is_main': 'isMain',
            'position': 'position'
        }
        return attributes

    @property
    def input_stream_id(self):
        # type: () -> string_types
        """Gets the input_stream_id of this ConcatenationInputConfiguration.

        The id of the input stream that should be used for concatenation. Can be either an ingest input stream, or the result of a trimming input stream

        :return: The input_stream_id of this ConcatenationInputConfiguration.
        :rtype: string_types
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        # type: (string_types) -> None
        """Sets the input_stream_id of this ConcatenationInputConfiguration.

        The id of the input stream that should be used for concatenation. Can be either an ingest input stream, or the result of a trimming input stream

        :param input_stream_id: The input_stream_id of this ConcatenationInputConfiguration.
        :type: string_types
        """

        if input_stream_id is not None:
            if not isinstance(input_stream_id, string_types):
                raise TypeError("Invalid type for `input_stream_id`, type has to be `string_types`")

        self._input_stream_id = input_stream_id

    @property
    def is_main(self):
        # type: () -> bool
        """Gets the is_main of this ConcatenationInputConfiguration.

        Exactly one input stream of a concatenation must have this set to true, which will be used as reference for scaling, aspect ratio, FPS, sample rate, etc. 

        :return: The is_main of this ConcatenationInputConfiguration.
        :rtype: bool
        """
        return self._is_main

    @is_main.setter
    def is_main(self, is_main):
        # type: (bool) -> None
        """Sets the is_main of this ConcatenationInputConfiguration.

        Exactly one input stream of a concatenation must have this set to true, which will be used as reference for scaling, aspect ratio, FPS, sample rate, etc. 

        :param is_main: The is_main of this ConcatenationInputConfiguration.
        :type: bool
        """

        if is_main is not None:
            if not isinstance(is_main, bool):
                raise TypeError("Invalid type for `is_main`, type has to be `bool`")

        self._is_main = is_main

    @property
    def position(self):
        # type: () -> int
        """Gets the position of this ConcatenationInputConfiguration.

        Position of the stream

        :return: The position of this ConcatenationInputConfiguration.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        # type: (int) -> None
        """Sets the position of this ConcatenationInputConfiguration.

        Position of the stream

        :param position: The position of this ConcatenationInputConfiguration.
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
        if not isinstance(other, ConcatenationInputConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
