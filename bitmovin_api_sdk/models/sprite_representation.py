# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class SpriteRepresentation(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 encoding_id=None,
                 stream_id=None,
                 sprite_id=None,
                 segment_path=None):
        # type: (string_types, string_types, string_types, string_types, string_types) -> None
        super(SpriteRepresentation, self).__init__(id_=id_)

        self._encoding_id = None
        self._stream_id = None
        self._sprite_id = None
        self._segment_path = None
        self.discriminator = None

        if encoding_id is not None:
            self.encoding_id = encoding_id
        if stream_id is not None:
            self.stream_id = stream_id
        if sprite_id is not None:
            self.sprite_id = sprite_id
        if segment_path is not None:
            self.segment_path = segment_path

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SpriteRepresentation, self), 'openapi_types'):
            types = getattr(super(SpriteRepresentation, self), 'openapi_types')

        types.update({
            'encoding_id': 'string_types',
            'stream_id': 'string_types',
            'sprite_id': 'string_types',
            'segment_path': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SpriteRepresentation, self), 'attribute_map'):
            attributes = getattr(super(SpriteRepresentation, self), 'attribute_map')

        attributes.update({
            'encoding_id': 'encodingId',
            'stream_id': 'streamId',
            'sprite_id': 'spriteId',
            'segment_path': 'segmentPath'
        })
        return attributes

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this SpriteRepresentation.

        UUID of an encoding (required)

        :return: The encoding_id of this SpriteRepresentation.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this SpriteRepresentation.

        UUID of an encoding (required)

        :param encoding_id: The encoding_id of this SpriteRepresentation.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def stream_id(self):
        # type: () -> string_types
        """Gets the stream_id of this SpriteRepresentation.

        UUID of a stream (required)

        :return: The stream_id of this SpriteRepresentation.
        :rtype: string_types
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        # type: (string_types) -> None
        """Sets the stream_id of this SpriteRepresentation.

        UUID of a stream (required)

        :param stream_id: The stream_id of this SpriteRepresentation.
        :type: string_types
        """

        if stream_id is not None:
            if not isinstance(stream_id, string_types):
                raise TypeError("Invalid type for `stream_id`, type has to be `string_types`")

        self._stream_id = stream_id

    @property
    def sprite_id(self):
        # type: () -> string_types
        """Gets the sprite_id of this SpriteRepresentation.

        UUID of a Sprite (required)

        :return: The sprite_id of this SpriteRepresentation.
        :rtype: string_types
        """
        return self._sprite_id

    @sprite_id.setter
    def sprite_id(self, sprite_id):
        # type: (string_types) -> None
        """Sets the sprite_id of this SpriteRepresentation.

        UUID of a Sprite (required)

        :param sprite_id: The sprite_id of this SpriteRepresentation.
        :type: string_types
        """

        if sprite_id is not None:
            if not isinstance(sprite_id, string_types):
                raise TypeError("Invalid type for `sprite_id`, type has to be `string_types`")

        self._sprite_id = sprite_id

    @property
    def segment_path(self):
        # type: () -> string_types
        """Gets the segment_path of this SpriteRepresentation.

        Path to sprite segments. Will be used as the representation id in the manifest. (required)

        :return: The segment_path of this SpriteRepresentation.
        :rtype: string_types
        """
        return self._segment_path

    @segment_path.setter
    def segment_path(self, segment_path):
        # type: (string_types) -> None
        """Sets the segment_path of this SpriteRepresentation.

        Path to sprite segments. Will be used as the representation id in the manifest. (required)

        :param segment_path: The segment_path of this SpriteRepresentation.
        :type: string_types
        """

        if segment_path is not None:
            if not isinstance(segment_path, string_types):
                raise TypeError("Invalid type for `segment_path`, type has to be `string_types`")

        self._segment_path = segment_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SpriteRepresentation, self), "to_dict"):
            result = super(SpriteRepresentation, self).to_dict()
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
        if not isinstance(other, SpriteRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
