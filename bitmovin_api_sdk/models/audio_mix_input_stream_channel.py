# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.audio_mix_channel_type import AudioMixChannelType
import pprint
import six


class AudioMixInputStreamChannel(object):
    @poscheck_model
    def __init__(self,
                 input_stream_id=None,
                 output_channel_type=None,
                 output_channel_number=None,
                 source_channels=None):
        # type: (string_types, AudioMixChannelType, int, list[AudioMixInputStreamSourceChannel]) -> None

        self._input_stream_id = None
        self._output_channel_type = None
        self._output_channel_number = None
        self._source_channels = list()
        self.discriminator = None

        if input_stream_id is not None:
            self.input_stream_id = input_stream_id
        if output_channel_type is not None:
            self.output_channel_type = output_channel_type
        if output_channel_number is not None:
            self.output_channel_number = output_channel_number
        if source_channels is not None:
            self.source_channels = source_channels

    @property
    def openapi_types(self):
        types = {
            'input_stream_id': 'string_types',
            'output_channel_type': 'AudioMixChannelType',
            'output_channel_number': 'int',
            'source_channels': 'list[AudioMixInputStreamSourceChannel]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'input_stream_id': 'inputStreamId',
            'output_channel_type': 'outputChannelType',
            'output_channel_number': 'outputChannelNumber',
            'source_channels': 'sourceChannels'
        }
        return attributes

    @property
    def input_stream_id(self):
        # type: () -> string_types
        """Gets the input_stream_id of this AudioMixInputStreamChannel.

        The id of the input stream that should be used for mixing.

        :return: The input_stream_id of this AudioMixInputStreamChannel.
        :rtype: string_types
        """
        return self._input_stream_id

    @input_stream_id.setter
    def input_stream_id(self, input_stream_id):
        # type: (string_types) -> None
        """Sets the input_stream_id of this AudioMixInputStreamChannel.

        The id of the input stream that should be used for mixing.

        :param input_stream_id: The input_stream_id of this AudioMixInputStreamChannel.
        :type: string_types
        """

        if input_stream_id is not None:
            if not isinstance(input_stream_id, string_types):
                raise TypeError("Invalid type for `input_stream_id`, type has to be `string_types`")

        self._input_stream_id = input_stream_id

    @property
    def output_channel_type(self):
        # type: () -> AudioMixChannelType
        """Gets the output_channel_type of this AudioMixInputStreamChannel.


        :return: The output_channel_type of this AudioMixInputStreamChannel.
        :rtype: AudioMixChannelType
        """
        return self._output_channel_type

    @output_channel_type.setter
    def output_channel_type(self, output_channel_type):
        # type: (AudioMixChannelType) -> None
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
        # type: () -> int
        """Gets the output_channel_number of this AudioMixInputStreamChannel.

        Number of this output channel. If type is 'CHANNEL_NUMBER', this must be set.

        :return: The output_channel_number of this AudioMixInputStreamChannel.
        :rtype: int
        """
        return self._output_channel_number

    @output_channel_number.setter
    def output_channel_number(self, output_channel_number):
        # type: (int) -> None
        """Sets the output_channel_number of this AudioMixInputStreamChannel.

        Number of this output channel. If type is 'CHANNEL_NUMBER', this must be set.

        :param output_channel_number: The output_channel_number of this AudioMixInputStreamChannel.
        :type: int
        """

        if output_channel_number is not None:
            if not isinstance(output_channel_number, int):
                raise TypeError("Invalid type for `output_channel_number`, type has to be `int`")

        self._output_channel_number = output_channel_number

    @property
    def source_channels(self):
        # type: () -> list[AudioMixInputStreamSourceChannel]
        """Gets the source_channels of this AudioMixInputStreamChannel.

        List of source channels to be mixed

        :return: The source_channels of this AudioMixInputStreamChannel.
        :rtype: list[AudioMixInputStreamSourceChannel]
        """
        return self._source_channels

    @source_channels.setter
    def source_channels(self, source_channels):
        # type: (list) -> None
        """Sets the source_channels of this AudioMixInputStreamChannel.

        List of source channels to be mixed

        :param source_channels: The source_channels of this AudioMixInputStreamChannel.
        :type: list[AudioMixInputStreamSourceChannel]
        """

        if source_channels is not None:
            if not isinstance(source_channels, list):
                raise TypeError("Invalid type for `source_channels`, type has to be `list[AudioMixInputStreamSourceChannel]`")

        self._source_channels = source_channels

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
        if not isinstance(other, AudioMixInputStreamChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
