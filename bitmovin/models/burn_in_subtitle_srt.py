# coding: utf-8

from bitmovin.models.bitmovin_resource import BitmovinResource
from bitmovin.models.caption_character_encoding import CaptionCharacterEncoding
from bitmovin.models.input_path import InputPath
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class BurnInSubtitleSrt(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(BurnInSubtitleSrt, self).openapi_types
        types.update({
            'character_encoding': 'CaptionCharacterEncoding',
            'input': 'InputPath'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(BurnInSubtitleSrt, self).attribute_map
        attributes.update({
            'character_encoding': 'characterEncoding',
            'input': 'input'
        })
        return attributes

    def __init__(self, character_encoding=None, input=None, *args, **kwargs):
        super(BurnInSubtitleSrt, self).__init__(*args, **kwargs)

        self._character_encoding = None
        self._input = None
        self.discriminator = None

        if character_encoding is not None:
            self.character_encoding = character_encoding
        if input is not None:
            self.input = input

    @property
    def character_encoding(self):
        """Gets the character_encoding of this BurnInSubtitleSrt.

        Character encoding of the SRT file (required)

        :return: The character_encoding of this BurnInSubtitleSrt.
        :rtype: CaptionCharacterEncoding
        """
        return self._character_encoding

    @character_encoding.setter
    def character_encoding(self, character_encoding):
        """Sets the character_encoding of this BurnInSubtitleSrt.

        Character encoding of the SRT file (required)

        :param character_encoding: The character_encoding of this BurnInSubtitleSrt.
        :type: CaptionCharacterEncoding
        """

        if character_encoding is not None:
            if not isinstance(character_encoding, CaptionCharacterEncoding):
                raise TypeError("Invalid type for `character_encoding`, type has to be `CaptionCharacterEncoding`")

        self._character_encoding = character_encoding


    @property
    def input(self):
        """Gets the input of this BurnInSubtitleSrt.

        The input location to get the SRT file from (required)

        :return: The input of this BurnInSubtitleSrt.
        :rtype: InputPath
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this BurnInSubtitleSrt.

        The input location to get the SRT file from (required)

        :param input: The input of this BurnInSubtitleSrt.
        :type: InputPath
        """

        if input is not None:
            if not isinstance(input, InputPath):
                raise TypeError("Invalid type for `input`, type has to be `InputPath`")

        self._input = input

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(BurnInSubtitleSrt, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(BurnInSubtitleSrt, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BurnInSubtitleSrt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
