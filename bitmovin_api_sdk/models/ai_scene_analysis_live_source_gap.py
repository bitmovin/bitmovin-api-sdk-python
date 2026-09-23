# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ai_scene_analysis_live_source_gap_reason import AiSceneAnalysisLiveSourceGapReason
import pprint
import six


class AiSceneAnalysisLiveSourceGap(object):
    @poscheck_model
    def __init__(self,
                 start_time_seconds=None,
                 end_time_seconds=None,
                 reason=None):
        # type: (float, float, AiSceneAnalysisLiveSourceGapReason) -> None

        self._start_time_seconds = None
        self._end_time_seconds = None
        self._reason = None
        self.discriminator = None

        if start_time_seconds is not None:
            self.start_time_seconds = start_time_seconds
        if end_time_seconds is not None:
            self.end_time_seconds = end_time_seconds
        if reason is not None:
            self.reason = reason

    @property
    def openapi_types(self):
        types = {
            'start_time_seconds': 'float',
            'end_time_seconds': 'float',
            'reason': 'AiSceneAnalysisLiveSourceGapReason'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'start_time_seconds': 'startTimeSeconds',
            'end_time_seconds': 'endTimeSeconds',
            'reason': 'reason'
        }
        return attributes

    @property
    def start_time_seconds(self):
        # type: () -> float
        """Gets the start_time_seconds of this AiSceneAnalysisLiveSourceGap.

        Gap start on the monotonic analysis timeline (required)

        :return: The start_time_seconds of this AiSceneAnalysisLiveSourceGap.
        :rtype: float
        """
        return self._start_time_seconds

    @start_time_seconds.setter
    def start_time_seconds(self, start_time_seconds):
        # type: (float) -> None
        """Sets the start_time_seconds of this AiSceneAnalysisLiveSourceGap.

        Gap start on the monotonic analysis timeline (required)

        :param start_time_seconds: The start_time_seconds of this AiSceneAnalysisLiveSourceGap.
        :type: float
        """

        if start_time_seconds is not None:
            if start_time_seconds is not None and start_time_seconds < 0:
                raise ValueError("Invalid value for `start_time_seconds`, must be a value greater than or equal to `0`")
            if not isinstance(start_time_seconds, (float, int)):
                raise TypeError("Invalid type for `start_time_seconds`, type has to be `float`")

        self._start_time_seconds = start_time_seconds

    @property
    def end_time_seconds(self):
        # type: () -> float
        """Gets the end_time_seconds of this AiSceneAnalysisLiveSourceGap.

        Gap end on the monotonic analysis timeline (required)

        :return: The end_time_seconds of this AiSceneAnalysisLiveSourceGap.
        :rtype: float
        """
        return self._end_time_seconds

    @end_time_seconds.setter
    def end_time_seconds(self, end_time_seconds):
        # type: (float) -> None
        """Sets the end_time_seconds of this AiSceneAnalysisLiveSourceGap.

        Gap end on the monotonic analysis timeline (required)

        :param end_time_seconds: The end_time_seconds of this AiSceneAnalysisLiveSourceGap.
        :type: float
        """

        if end_time_seconds is not None:
            if end_time_seconds is not None and end_time_seconds < 0:
                raise ValueError("Invalid value for `end_time_seconds`, must be a value greater than or equal to `0`")
            if not isinstance(end_time_seconds, (float, int)):
                raise TypeError("Invalid type for `end_time_seconds`, type has to be `float`")

        self._end_time_seconds = end_time_seconds

    @property
    def reason(self):
        # type: () -> AiSceneAnalysisLiveSourceGapReason
        """Gets the reason of this AiSceneAnalysisLiveSourceGap.

        Reason for the source gap (required)

        :return: The reason of this AiSceneAnalysisLiveSourceGap.
        :rtype: AiSceneAnalysisLiveSourceGapReason
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        # type: (AiSceneAnalysisLiveSourceGapReason) -> None
        """Sets the reason of this AiSceneAnalysisLiveSourceGap.

        Reason for the source gap (required)

        :param reason: The reason of this AiSceneAnalysisLiveSourceGap.
        :type: AiSceneAnalysisLiveSourceGapReason
        """

        if reason is not None:
            if not isinstance(reason, AiSceneAnalysisLiveSourceGapReason):
                raise TypeError("Invalid type for `reason`, type has to be `AiSceneAnalysisLiveSourceGapReason`")

        self._reason = reason

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
        if not isinstance(other, AiSceneAnalysisLiveSourceGap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
