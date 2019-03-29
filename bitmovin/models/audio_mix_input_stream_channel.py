# coding: utf-8

from bitmovin.models.audio_mix_channel_type import AudioMixChannelType
import pprint
import six
from datetime import datetime
from enum import Enum


class AudioMixInputStreamChannel(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'input_stream_id': 'str',
            'output_channel_type': 'AudioMixChannelType',
            'output_channel_number': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'input_stream_id': 'inputStreamId',
            'output_channel_type': 'outputChannelType',
            'output_channel_number': 'outputChannelNumber'
        }
        return attributes

    def __init__(self, input_stream_id=None, output_channel_type=None, output_channel_number=None, *args, **kwargs):

        self._input_stream_id = None
        self._output_channel_type = None
        self._output_channel_number = None
        self.discriminator = None

        if input_stream_id is not None:
            self.input_stream_id = input_stream_id
        self.output_channel_type = output_channel_type
        if output_channel_number is not None:
            self.output_channel_number = output_channel_number

    @property
    def input_stream_id(self):
        """Gets the input_stream_id of this AudioMixInputStreamChannel.

        The id of the input stream that should be used for mixing.

        :return: The input_stream_id of this AudioMixInputStreamChannel.
        :rtype: str
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        """Sets the input_stream_id of this AudioMixInputStreamChannel.

        The id of the input stream that should be used for mixing.

        :param input_stream_id: The input_stream_id of this AudioMixInputStreamChannel.
        :type: str
        """

        if input_stream_id is not None:
            if not isinstance(input_stream_id, str):
                raise TypeError("Invalid type for `input_stream_id`, type has to be `str`")

            self._input_stream_id = input_stream_id


    @property
    def output_channel_type(self):
        """Gets the output_channel_type of this AudioMixInputStreamChannel.


        :return: The output_channel_type of this AudioMixInputStreamChannel.
        :rtype: AudioMixChannelType
        """
        return self._output_channel_type

    @output_channel_type.setter
    def output_channel_type(self, output_channel_type):
        """Sets the output_channel_type of this AudioMixInputStreamChannel.


        :param output_channel_type: The output_channel_type of this AudioMixInputStreamChannel.
        :type: AudioMixChannelType
        """

        if output_channel_type is not None:
            if not isinstance(output_channel_type, AudioMixChannelType):
                raise TypeError("Invalid type for `output_channel_type`, type has to be `AudioMixChannelType`")

            self._output_channel_type = output_channel_type


    @property
    def output_channel_number(self):
        """Gets the output_channel_number of this AudioMixInputStreamChannel.

        Number of this output channel. If type is 'CHANNEL_NUMBER', this must be set.

        :return: The output_channel_number of this AudioMixInputStreamChannel.
        :rtype: int
        """
        return self._output_channel_number

    @output_channel_number.setter
    def output_channel_number(self, output_channel_number):
        """Sets the output_channel_number of this AudioMixInputStreamChannel.

        Number of this output channel. If type is 'CHANNEL_NUMBER', this must be set.

        :param output_channel_number: The output_channel_number of this AudioMixInputStreamChannel.
        :type: int
        """

        if output_channel_number is not None:
            if not isinstance(output_channel_number, int):
                raise TypeError("Invalid type for `output_channel_number`, type has to be `int`")

            self._output_channel_number = output_channel_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
            if issubclass(AudioMixInputStreamChannel, dict):
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
        if not isinstance(other, AudioMixInputStreamChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
