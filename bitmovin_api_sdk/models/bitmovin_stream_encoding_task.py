# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_stream_encoding_status import BitmovinStreamEncodingStatus
from bitmovin_api_sdk.models.bitmovin_stream_quality import BitmovinStreamQuality
import pprint
import six


class BitmovinStreamEncodingTask(object):
    @poscheck_model
    def __init__(self,
                 quality=None,
                 status=None):
        # type: (BitmovinStreamQuality, BitmovinStreamEncodingStatus) -> None

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
            'quality': 'BitmovinStreamQuality',
            'status': 'BitmovinStreamEncodingStatus'
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
        # type: () -> BitmovinStreamQuality
        """Gets the quality of this BitmovinStreamEncodingTask.

        Quality of the encoding

        :return: The quality of this BitmovinStreamEncodingTask.
        :rtype: BitmovinStreamQuality
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        # type: (BitmovinStreamQuality) -> None
        """Sets the quality of this BitmovinStreamEncodingTask.

        Quality of the encoding

        :param quality: The quality of this BitmovinStreamEncodingTask.
        :type: BitmovinStreamQuality
        """

        if quality is not None:
            if not isinstance(quality, BitmovinStreamQuality):
                raise TypeError("Invalid type for `quality`, type has to be `BitmovinStreamQuality`")

        self._quality = quality

    @property
    def status(self):
        # type: () -> BitmovinStreamEncodingStatus
        """Gets the status of this BitmovinStreamEncodingTask.

        Current state of the encoding

        :return: The status of this BitmovinStreamEncodingTask.
        :rtype: BitmovinStreamEncodingStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (BitmovinStreamEncodingStatus) -> None
        """Sets the status of this BitmovinStreamEncodingTask.

        Current state of the encoding

        :param status: The status of this BitmovinStreamEncodingTask.
        :type: BitmovinStreamEncodingStatus
        """

        if status is not None:
            if not isinstance(status, BitmovinStreamEncodingStatus):
                raise TypeError("Invalid type for `status`, type has to be `BitmovinStreamEncodingStatus`")

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
        if not isinstance(other, BitmovinStreamEncodingTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
