# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.caption_character_encoding import CaptionCharacterEncoding
from bitmovin_api_sdk.models.cea608_channel_type import Cea608ChannelType
from bitmovin_api_sdk.models.input_path import InputPath
import pprint
import six


class SrtToCea608708Caption(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 input_=None,
                 cc_channel=None,
                 character_encoding=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, InputPath, Cea608ChannelType, CaptionCharacterEncoding) -> None
        super(SrtToCea608708Caption, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._input = None
        self._cc_channel = None
        self._character_encoding = None
        self.discriminator = None

        if input_ is not None:
            self.input = input_
        if cc_channel is not None:
            self.cc_channel = cc_channel
        if character_encoding is not None:
            self.character_encoding = character_encoding

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(SrtToCea608708Caption, self), 'openapi_types'):
            types = getattr(super(SrtToCea608708Caption, self), 'openapi_types')

        types.update({
            'input': 'InputPath',
            'cc_channel': 'Cea608ChannelType',
            'character_encoding': 'CaptionCharacterEncoding'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(SrtToCea608708Caption, self), 'attribute_map'):
            attributes = getattr(super(SrtToCea608708Caption, self), 'attribute_map')

        attributes.update({
            'input': 'input',
            'cc_channel': 'ccChannel',
            'character_encoding': 'characterEncoding'
        })
        return attributes

    @property
    def input(self):
        # type: () -> InputPath
        """Gets the input of this SrtToCea608708Caption.

        Input location of the SRT file (required)

        :return: The input of this SrtToCea608708Caption.
        :rtype: InputPath
        """
        return self._input

    @input.setter
    def input(self, input_):
        # type: (InputPath) -> None
        """Sets the input of this SrtToCea608708Caption.

        Input location of the SRT file (required)

        :param input_: The input of this SrtToCea608708Caption.
        :type: InputPath
        """

        if input_ is not None:
            if not isinstance(input_, InputPath):
                raise TypeError("Invalid type for `input`, type has to be `InputPath`")

        self._input = input_

    @property
    def cc_channel(self):
        # type: () -> Cea608ChannelType
        """Gets the cc_channel of this SrtToCea608708Caption.

        The channel number to embed the CEA subtitles in (required)

        :return: The cc_channel of this SrtToCea608708Caption.
        :rtype: Cea608ChannelType
        """
        return self._cc_channel

    @cc_channel.setter
    def cc_channel(self, cc_channel):
        # type: (Cea608ChannelType) -> None
        """Sets the cc_channel of this SrtToCea608708Caption.

        The channel number to embed the CEA subtitles in (required)

        :param cc_channel: The cc_channel of this SrtToCea608708Caption.
        :type: Cea608ChannelType
        """

        if cc_channel is not None:
            if not isinstance(cc_channel, Cea608ChannelType):
                raise TypeError("Invalid type for `cc_channel`, type has to be `Cea608ChannelType`")

        self._cc_channel = cc_channel

    @property
    def character_encoding(self):
        # type: () -> CaptionCharacterEncoding
        """Gets the character_encoding of this SrtToCea608708Caption.

        Character encoding of the input SRT file (required)

        :return: The character_encoding of this SrtToCea608708Caption.
        :rtype: CaptionCharacterEncoding
        """
        return self._character_encoding

    @character_encoding.setter
    def character_encoding(self, character_encoding):
        # type: (CaptionCharacterEncoding) -> None
        """Sets the character_encoding of this SrtToCea608708Caption.

        Character encoding of the input SRT file (required)

        :param character_encoding: The character_encoding of this SrtToCea608708Caption.
        :type: CaptionCharacterEncoding
        """

        if character_encoding is not None:
            if not isinstance(character_encoding, CaptionCharacterEncoding):
                raise TypeError("Invalid type for `character_encoding`, type has to be `CaptionCharacterEncoding`")

        self._character_encoding = character_encoding

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(SrtToCea608708Caption, self), "to_dict"):
            result = super(SrtToCea608708Caption, self).to_dict()
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
        if not isinstance(other, SrtToCea608708Caption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
