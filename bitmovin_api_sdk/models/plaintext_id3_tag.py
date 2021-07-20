# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.id3_tag import Id3Tag
from bitmovin_api_sdk.models.id3_tag_position_mode import Id3TagPositionMode
import pprint
import six


class PlaintextId3Tag(Id3Tag):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 position_mode=None,
                 frame=None,
                 time=None,
                 text=None,
                 frame_id=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, Id3TagPositionMode, int, float, string_types, string_types) -> None
        super(PlaintextId3Tag, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, position_mode=position_mode, frame=frame, time=time)

        self._text = None
        self._frame_id = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if frame_id is not None:
            self.frame_id = frame_id

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(PlaintextId3Tag, self), 'openapi_types'):
            types = getattr(super(PlaintextId3Tag, self), 'openapi_types')

        types.update({
            'text': 'string_types',
            'frame_id': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(PlaintextId3Tag, self), 'attribute_map'):
            attributes = getattr(super(PlaintextId3Tag, self), 'attribute_map')

        attributes.update({
            'text': 'text',
            'frame_id': 'frameId'
        })
        return attributes

    @property
    def text(self):
        # type: () -> string_types
        """Gets the text of this PlaintextId3Tag.

        Plain Text Data (required)

        :return: The text of this PlaintextId3Tag.
        :rtype: string_types
        """
        return self._text

    @text.setter
    def text(self, text):
        # type: (string_types) -> None
        """Sets the text of this PlaintextId3Tag.

        Plain Text Data (required)

        :param text: The text of this PlaintextId3Tag.
        :type: string_types
        """

        if text is not None:
            if not isinstance(text, string_types):
                raise TypeError("Invalid type for `text`, type has to be `string_types`")

        self._text = text

    @property
    def frame_id(self):
        # type: () -> string_types
        """Gets the frame_id of this PlaintextId3Tag.

        4 character long Frame ID (required)

        :return: The frame_id of this PlaintextId3Tag.
        :rtype: string_types
        """
        return self._frame_id

    @frame_id.setter
    def frame_id(self, frame_id):
        # type: (string_types) -> None
        """Sets the frame_id of this PlaintextId3Tag.

        4 character long Frame ID (required)

        :param frame_id: The frame_id of this PlaintextId3Tag.
        :type: string_types
        """

        if frame_id is not None:
            if not isinstance(frame_id, string_types):
                raise TypeError("Invalid type for `frame_id`, type has to be `string_types`")

        self._frame_id = frame_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(PlaintextId3Tag, self), "to_dict"):
            result = super(PlaintextId3Tag, self).to_dict()
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
        if not isinstance(other, PlaintextId3Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
