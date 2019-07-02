# coding: utf-8

from bitmovin.models.input_stream import InputStream
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class Cea708CaptionInputStream(InputStream):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Cea708CaptionInputStream, self).openapi_types
        types.update({
            'input_id': 'str',
            'input_path': 'str',
            'channel': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Cea708CaptionInputStream, self).attribute_map
        attributes.update({
            'input_id': 'inputId',
            'input_path': 'inputPath',
            'channel': 'channel'
        })
        return attributes

    def __init__(self, input_id=None, input_path=None, channel=None, *args, **kwargs):
        super(Cea708CaptionInputStream, self).__init__(*args, **kwargs)

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
    def input_id(self):
        """Gets the input_id of this Cea708CaptionInputStream.

        Id of the Input (required)

        :return: The input_id of this Cea708CaptionInputStream.
        :rtype: str
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        """Sets the input_id of this Cea708CaptionInputStream.

        Id of the Input (required)

        :param input_id: The input_id of this Cea708CaptionInputStream.
        :type: str
        """

        if input_id is not None:
            if not isinstance(input_id, str):
                raise TypeError("Invalid type for `input_id`, type has to be `str`")

        self._input_id = input_id


    @property
    def input_path(self):
        """Gets the input_path of this Cea708CaptionInputStream.

        Path to media file (required)

        :return: The input_path of this Cea708CaptionInputStream.
        :rtype: str
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        """Sets the input_path of this Cea708CaptionInputStream.

        Path to media file (required)

        :param input_path: The input_path of this Cea708CaptionInputStream.
        :type: str
        """

        if input_path is not None:
            if not isinstance(input_path, str):
                raise TypeError("Invalid type for `input_path`, type has to be `str`")

        self._input_path = input_path


    @property
    def channel(self):
        """Gets the channel of this Cea708CaptionInputStream.

        The channel number of the subtitle on the respective stream position. Must not be smaller than 1 (required)

        :return: The channel of this Cea708CaptionInputStream.
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
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
        result = super(Cea708CaptionInputStream, self).to_dict()

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
            if issubclass(Cea708CaptionInputStream, dict):
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
        if not isinstance(other, Cea708CaptionInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
