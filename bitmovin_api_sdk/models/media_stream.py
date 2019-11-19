# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class MediaStream(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 position=None,
                 duration=None,
                 codec=None):
        # type: (string_types, int, float, string_types) -> None
        super(MediaStream, self).__init__(id_=id_)

        self._position = None
        self._duration = None
        self._codec = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if duration is not None:
            self.duration = duration
        if codec is not None:
            self.codec = codec

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(MediaStream, self), 'openapi_types'):
            types = getattr(super(MediaStream, self), 'openapi_types')

        types.update({
            'position': 'int',
            'duration': 'float',
            'codec': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(MediaStream, self), 'attribute_map'):
            attributes = getattr(super(MediaStream, self), 'attribute_map')

        attributes.update({
            'position': 'position',
            'duration': 'duration',
            'codec': 'codec'
        })
        return attributes

    @property
    def position(self):
        # type: () -> int
        """Gets the position of this MediaStream.

        Position starts from 0 and indicates the position of the stream in the media. 0 means that this is the first stream found in the media

        :return: The position of this MediaStream.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        # type: (int) -> None
        """Sets the position of this MediaStream.

        Position starts from 0 and indicates the position of the stream in the media. 0 means that this is the first stream found in the media

        :param position: The position of this MediaStream.
        :type: int
        """

        if position is not None:
            if not isinstance(position, int):
                raise TypeError("Invalid type for `position`, type has to be `int`")

        self._position = position

    @property
    def duration(self):
        # type: () -> float
        """Gets the duration of this MediaStream.

        Duration of the stream in seconds

        :return: The duration of this MediaStream.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        # type: (float) -> None
        """Sets the duration of this MediaStream.

        Duration of the stream in seconds

        :param duration: The duration of this MediaStream.
        :type: float
        """

        if duration is not None:
            if not isinstance(duration, (float, int)):
                raise TypeError("Invalid type for `duration`, type has to be `float`")

        self._duration = duration

    @property
    def codec(self):
        # type: () -> string_types
        """Gets the codec of this MediaStream.

        Codec of the stream

        :return: The codec of this MediaStream.
        :rtype: string_types
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (string_types) -> None
        """Sets the codec of this MediaStream.

        Codec of the stream

        :param codec: The codec of this MediaStream.
        :type: string_types
        """

        if codec is not None:
            if not isinstance(codec, string_types):
                raise TypeError("Invalid type for `codec`, type has to be `string_types`")

        self._codec = codec

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(MediaStream, self), "to_dict"):
            result = super(MediaStream, self).to_dict()
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
        if not isinstance(other, MediaStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
