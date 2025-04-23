# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.caption_character_encoding import CaptionCharacterEncoding
from bitmovin_api_sdk.models.input_path import InputPath
import pprint
import six


class BurnInSubtitleAssa(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 character_encoding=None,
                 input_=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, CaptionCharacterEncoding, InputPath) -> None
        super(BurnInSubtitleAssa, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._character_encoding = None
        self._input = None
        self.discriminator = None

        if character_encoding is not None:
            self.character_encoding = character_encoding
        if input_ is not None:
            self.input = input_

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(BurnInSubtitleAssa, self), 'openapi_types'):
            types = getattr(super(BurnInSubtitleAssa, self), 'openapi_types')

        types.update({
            'character_encoding': 'CaptionCharacterEncoding',
            'input': 'InputPath'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(BurnInSubtitleAssa, self), 'attribute_map'):
            attributes = getattr(super(BurnInSubtitleAssa, self), 'attribute_map')

        attributes.update({
            'character_encoding': 'characterEncoding',
            'input': 'input'
        })
        return attributes

    @property
    def character_encoding(self):
        # type: () -> CaptionCharacterEncoding
        """Gets the character_encoding of this BurnInSubtitleAssa.

        Character encoding of the ASSA file (required)

        :return: The character_encoding of this BurnInSubtitleAssa.
        :rtype: CaptionCharacterEncoding
        """
        return self._character_encoding

    @character_encoding.setter
    def character_encoding(self, character_encoding):
        # type: (CaptionCharacterEncoding) -> None
        """Sets the character_encoding of this BurnInSubtitleAssa.

        Character encoding of the ASSA file (required)

        :param character_encoding: The character_encoding of this BurnInSubtitleAssa.
        :type: CaptionCharacterEncoding
        """

        if character_encoding is not None:
            if not isinstance(character_encoding, CaptionCharacterEncoding):
                raise TypeError("Invalid type for `character_encoding`, type has to be `CaptionCharacterEncoding`")

        self._character_encoding = character_encoding

    @property
    def input(self):
        # type: () -> InputPath
        """Gets the input of this BurnInSubtitleAssa.

        The input location to get the ASSA file from (required)

        :return: The input of this BurnInSubtitleAssa.
        :rtype: InputPath
        """
        return self._input

    @input.setter
    def input(self, input_):
        # type: (InputPath) -> None
        """Sets the input of this BurnInSubtitleAssa.

        The input location to get the ASSA file from (required)

        :param input_: The input of this BurnInSubtitleAssa.
        :type: InputPath
        """

        if input_ is not None:
            if not isinstance(input_, InputPath):
                raise TypeError("Invalid type for `input`, type has to be `InputPath`")

        self._input = input_

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(BurnInSubtitleAssa, self), "to_dict"):
            result = super(BurnInSubtitleAssa, self).to_dict()
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
        if not isinstance(other, BurnInSubtitleAssa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
