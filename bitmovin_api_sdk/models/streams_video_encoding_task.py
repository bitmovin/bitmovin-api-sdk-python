# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.streams_video_encoding_status import StreamsVideoEncodingStatus
from bitmovin_api_sdk.models.streams_video_quality import StreamsVideoQuality
import pprint
import six


class StreamsVideoEncodingTask(object):
    @poscheck_model
    def __init__(self,
                 quality=None,
                 status=None):
        # type: (StreamsVideoQuality, StreamsVideoEncodingStatus) -> None

        self._quality = None
        self._status = None
        self.discriminator = None

        if quality is not None:
            self.quality = quality
        if status is not None:
            self.status = status

    @property
    def openapi_types(self):
        types = {
            'quality': 'StreamsVideoQuality',
            'status': 'StreamsVideoEncodingStatus'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'quality': 'quality',
            'status': 'status'
        }
        return attributes

    @property
    def quality(self):
        # type: () -> StreamsVideoQuality
        """Gets the quality of this StreamsVideoEncodingTask.

        Quality of the encoding

        :return: The quality of this StreamsVideoEncodingTask.
        :rtype: StreamsVideoQuality
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        # type: (StreamsVideoQuality) -> None
        """Sets the quality of this StreamsVideoEncodingTask.

        Quality of the encoding

        :param quality: The quality of this StreamsVideoEncodingTask.
        :type: StreamsVideoQuality
        """

        if quality is not None:
            if not isinstance(quality, StreamsVideoQuality):
                raise TypeError("Invalid type for `quality`, type has to be `StreamsVideoQuality`")

        self._quality = quality

    @property
    def status(self):
        # type: () -> StreamsVideoEncodingStatus
        """Gets the status of this StreamsVideoEncodingTask.

        Current state of the encoding

        :return: The status of this StreamsVideoEncodingTask.
        :rtype: StreamsVideoEncodingStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (StreamsVideoEncodingStatus) -> None
        """Sets the status of this StreamsVideoEncodingTask.

        Current state of the encoding

        :param status: The status of this StreamsVideoEncodingTask.
        :type: StreamsVideoEncodingStatus
        """

        if status is not None:
            if not isinstance(status, StreamsVideoEncodingStatus):
                raise TypeError("Invalid type for `status`, type has to be `StreamsVideoEncodingStatus`")

        self._status = status

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
        if not isinstance(other, StreamsVideoEncodingTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
