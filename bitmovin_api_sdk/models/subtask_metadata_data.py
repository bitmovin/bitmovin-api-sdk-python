# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class SubtaskMetadataData(object):
    @poscheck_model
    def __init__(self,
                 avg_frames_encoded_per_second=None,
                 bytes_encoded=None,
                 frames_analysed=None,
                 frames_encoded=None,
                 realtime_factor=None,
                 size=None):
        # type: (float, int, int, int, float, int) -> None

        self._avg_frames_encoded_per_second = None
        self._bytes_encoded = None
        self._frames_analysed = None
        self._frames_encoded = None
        self._realtime_factor = None
        self._size = None
        self.discriminator = None

        if avg_frames_encoded_per_second is not None:
            self.avg_frames_encoded_per_second = avg_frames_encoded_per_second
        if bytes_encoded is not None:
            self.bytes_encoded = bytes_encoded
        if frames_analysed is not None:
            self.frames_analysed = frames_analysed
        if frames_encoded is not None:
            self.frames_encoded = frames_encoded
        if realtime_factor is not None:
            self.realtime_factor = realtime_factor
        if size is not None:
            self.size = size

    @property
    def openapi_types(self):
        types = {
            'avg_frames_encoded_per_second': 'float',
            'bytes_encoded': 'int',
            'frames_analysed': 'int',
            'frames_encoded': 'int',
            'realtime_factor': 'float',
            'size': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'avg_frames_encoded_per_second': 'avgFramesEncodedPerSecond',
            'bytes_encoded': 'bytesEncoded',
            'frames_analysed': 'framesAnalysed',
            'frames_encoded': 'framesEncoded',
            'realtime_factor': 'realtimeFactor',
            'size': 'size'
        }
        return attributes

    @property
    def avg_frames_encoded_per_second(self):
        # type: () -> float
        """Gets the avg_frames_encoded_per_second of this SubtaskMetadataData.


        :return: The avg_frames_encoded_per_second of this SubtaskMetadataData.
        :rtype: float
        """
        return self._avg_frames_encoded_per_second

    @avg_frames_encoded_per_second.setter
    def avg_frames_encoded_per_second(self, avg_frames_encoded_per_second):
        # type: (float) -> None
        """Sets the avg_frames_encoded_per_second of this SubtaskMetadataData.


        :param avg_frames_encoded_per_second: The avg_frames_encoded_per_second of this SubtaskMetadataData.
        :type: float
        """

        if avg_frames_encoded_per_second is not None:
            if not isinstance(avg_frames_encoded_per_second, (float, int)):
                raise TypeError("Invalid type for `avg_frames_encoded_per_second`, type has to be `float`")

        self._avg_frames_encoded_per_second = avg_frames_encoded_per_second

    @property
    def bytes_encoded(self):
        # type: () -> int
        """Gets the bytes_encoded of this SubtaskMetadataData.


        :return: The bytes_encoded of this SubtaskMetadataData.
        :rtype: int
        """
        return self._bytes_encoded

    @bytes_encoded.setter
    def bytes_encoded(self, bytes_encoded):
        # type: (int) -> None
        """Sets the bytes_encoded of this SubtaskMetadataData.


        :param bytes_encoded: The bytes_encoded of this SubtaskMetadataData.
        :type: int
        """

        if bytes_encoded is not None:
            if not isinstance(bytes_encoded, int):
                raise TypeError("Invalid type for `bytes_encoded`, type has to be `int`")

        self._bytes_encoded = bytes_encoded

    @property
    def frames_analysed(self):
        # type: () -> int
        """Gets the frames_analysed of this SubtaskMetadataData.


        :return: The frames_analysed of this SubtaskMetadataData.
        :rtype: int
        """
        return self._frames_analysed

    @frames_analysed.setter
    def frames_analysed(self, frames_analysed):
        # type: (int) -> None
        """Sets the frames_analysed of this SubtaskMetadataData.


        :param frames_analysed: The frames_analysed of this SubtaskMetadataData.
        :type: int
        """

        if frames_analysed is not None:
            if not isinstance(frames_analysed, int):
                raise TypeError("Invalid type for `frames_analysed`, type has to be `int`")

        self._frames_analysed = frames_analysed

    @property
    def frames_encoded(self):
        # type: () -> int
        """Gets the frames_encoded of this SubtaskMetadataData.


        :return: The frames_encoded of this SubtaskMetadataData.
        :rtype: int
        """
        return self._frames_encoded

    @frames_encoded.setter
    def frames_encoded(self, frames_encoded):
        # type: (int) -> None
        """Sets the frames_encoded of this SubtaskMetadataData.


        :param frames_encoded: The frames_encoded of this SubtaskMetadataData.
        :type: int
        """

        if frames_encoded is not None:
            if not isinstance(frames_encoded, int):
                raise TypeError("Invalid type for `frames_encoded`, type has to be `int`")

        self._frames_encoded = frames_encoded

    @property
    def realtime_factor(self):
        # type: () -> float
        """Gets the realtime_factor of this SubtaskMetadataData.


        :return: The realtime_factor of this SubtaskMetadataData.
        :rtype: float
        """
        return self._realtime_factor

    @realtime_factor.setter
    def realtime_factor(self, realtime_factor):
        # type: (float) -> None
        """Sets the realtime_factor of this SubtaskMetadataData.


        :param realtime_factor: The realtime_factor of this SubtaskMetadataData.
        :type: float
        """

        if realtime_factor is not None:
            if not isinstance(realtime_factor, (float, int)):
                raise TypeError("Invalid type for `realtime_factor`, type has to be `float`")

        self._realtime_factor = realtime_factor

    @property
    def size(self):
        # type: () -> int
        """Gets the size of this SubtaskMetadataData.


        :return: The size of this SubtaskMetadataData.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        # type: (int) -> None
        """Sets the size of this SubtaskMetadataData.


        :param size: The size of this SubtaskMetadataData.
        :type: int
        """

        if size is not None:
            if not isinstance(size, int):
                raise TypeError("Invalid type for `size`, type has to be `int`")

        self._size = size

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
        if not isinstance(other, SubtaskMetadataData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
