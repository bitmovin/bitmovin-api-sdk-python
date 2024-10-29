# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveAutoShutdownConfiguration(object):
    @poscheck_model
    def __init__(self,
                 bytes_read_timeout_seconds=None,
                 stream_timeout_minutes=None,
                 waiting_for_first_connect_timeout_minutes=None):
        # type: (int, int, int) -> None

        self._bytes_read_timeout_seconds = None
        self._stream_timeout_minutes = None
        self._waiting_for_first_connect_timeout_minutes = None
        self.discriminator = None

        if bytes_read_timeout_seconds is not None:
            self.bytes_read_timeout_seconds = bytes_read_timeout_seconds
        if stream_timeout_minutes is not None:
            self.stream_timeout_minutes = stream_timeout_minutes
        if waiting_for_first_connect_timeout_minutes is not None:
            self.waiting_for_first_connect_timeout_minutes = waiting_for_first_connect_timeout_minutes

    @property
    def openapi_types(self):
        types = {
            'bytes_read_timeout_seconds': 'int',
            'stream_timeout_minutes': 'int',
            'waiting_for_first_connect_timeout_minutes': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'bytes_read_timeout_seconds': 'bytesReadTimeoutSeconds',
            'stream_timeout_minutes': 'streamTimeoutMinutes',
            'waiting_for_first_connect_timeout_minutes': 'waitingForFirstConnectTimeoutMinutes'
        }
        return attributes

    @property
    def bytes_read_timeout_seconds(self):
        # type: () -> int
        """Gets the bytes_read_timeout_seconds of this LiveAutoShutdownConfiguration.

        Automatically shutdown the live stream if there is no input anymore for a predefined number of seconds.

        :return: The bytes_read_timeout_seconds of this LiveAutoShutdownConfiguration.
        :rtype: int
        """
        return self._bytes_read_timeout_seconds

    @bytes_read_timeout_seconds.setter
    def bytes_read_timeout_seconds(self, bytes_read_timeout_seconds):
        # type: (int) -> None
        """Sets the bytes_read_timeout_seconds of this LiveAutoShutdownConfiguration.

        Automatically shutdown the live stream if there is no input anymore for a predefined number of seconds.

        :param bytes_read_timeout_seconds: The bytes_read_timeout_seconds of this LiveAutoShutdownConfiguration.
        :type: int
        """

        if bytes_read_timeout_seconds is not None:
            if bytes_read_timeout_seconds is not None and bytes_read_timeout_seconds < 30:
                raise ValueError("Invalid value for `bytes_read_timeout_seconds`, must be a value greater than or equal to `30`")
            if not isinstance(bytes_read_timeout_seconds, int):
                raise TypeError("Invalid type for `bytes_read_timeout_seconds`, type has to be `int`")

        self._bytes_read_timeout_seconds = bytes_read_timeout_seconds

    @property
    def stream_timeout_minutes(self):
        # type: () -> int
        """Gets the stream_timeout_minutes of this LiveAutoShutdownConfiguration.

        Automatically shutdown the live stream after a predefined runtime in minutes.

        :return: The stream_timeout_minutes of this LiveAutoShutdownConfiguration.
        :rtype: int
        """
        return self._stream_timeout_minutes

    @stream_timeout_minutes.setter
    def stream_timeout_minutes(self, stream_timeout_minutes):
        # type: (int) -> None
        """Sets the stream_timeout_minutes of this LiveAutoShutdownConfiguration.

        Automatically shutdown the live stream after a predefined runtime in minutes.

        :param stream_timeout_minutes: The stream_timeout_minutes of this LiveAutoShutdownConfiguration.
        :type: int
        """

        if stream_timeout_minutes is not None:
            if stream_timeout_minutes is not None and stream_timeout_minutes < 5:
                raise ValueError("Invalid value for `stream_timeout_minutes`, must be a value greater than or equal to `5`")
            if not isinstance(stream_timeout_minutes, int):
                raise TypeError("Invalid type for `stream_timeout_minutes`, type has to be `int`")

        self._stream_timeout_minutes = stream_timeout_minutes

    @property
    def waiting_for_first_connect_timeout_minutes(self):
        # type: () -> int
        """Gets the waiting_for_first_connect_timeout_minutes of this LiveAutoShutdownConfiguration.

        Automatically shutdown the live stream if input is never connected for a predefined number of minutes.

        :return: The waiting_for_first_connect_timeout_minutes of this LiveAutoShutdownConfiguration.
        :rtype: int
        """
        return self._waiting_for_first_connect_timeout_minutes

    @waiting_for_first_connect_timeout_minutes.setter
    def waiting_for_first_connect_timeout_minutes(self, waiting_for_first_connect_timeout_minutes):
        # type: (int) -> None
        """Sets the waiting_for_first_connect_timeout_minutes of this LiveAutoShutdownConfiguration.

        Automatically shutdown the live stream if input is never connected for a predefined number of minutes.

        :param waiting_for_first_connect_timeout_minutes: The waiting_for_first_connect_timeout_minutes of this LiveAutoShutdownConfiguration.
        :type: int
        """

        if waiting_for_first_connect_timeout_minutes is not None:
            if waiting_for_first_connect_timeout_minutes is not None and waiting_for_first_connect_timeout_minutes < 5:
                raise ValueError("Invalid value for `waiting_for_first_connect_timeout_minutes`, must be a value greater than or equal to `5`")
            if not isinstance(waiting_for_first_connect_timeout_minutes, int):
                raise TypeError("Invalid type for `waiting_for_first_connect_timeout_minutes`, type has to be `int`")

        self._waiting_for_first_connect_timeout_minutes = waiting_for_first_connect_timeout_minutes

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
        if not isinstance(other, LiveAutoShutdownConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
