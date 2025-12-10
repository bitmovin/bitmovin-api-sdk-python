# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveEncodingHeartbeatIngestStream(object):
    @poscheck_model
    def __init__(self,
                 stream_id=None,
                 media_type=None,
                 width=None,
                 height=None,
                 rate=None,
                 codec=None,
                 aspect_ratio=None,
                 bitrate=None,
                 samples_read_per_second_avg=None,
                 incoming_bitrate=None,
                 key_frame_interval_max=None,
                 key_frame_interval_avg=None,
                 last_timestamp=None,
                 last_timestamp_timescale=None,
                 number_of_audio_channels=None,
                 audio_channel_format=None,
                 last_arrival_time=None,
                 healthy=None):
        # type: (string_types, string_types, int, int, float, string_types, string_types, int, float, float, int, float, int, int, int, string_types, datetime, bool) -> None

        self._stream_id = None
        self._media_type = None
        self._width = None
        self._height = None
        self._rate = None
        self._codec = None
        self._aspect_ratio = None
        self._bitrate = None
        self._samples_read_per_second_avg = None
        self._incoming_bitrate = None
        self._key_frame_interval_max = None
        self._key_frame_interval_avg = None
        self._last_timestamp = None
        self._last_timestamp_timescale = None
        self._number_of_audio_channels = None
        self._audio_channel_format = None
        self._last_arrival_time = None
        self._healthy = None
        self.discriminator = None

        if stream_id is not None:
            self.stream_id = stream_id
        if media_type is not None:
            self.media_type = media_type
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if rate is not None:
            self.rate = rate
        if codec is not None:
            self.codec = codec
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if bitrate is not None:
            self.bitrate = bitrate
        if samples_read_per_second_avg is not None:
            self.samples_read_per_second_avg = samples_read_per_second_avg
        if incoming_bitrate is not None:
            self.incoming_bitrate = incoming_bitrate
        if key_frame_interval_max is not None:
            self.key_frame_interval_max = key_frame_interval_max
        if key_frame_interval_avg is not None:
            self.key_frame_interval_avg = key_frame_interval_avg
        if last_timestamp is not None:
            self.last_timestamp = last_timestamp
        if last_timestamp_timescale is not None:
            self.last_timestamp_timescale = last_timestamp_timescale
        if number_of_audio_channels is not None:
            self.number_of_audio_channels = number_of_audio_channels
        if audio_channel_format is not None:
            self.audio_channel_format = audio_channel_format
        if last_arrival_time is not None:
            self.last_arrival_time = last_arrival_time
        if healthy is not None:
            self.healthy = healthy

    @property
    def openapi_types(self):
        types = {
            'stream_id': 'string_types',
            'media_type': 'string_types',
            'width': 'int',
            'height': 'int',
            'rate': 'float',
            'codec': 'string_types',
            'aspect_ratio': 'string_types',
            'bitrate': 'int',
            'samples_read_per_second_avg': 'float',
            'incoming_bitrate': 'float',
            'key_frame_interval_max': 'int',
            'key_frame_interval_avg': 'float',
            'last_timestamp': 'int',
            'last_timestamp_timescale': 'int',
            'number_of_audio_channels': 'int',
            'audio_channel_format': 'string_types',
            'last_arrival_time': 'datetime',
            'healthy': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_id': 'streamId',
            'media_type': 'mediaType',
            'width': 'width',
            'height': 'height',
            'rate': 'rate',
            'codec': 'codec',
            'aspect_ratio': 'aspectRatio',
            'bitrate': 'bitrate',
            'samples_read_per_second_avg': 'samplesReadPerSecondAvg',
            'incoming_bitrate': 'incomingBitrate',
            'key_frame_interval_max': 'keyFrameIntervalMax',
            'key_frame_interval_avg': 'keyFrameIntervalAvg',
            'last_timestamp': 'lastTimestamp',
            'last_timestamp_timescale': 'lastTimestampTimescale',
            'number_of_audio_channels': 'numberOfAudioChannels',
            'audio_channel_format': 'audioChannelFormat',
            'last_arrival_time': 'lastArrivalTime',
            'healthy': 'healthy'
        }
        return attributes

    @property
    def stream_id(self):
        # type: () -> string_types
        """Gets the stream_id of this LiveEncodingHeartbeatIngestStream.

        Unique identifier of the stream.

        :return: The stream_id of this LiveEncodingHeartbeatIngestStream.
        :rtype: string_types
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        # type: (string_types) -> None
        """Sets the stream_id of this LiveEncodingHeartbeatIngestStream.

        Unique identifier of the stream.

        :param stream_id: The stream_id of this LiveEncodingHeartbeatIngestStream.
        :type: string_types
        """

        if stream_id is not None:
            if not isinstance(stream_id, string_types):
                raise TypeError("Invalid type for `stream_id`, type has to be `string_types`")

        self._stream_id = stream_id

    @property
    def media_type(self):
        # type: () -> string_types
        """Gets the media_type of this LiveEncodingHeartbeatIngestStream.

        Media type for the stream (e.g., \"video\" or \"audio\").

        :return: The media_type of this LiveEncodingHeartbeatIngestStream.
        :rtype: string_types
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        # type: (string_types) -> None
        """Sets the media_type of this LiveEncodingHeartbeatIngestStream.

        Media type for the stream (e.g., \"video\" or \"audio\").

        :param media_type: The media_type of this LiveEncodingHeartbeatIngestStream.
        :type: string_types
        """

        if media_type is not None:
            if not isinstance(media_type, string_types):
                raise TypeError("Invalid type for `media_type`, type has to be `string_types`")

        self._media_type = media_type

    @property
    def width(self):
        # type: () -> int
        """Gets the width of this LiveEncodingHeartbeatIngestStream.

        Width of the video stream in pixels.

        :return: The width of this LiveEncodingHeartbeatIngestStream.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        # type: (int) -> None
        """Sets the width of this LiveEncodingHeartbeatIngestStream.

        Width of the video stream in pixels.

        :param width: The width of this LiveEncodingHeartbeatIngestStream.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

        self._width = width

    @property
    def height(self):
        # type: () -> int
        """Gets the height of this LiveEncodingHeartbeatIngestStream.

        Height of the video stream in pixels.

        :return: The height of this LiveEncodingHeartbeatIngestStream.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        # type: (int) -> None
        """Sets the height of this LiveEncodingHeartbeatIngestStream.

        Height of the video stream in pixels.

        :param height: The height of this LiveEncodingHeartbeatIngestStream.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

        self._height = height

    @property
    def rate(self):
        # type: () -> float
        """Gets the rate of this LiveEncodingHeartbeatIngestStream.

        Frame rate of the video stream.

        :return: The rate of this LiveEncodingHeartbeatIngestStream.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        # type: (float) -> None
        """Sets the rate of this LiveEncodingHeartbeatIngestStream.

        Frame rate of the video stream.

        :param rate: The rate of this LiveEncodingHeartbeatIngestStream.
        :type: float
        """

        if rate is not None:
            if not isinstance(rate, (float, int)):
                raise TypeError("Invalid type for `rate`, type has to be `float`")

        self._rate = rate

    @property
    def codec(self):
        # type: () -> string_types
        """Gets the codec of this LiveEncodingHeartbeatIngestStream.

        Codec of the stream.

        :return: The codec of this LiveEncodingHeartbeatIngestStream.
        :rtype: string_types
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        # type: (string_types) -> None
        """Sets the codec of this LiveEncodingHeartbeatIngestStream.

        Codec of the stream.

        :param codec: The codec of this LiveEncodingHeartbeatIngestStream.
        :type: string_types
        """

        if codec is not None:
            if not isinstance(codec, string_types):
                raise TypeError("Invalid type for `codec`, type has to be `string_types`")

        self._codec = codec

    @property
    def aspect_ratio(self):
        # type: () -> string_types
        """Gets the aspect_ratio of this LiveEncodingHeartbeatIngestStream.

        Aspect ratio of the video.

        :return: The aspect_ratio of this LiveEncodingHeartbeatIngestStream.
        :rtype: string_types
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        # type: (string_types) -> None
        """Sets the aspect_ratio of this LiveEncodingHeartbeatIngestStream.

        Aspect ratio of the video.

        :param aspect_ratio: The aspect_ratio of this LiveEncodingHeartbeatIngestStream.
        :type: string_types
        """

        if aspect_ratio is not None:
            if not isinstance(aspect_ratio, string_types):
                raise TypeError("Invalid type for `aspect_ratio`, type has to be `string_types`")

        self._aspect_ratio = aspect_ratio

    @property
    def bitrate(self):
        # type: () -> int
        """Gets the bitrate of this LiveEncodingHeartbeatIngestStream.

        Container format's bitrate of the stream, in bits per second.

        :return: The bitrate of this LiveEncodingHeartbeatIngestStream.
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        # type: (int) -> None
        """Sets the bitrate of this LiveEncodingHeartbeatIngestStream.

        Container format's bitrate of the stream, in bits per second.

        :param bitrate: The bitrate of this LiveEncodingHeartbeatIngestStream.
        :type: int
        """

        if bitrate is not None:
            if not isinstance(bitrate, int):
                raise TypeError("Invalid type for `bitrate`, type has to be `int`")

        self._bitrate = bitrate

    @property
    def samples_read_per_second_avg(self):
        # type: () -> float
        """Gets the samples_read_per_second_avg of this LiveEncodingHeartbeatIngestStream.

        Average number of samples/frames read per second.

        :return: The samples_read_per_second_avg of this LiveEncodingHeartbeatIngestStream.
        :rtype: float
        """
        return self._samples_read_per_second_avg

    @samples_read_per_second_avg.setter
    def samples_read_per_second_avg(self, samples_read_per_second_avg):
        # type: (float) -> None
        """Sets the samples_read_per_second_avg of this LiveEncodingHeartbeatIngestStream.

        Average number of samples/frames read per second.

        :param samples_read_per_second_avg: The samples_read_per_second_avg of this LiveEncodingHeartbeatIngestStream.
        :type: float
        """

        if samples_read_per_second_avg is not None:
            if not isinstance(samples_read_per_second_avg, (float, int)):
                raise TypeError("Invalid type for `samples_read_per_second_avg`, type has to be `float`")

        self._samples_read_per_second_avg = samples_read_per_second_avg

    @property
    def incoming_bitrate(self):
        # type: () -> float
        """Gets the incoming_bitrate of this LiveEncodingHeartbeatIngestStream.

        Incoming bitrate measured in bits per second.

        :return: The incoming_bitrate of this LiveEncodingHeartbeatIngestStream.
        :rtype: float
        """
        return self._incoming_bitrate

    @incoming_bitrate.setter
    def incoming_bitrate(self, incoming_bitrate):
        # type: (float) -> None
        """Sets the incoming_bitrate of this LiveEncodingHeartbeatIngestStream.

        Incoming bitrate measured in bits per second.

        :param incoming_bitrate: The incoming_bitrate of this LiveEncodingHeartbeatIngestStream.
        :type: float
        """

        if incoming_bitrate is not None:
            if not isinstance(incoming_bitrate, (float, int)):
                raise TypeError("Invalid type for `incoming_bitrate`, type has to be `float`")

        self._incoming_bitrate = incoming_bitrate

    @property
    def key_frame_interval_max(self):
        # type: () -> int
        """Gets the key_frame_interval_max of this LiveEncodingHeartbeatIngestStream.

        Largest encountered key-frame interval in milliseconds.

        :return: The key_frame_interval_max of this LiveEncodingHeartbeatIngestStream.
        :rtype: int
        """
        return self._key_frame_interval_max

    @key_frame_interval_max.setter
    def key_frame_interval_max(self, key_frame_interval_max):
        # type: (int) -> None
        """Sets the key_frame_interval_max of this LiveEncodingHeartbeatIngestStream.

        Largest encountered key-frame interval in milliseconds.

        :param key_frame_interval_max: The key_frame_interval_max of this LiveEncodingHeartbeatIngestStream.
        :type: int
        """

        if key_frame_interval_max is not None:
            if not isinstance(key_frame_interval_max, int):
                raise TypeError("Invalid type for `key_frame_interval_max`, type has to be `int`")

        self._key_frame_interval_max = key_frame_interval_max

    @property
    def key_frame_interval_avg(self):
        # type: () -> float
        """Gets the key_frame_interval_avg of this LiveEncodingHeartbeatIngestStream.

        Average key-frame interval in milliseconds.

        :return: The key_frame_interval_avg of this LiveEncodingHeartbeatIngestStream.
        :rtype: float
        """
        return self._key_frame_interval_avg

    @key_frame_interval_avg.setter
    def key_frame_interval_avg(self, key_frame_interval_avg):
        # type: (float) -> None
        """Sets the key_frame_interval_avg of this LiveEncodingHeartbeatIngestStream.

        Average key-frame interval in milliseconds.

        :param key_frame_interval_avg: The key_frame_interval_avg of this LiveEncodingHeartbeatIngestStream.
        :type: float
        """

        if key_frame_interval_avg is not None:
            if not isinstance(key_frame_interval_avg, (float, int)):
                raise TypeError("Invalid type for `key_frame_interval_avg`, type has to be `float`")

        self._key_frame_interval_avg = key_frame_interval_avg

    @property
    def last_timestamp(self):
        # type: () -> int
        """Gets the last_timestamp of this LiveEncodingHeartbeatIngestStream.

        Last presentation timestamp (PTS) of the stream.

        :return: The last_timestamp of this LiveEncodingHeartbeatIngestStream.
        :rtype: int
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        # type: (int) -> None
        """Sets the last_timestamp of this LiveEncodingHeartbeatIngestStream.

        Last presentation timestamp (PTS) of the stream.

        :param last_timestamp: The last_timestamp of this LiveEncodingHeartbeatIngestStream.
        :type: int
        """

        if last_timestamp is not None:
            if not isinstance(last_timestamp, int):
                raise TypeError("Invalid type for `last_timestamp`, type has to be `int`")

        self._last_timestamp = last_timestamp

    @property
    def last_timestamp_timescale(self):
        # type: () -> int
        """Gets the last_timestamp_timescale of this LiveEncodingHeartbeatIngestStream.

        Timescale of lastTimestamp

        :return: The last_timestamp_timescale of this LiveEncodingHeartbeatIngestStream.
        :rtype: int
        """
        return self._last_timestamp_timescale

    @last_timestamp_timescale.setter
    def last_timestamp_timescale(self, last_timestamp_timescale):
        # type: (int) -> None
        """Sets the last_timestamp_timescale of this LiveEncodingHeartbeatIngestStream.

        Timescale of lastTimestamp

        :param last_timestamp_timescale: The last_timestamp_timescale of this LiveEncodingHeartbeatIngestStream.
        :type: int
        """

        if last_timestamp_timescale is not None:
            if not isinstance(last_timestamp_timescale, int):
                raise TypeError("Invalid type for `last_timestamp_timescale`, type has to be `int`")

        self._last_timestamp_timescale = last_timestamp_timescale

    @property
    def number_of_audio_channels(self):
        # type: () -> int
        """Gets the number_of_audio_channels of this LiveEncodingHeartbeatIngestStream.

        Number of audio channels.

        :return: The number_of_audio_channels of this LiveEncodingHeartbeatIngestStream.
        :rtype: int
        """
        return self._number_of_audio_channels

    @number_of_audio_channels.setter
    def number_of_audio_channels(self, number_of_audio_channels):
        # type: (int) -> None
        """Sets the number_of_audio_channels of this LiveEncodingHeartbeatIngestStream.

        Number of audio channels.

        :param number_of_audio_channels: The number_of_audio_channels of this LiveEncodingHeartbeatIngestStream.
        :type: int
        """

        if number_of_audio_channels is not None:
            if not isinstance(number_of_audio_channels, int):
                raise TypeError("Invalid type for `number_of_audio_channels`, type has to be `int`")

        self._number_of_audio_channels = number_of_audio_channels

    @property
    def audio_channel_format(self):
        # type: () -> string_types
        """Gets the audio_channel_format of this LiveEncodingHeartbeatIngestStream.

        Format of the audio channel.

        :return: The audio_channel_format of this LiveEncodingHeartbeatIngestStream.
        :rtype: string_types
        """
        return self._audio_channel_format

    @audio_channel_format.setter
    def audio_channel_format(self, audio_channel_format):
        # type: (string_types) -> None
        """Sets the audio_channel_format of this LiveEncodingHeartbeatIngestStream.

        Format of the audio channel.

        :param audio_channel_format: The audio_channel_format of this LiveEncodingHeartbeatIngestStream.
        :type: string_types
        """

        if audio_channel_format is not None:
            if not isinstance(audio_channel_format, string_types):
                raise TypeError("Invalid type for `audio_channel_format`, type has to be `string_types`")

        self._audio_channel_format = audio_channel_format

    @property
    def last_arrival_time(self):
        # type: () -> datetime
        """Gets the last_arrival_time of this LiveEncodingHeartbeatIngestStream.

        lastArrivalTime timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The last_arrival_time of this LiveEncodingHeartbeatIngestStream.
        :rtype: datetime
        """
        return self._last_arrival_time

    @last_arrival_time.setter
    def last_arrival_time(self, last_arrival_time):
        # type: (datetime) -> None
        """Sets the last_arrival_time of this LiveEncodingHeartbeatIngestStream.

        lastArrivalTime timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param last_arrival_time: The last_arrival_time of this LiveEncodingHeartbeatIngestStream.
        :type: datetime
        """

        if last_arrival_time is not None:
            if not isinstance(last_arrival_time, datetime):
                raise TypeError("Invalid type for `last_arrival_time`, type has to be `datetime`")

        self._last_arrival_time = last_arrival_time

    @property
    def healthy(self):
        # type: () -> bool
        """Gets the healthy of this LiveEncodingHeartbeatIngestStream.

        Indicates whether this particular stream is healthy.

        :return: The healthy of this LiveEncodingHeartbeatIngestStream.
        :rtype: bool
        """
        return self._healthy

    @healthy.setter
    def healthy(self, healthy):
        # type: (bool) -> None
        """Sets the healthy of this LiveEncodingHeartbeatIngestStream.

        Indicates whether this particular stream is healthy.

        :param healthy: The healthy of this LiveEncodingHeartbeatIngestStream.
        :type: bool
        """

        if healthy is not None:
            if not isinstance(healthy, bool):
                raise TypeError("Invalid type for `healthy`, type has to be `bool`")

        self._healthy = healthy

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
        if not isinstance(other, LiveEncodingHeartbeatIngestStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
