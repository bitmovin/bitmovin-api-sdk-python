# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class BroadcastTsSubtitleInputStreamConfiguration(object):
    @poscheck_model
    def __init__(self,
                 stream_id=None,
                 packet_identifier=None,
                 rate=None):
        # type: (string_types, int, int) -> None

        self._stream_id = None
        self._packet_identifier = None
        self._rate = None
        self.discriminator = None

        if stream_id is not None:
            self.stream_id = stream_id
        if packet_identifier is not None:
            self.packet_identifier = packet_identifier
        if rate is not None:
            self.rate = rate

    @property
    def openapi_types(self):
        types = {
            'stream_id': 'string_types',
            'packet_identifier': 'int',
            'rate': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_id': 'streamId',
            'packet_identifier': 'packetIdentifier',
            'rate': 'rate'
        }
        return attributes

    @property
    def stream_id(self):
        # type: () -> string_types
        """Gets the stream_id of this BroadcastTsSubtitleInputStreamConfiguration.

        The UUID of the subtitle stream to which this configuration belongs to. This has to be an ID of an subtitle stream that has been added to the current muxing. 

        :return: The stream_id of this BroadcastTsSubtitleInputStreamConfiguration.
        :rtype: string_types
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        # type: (string_types) -> None
        """Sets the stream_id of this BroadcastTsSubtitleInputStreamConfiguration.

        The UUID of the subtitle stream to which this configuration belongs to. This has to be an ID of an subtitle stream that has been added to the current muxing. 

        :param stream_id: The stream_id of this BroadcastTsSubtitleInputStreamConfiguration.
        :type: string_types
        """

        if stream_id is not None:
            if not isinstance(stream_id, string_types):
                raise TypeError("Invalid type for `stream_id`, type has to be `string_types`")

        self._stream_id = stream_id

    @property
    def packet_identifier(self):
        # type: () -> int
        """Gets the packet_identifier of this BroadcastTsSubtitleInputStreamConfiguration.

        An integer value. Packet Identifier (PID) for this stream.

        :return: The packet_identifier of this BroadcastTsSubtitleInputStreamConfiguration.
        :rtype: int
        """
        return self._packet_identifier

    @packet_identifier.setter
    def packet_identifier(self, packet_identifier):
        # type: (int) -> None
        """Sets the packet_identifier of this BroadcastTsSubtitleInputStreamConfiguration.

        An integer value. Packet Identifier (PID) for this stream.

        :param packet_identifier: The packet_identifier of this BroadcastTsSubtitleInputStreamConfiguration.
        :type: int
        """

        if packet_identifier is not None:
            if packet_identifier is not None and packet_identifier > 8190:
                raise ValueError("Invalid value for `packet_identifier`, must be a value less than or equal to `8190`")
            if packet_identifier is not None and packet_identifier < 16:
                raise ValueError("Invalid value for `packet_identifier`, must be a value greater than or equal to `16`")
            if not isinstance(packet_identifier, int):
                raise TypeError("Invalid type for `packet_identifier`, type has to be `int`")

        self._packet_identifier = packet_identifier

    @property
    def rate(self):
        # type: () -> int
        """Gets the rate of this BroadcastTsSubtitleInputStreamConfiguration.

        The rate parameter determines the maximum rate in bits per second that should be used for the subtitle stream. The valid range is `100` to `60 000 000` bps or `0`. If the value is set to 0, we will examine the first 100 packets of subtitle packet data and use the highest rate that was computed. If the value is set too low, not enough to accommodate the subtitle bit-rate, then some PES packets corresponding to DVB subtitle stream will be dropped. This parameter is optional and the default value is 0. 

        :return: The rate of this BroadcastTsSubtitleInputStreamConfiguration.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        # type: (int) -> None
        """Sets the rate of this BroadcastTsSubtitleInputStreamConfiguration.

        The rate parameter determines the maximum rate in bits per second that should be used for the subtitle stream. The valid range is `100` to `60 000 000` bps or `0`. If the value is set to 0, we will examine the first 100 packets of subtitle packet data and use the highest rate that was computed. If the value is set too low, not enough to accommodate the subtitle bit-rate, then some PES packets corresponding to DVB subtitle stream will be dropped. This parameter is optional and the default value is 0. 

        :param rate: The rate of this BroadcastTsSubtitleInputStreamConfiguration.
        :type: int
        """

        if rate is not None:
            if rate is not None and rate > 60000000:
                raise ValueError("Invalid value for `rate`, must be a value less than or equal to `60000000`")
            if rate is not None and rate < 0:
                raise ValueError("Invalid value for `rate`, must be a value greater than or equal to `0`")
            if not isinstance(rate, int):
                raise TypeError("Invalid type for `rate`, type has to be `int`")

        self._rate = rate

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
        if not isinstance(other, BroadcastTsSubtitleInputStreamConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
