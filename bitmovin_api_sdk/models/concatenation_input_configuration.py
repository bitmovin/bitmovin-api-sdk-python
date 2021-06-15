# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.aspect_mode import AspectMode
from bitmovin_api_sdk.models.padding_sequence import PaddingSequence
import pprint
import six


class ConcatenationInputConfiguration(object):
    @poscheck_model
    def __init__(self,
                 input_stream_id=None,
                 is_main=None,
                 position=None,
                 padding_before=None,
                 padding_after=None,
                 aspect_mode=None):
        # type: (string_types, bool, int, PaddingSequence, PaddingSequence, AspectMode) -> None

        self._input_stream_id = None
        self._is_main = None
        self._position = None
        self._padding_before = None
        self._padding_after = None
        self._aspect_mode = None
        self.discriminator = None

        if input_stream_id is not None:
            self.input_stream_id = input_stream_id
        if is_main is not None:
            self.is_main = is_main
        if position is not None:
            self.position = position
        if padding_before is not None:
            self.padding_before = padding_before
        if padding_after is not None:
            self.padding_after = padding_after
        if aspect_mode is not None:
            self.aspect_mode = aspect_mode

    @property
    def openapi_types(self):
        types = {
            'input_stream_id': 'string_types',
            'is_main': 'bool',
            'position': 'int',
            'padding_before': 'PaddingSequence',
            'padding_after': 'PaddingSequence',
            'aspect_mode': 'AspectMode'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'input_stream_id': 'inputStreamId',
            'is_main': 'isMain',
            'position': 'position',
            'padding_before': 'paddingBefore',
            'padding_after': 'paddingAfter',
            'aspect_mode': 'aspectMode'
        }
        return attributes

    @property
    def input_stream_id(self):
        # type: () -> string_types
        """Gets the input_stream_id of this ConcatenationInputConfiguration.

        The ID of the input stream to be concatenated. This can be an ingest input stream or a trimming input stream (required)

        :return: The input_stream_id of this ConcatenationInputConfiguration.
        :rtype: string_types
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        # type: (string_types) -> None
        """Sets the input_stream_id of this ConcatenationInputConfiguration.

        The ID of the input stream to be concatenated. This can be an ingest input stream or a trimming input stream (required)

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

        A unique integer value that determines concatenation order (required)

        :return: The position of this ConcatenationInputConfiguration.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        # type: (int) -> None
        """Sets the position of this ConcatenationInputConfiguration.

        A unique integer value that determines concatenation order (required)

        :param position: The position of this ConcatenationInputConfiguration.
        :type: int
        """

        if position is not None:
            if not isinstance(position, int):
                raise TypeError("Invalid type for `position`, type has to be `int`")

        self._position = position

    @property
    def padding_before(self):
        # type: () -> PaddingSequence
        """Gets the padding_before of this ConcatenationInputConfiguration.

        Inserts a padding sequence (black frames and/or silent audio) before the input stream.

        :return: The padding_before of this ConcatenationInputConfiguration.
        :rtype: PaddingSequence
        """
        return self._padding_before

    @padding_before.setter
    def padding_before(self, padding_before):
        # type: (PaddingSequence) -> None
        """Sets the padding_before of this ConcatenationInputConfiguration.

        Inserts a padding sequence (black frames and/or silent audio) before the input stream.

        :param padding_before: The padding_before of this ConcatenationInputConfiguration.
        :type: PaddingSequence
        """

        if padding_before is not None:
            if not isinstance(padding_before, PaddingSequence):
                raise TypeError("Invalid type for `padding_before`, type has to be `PaddingSequence`")

        self._padding_before = padding_before

    @property
    def padding_after(self):
        # type: () -> PaddingSequence
        """Gets the padding_after of this ConcatenationInputConfiguration.

        Inserts a padding sequence (black frames and/or silent audio) after the input stream.

        :return: The padding_after of this ConcatenationInputConfiguration.
        :rtype: PaddingSequence
        """
        return self._padding_after

    @padding_after.setter
    def padding_after(self, padding_after):
        # type: (PaddingSequence) -> None
        """Sets the padding_after of this ConcatenationInputConfiguration.

        Inserts a padding sequence (black frames and/or silent audio) after the input stream.

        :param padding_after: The padding_after of this ConcatenationInputConfiguration.
        :type: PaddingSequence
        """

        if padding_after is not None:
            if not isinstance(padding_after, PaddingSequence):
                raise TypeError("Invalid type for `padding_after`, type has to be `PaddingSequence`")

        self._padding_after = padding_after

    @property
    def aspect_mode(self):
        # type: () -> AspectMode
        """Gets the aspect_mode of this ConcatenationInputConfiguration.

        Specifies the aspect mode that is used when adapting to the main input stream's aspect ratio

        :return: The aspect_mode of this ConcatenationInputConfiguration.
        :rtype: AspectMode
        """
        return self._aspect_mode

    @aspect_mode.setter
    def aspect_mode(self, aspect_mode):
        # type: (AspectMode) -> None
        """Sets the aspect_mode of this ConcatenationInputConfiguration.

        Specifies the aspect mode that is used when adapting to the main input stream's aspect ratio

        :param aspect_mode: The aspect_mode of this ConcatenationInputConfiguration.
        :type: AspectMode
        """

        if aspect_mode is not None:
            if not isinstance(aspect_mode, AspectMode):
                raise TypeError("Invalid type for `aspect_mode`, type has to be `AspectMode`")

        self._aspect_mode = aspect_mode

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
