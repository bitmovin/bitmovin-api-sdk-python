# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.input_stream import InputStream
import pprint
import six


class Cea708CaptionInputStream(InputStream):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 input_id=None,
                 input_path=None,
                 channel=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, string_types, string_types, int) -> None
        super(Cea708CaptionInputStream, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._input_id = None
        self._input_path = None
        self._channel = None
        self.discriminator = None

        if input_id is not None:
            self.input_id = input_id
        if input_path is not None:
            self.input_path = input_path
        if channel is not None:
            self.channel = channel

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Cea708CaptionInputStream, self), 'openapi_types'):
            types = getattr(super(Cea708CaptionInputStream, self), 'openapi_types')

        types.update({
            'input_id': 'string_types',
            'input_path': 'string_types',
            'channel': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Cea708CaptionInputStream, self), 'attribute_map'):
            attributes = getattr(super(Cea708CaptionInputStream, self), 'attribute_map')

        attributes.update({
            'input_id': 'inputId',
            'input_path': 'inputPath',
            'channel': 'channel'
        })
        return attributes

    @property
    def input_id(self):
        # type: () -> string_types
        """Gets the input_id of this Cea708CaptionInputStream.

        Id of the Input (required)

        :return: The input_id of this Cea708CaptionInputStream.
        :rtype: string_types
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        # type: (string_types) -> None
        """Sets the input_id of this Cea708CaptionInputStream.

        Id of the Input (required)

        :param input_id: The input_id of this Cea708CaptionInputStream.
        :type: string_types
        """

        if input_id is not None:
            if not isinstance(input_id, string_types):
                raise TypeError("Invalid type for `input_id`, type has to be `string_types`")

        self._input_id = input_id

    @property
    def input_path(self):
        # type: () -> string_types
        """Gets the input_path of this Cea708CaptionInputStream.

        Path to media file (required)

        :return: The input_path of this Cea708CaptionInputStream.
        :rtype: string_types
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        # type: (string_types) -> None
        """Sets the input_path of this Cea708CaptionInputStream.

        Path to media file (required)

        :param input_path: The input_path of this Cea708CaptionInputStream.
        :type: string_types
        """

        if input_path is not None:
            if not isinstance(input_path, string_types):
                raise TypeError("Invalid type for `input_path`, type has to be `string_types`")

        self._input_path = input_path

    @property
    def channel(self):
        # type: () -> int
        """Gets the channel of this Cea708CaptionInputStream.

        The channel number of the subtitle on the respective stream position. Must not be smaller than 1 (required)

        :return: The channel of this Cea708CaptionInputStream.
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        # type: (int) -> None
        """Sets the channel of this Cea708CaptionInputStream.

        The channel number of the subtitle on the respective stream position. Must not be smaller than 1 (required)

        :param channel: The channel of this Cea708CaptionInputStream.
        :type: int
        """

        if channel is not None:
            if not isinstance(channel, int):
                raise TypeError("Invalid type for `channel`, type has to be `int`")

        self._channel = channel

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Cea708CaptionInputStream, self), "to_dict"):
            result = super(Cea708CaptionInputStream, self).to_dict()
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
        if not isinstance(other, Cea708CaptionInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
