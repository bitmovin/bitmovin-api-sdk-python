# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_encoding_heartbeat_total_processing_stats_ms import LiveEncodingHeartbeatTotalProcessingStatsMs
import pprint
import six


class LiveEncodingHeartbeatSegments(object):
    @poscheck_model
    def __init__(self,
                 total_processing_stats_ms=None,
                 upload_outliers=None,
                 total_processing_outliers=None):
        # type: (LiveEncodingHeartbeatTotalProcessingStatsMs, list[LiveEncodingHeartbeatUploadOutlier], list[LiveEncodingHeartbeatTotalProcessingOutlier]) -> None

        self._total_processing_stats_ms = None
        self._upload_outliers = list()
        self._total_processing_outliers = list()
        self.discriminator = None

        if total_processing_stats_ms is not None:
            self.total_processing_stats_ms = total_processing_stats_ms
        if upload_outliers is not None:
            self.upload_outliers = upload_outliers
        if total_processing_outliers is not None:
            self.total_processing_outliers = total_processing_outliers

    @property
    def openapi_types(self):
        types = {
            'total_processing_stats_ms': 'LiveEncodingHeartbeatTotalProcessingStatsMs',
            'upload_outliers': 'list[LiveEncodingHeartbeatUploadOutlier]',
            'total_processing_outliers': 'list[LiveEncodingHeartbeatTotalProcessingOutlier]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'total_processing_stats_ms': 'totalProcessingStatsMs',
            'upload_outliers': 'uploadOutliers',
            'total_processing_outliers': 'totalProcessingOutliers'
        }
        return attributes

    @property
    def total_processing_stats_ms(self):
        # type: () -> LiveEncodingHeartbeatTotalProcessingStatsMs
        """Gets the total_processing_stats_ms of this LiveEncodingHeartbeatSegments.

        Aggregate statistics of per-segment total processing duration.

        :return: The total_processing_stats_ms of this LiveEncodingHeartbeatSegments.
        :rtype: LiveEncodingHeartbeatTotalProcessingStatsMs
        """
        return self._total_processing_stats_ms

    @total_processing_stats_ms.setter
    def total_processing_stats_ms(self, total_processing_stats_ms):
        # type: (LiveEncodingHeartbeatTotalProcessingStatsMs) -> None
        """Sets the total_processing_stats_ms of this LiveEncodingHeartbeatSegments.

        Aggregate statistics of per-segment total processing duration.

        :param total_processing_stats_ms: The total_processing_stats_ms of this LiveEncodingHeartbeatSegments.
        :type: LiveEncodingHeartbeatTotalProcessingStatsMs
        """

        if total_processing_stats_ms is not None:
            if not isinstance(total_processing_stats_ms, LiveEncodingHeartbeatTotalProcessingStatsMs):
                raise TypeError("Invalid type for `total_processing_stats_ms`, type has to be `LiveEncodingHeartbeatTotalProcessingStatsMs`")

        self._total_processing_stats_ms = total_processing_stats_ms

    @property
    def upload_outliers(self):
        # type: () -> list[LiveEncodingHeartbeatUploadOutlier]
        """Gets the upload_outliers of this LiveEncodingHeartbeatSegments.

        Last 20 per-muxing uploads whose duration exceeded the upload-outlier threshold.

        :return: The upload_outliers of this LiveEncodingHeartbeatSegments.
        :rtype: list[LiveEncodingHeartbeatUploadOutlier]
        """
        return self._upload_outliers

    @upload_outliers.setter
    def upload_outliers(self, upload_outliers):
        # type: (list) -> None
        """Sets the upload_outliers of this LiveEncodingHeartbeatSegments.

        Last 20 per-muxing uploads whose duration exceeded the upload-outlier threshold.

        :param upload_outliers: The upload_outliers of this LiveEncodingHeartbeatSegments.
        :type: list[LiveEncodingHeartbeatUploadOutlier]
        """

        if upload_outliers is not None:
            if not isinstance(upload_outliers, list):
                raise TypeError("Invalid type for `upload_outliers`, type has to be `list[LiveEncodingHeartbeatUploadOutlier]`")

        self._upload_outliers = upload_outliers

    @property
    def total_processing_outliers(self):
        # type: () -> list[LiveEncodingHeartbeatTotalProcessingOutlier]
        """Gets the total_processing_outliers of this LiveEncodingHeartbeatSegments.

        Last 20 segments whose total processing duration exceeded twice the rolling median.

        :return: The total_processing_outliers of this LiveEncodingHeartbeatSegments.
        :rtype: list[LiveEncodingHeartbeatTotalProcessingOutlier]
        """
        return self._total_processing_outliers

    @total_processing_outliers.setter
    def total_processing_outliers(self, total_processing_outliers):
        # type: (list) -> None
        """Sets the total_processing_outliers of this LiveEncodingHeartbeatSegments.

        Last 20 segments whose total processing duration exceeded twice the rolling median.

        :param total_processing_outliers: The total_processing_outliers of this LiveEncodingHeartbeatSegments.
        :type: list[LiveEncodingHeartbeatTotalProcessingOutlier]
        """

        if total_processing_outliers is not None:
            if not isinstance(total_processing_outliers, list):
                raise TypeError("Invalid type for `total_processing_outliers`, type has to be `list[LiveEncodingHeartbeatTotalProcessingOutlier]`")

        self._total_processing_outliers = total_processing_outliers

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
        if not isinstance(other, LiveEncodingHeartbeatSegments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
