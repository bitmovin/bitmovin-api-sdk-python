# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveEncodingHeartbeatUploadOutlier(object):
    @poscheck_model
    def __init__(self,
                 segment_number=None,
                 encoding_reference_muxing_id=None,
                 duration_ms=None):
        # type: (int, string_types, int) -> None

        self._segment_number = None
        self._encoding_reference_muxing_id = None
        self._duration_ms = None
        self.discriminator = None

        if segment_number is not None:
            self.segment_number = segment_number
        if encoding_reference_muxing_id is not None:
            self.encoding_reference_muxing_id = encoding_reference_muxing_id
        if duration_ms is not None:
            self.duration_ms = duration_ms

    @property
    def openapi_types(self):
        types = {
            'segment_number': 'int',
            'encoding_reference_muxing_id': 'string_types',
            'duration_ms': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'segment_number': 'segmentNumber',
            'encoding_reference_muxing_id': 'encodingReferenceMuxingId',
            'duration_ms': 'durationMs'
        }
        return attributes

    @property
    def segment_number(self):
        # type: () -> int
        """Gets the segment_number of this LiveEncodingHeartbeatUploadOutlier.

        Output segment number this upload belongs to.

        :return: The segment_number of this LiveEncodingHeartbeatUploadOutlier.
        :rtype: int
        """
        return self._segment_number

    @segment_number.setter
    def segment_number(self, segment_number):
        # type: (int) -> None
        """Sets the segment_number of this LiveEncodingHeartbeatUploadOutlier.

        Output segment number this upload belongs to.

        :param segment_number: The segment_number of this LiveEncodingHeartbeatUploadOutlier.
        :type: int
        """

        if segment_number is not None:
            if not isinstance(segment_number, int):
                raise TypeError("Invalid type for `segment_number`, type has to be `int`")

        self._segment_number = segment_number

    @property
    def encoding_reference_muxing_id(self):
        # type: () -> string_types
        """Gets the encoding_reference_muxing_id of this LiveEncodingHeartbeatUploadOutlier.

        Identifier of the muxing whose upload was flagged.

        :return: The encoding_reference_muxing_id of this LiveEncodingHeartbeatUploadOutlier.
        :rtype: string_types
        """
        return self._encoding_reference_muxing_id

    @encoding_reference_muxing_id.setter
    def encoding_reference_muxing_id(self, encoding_reference_muxing_id):
        # type: (string_types) -> None
        """Sets the encoding_reference_muxing_id of this LiveEncodingHeartbeatUploadOutlier.

        Identifier of the muxing whose upload was flagged.

        :param encoding_reference_muxing_id: The encoding_reference_muxing_id of this LiveEncodingHeartbeatUploadOutlier.
        :type: string_types
        """

        if encoding_reference_muxing_id is not None:
            if not isinstance(encoding_reference_muxing_id, string_types):
                raise TypeError("Invalid type for `encoding_reference_muxing_id`, type has to be `string_types`")

        self._encoding_reference_muxing_id = encoding_reference_muxing_id

    @property
    def duration_ms(self):
        # type: () -> int
        """Gets the duration_ms of this LiveEncodingHeartbeatUploadOutlier.

        Upload duration in milliseconds.

        :return: The duration_ms of this LiveEncodingHeartbeatUploadOutlier.
        :rtype: int
        """
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, duration_ms):
        # type: (int) -> None
        """Sets the duration_ms of this LiveEncodingHeartbeatUploadOutlier.

        Upload duration in milliseconds.

        :param duration_ms: The duration_ms of this LiveEncodingHeartbeatUploadOutlier.
        :type: int
        """

        if duration_ms is not None:
            if not isinstance(duration_ms, int):
                raise TypeError("Invalid type for `duration_ms`, type has to be `int`")

        self._duration_ms = duration_ms

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
        if not isinstance(other, LiveEncodingHeartbeatUploadOutlier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
