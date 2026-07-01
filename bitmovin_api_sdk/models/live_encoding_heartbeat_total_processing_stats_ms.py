# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class LiveEncodingHeartbeatTotalProcessingStatsMs(object):
    @poscheck_model
    def __init__(self,
                 min_=None,
                 max_=None,
                 mean=None,
                 median=None):
        # type: (int, int, int, int) -> None

        self._min = None
        self._max = None
        self._mean = None
        self._median = None
        self.discriminator = None

        if min_ is not None:
            self.min = min_
        if max_ is not None:
            self.max = max_
        if mean is not None:
            self.mean = mean
        if median is not None:
            self.median = median

    @property
    def openapi_types(self):
        types = {
            'min': 'int',
            'max': 'int',
            'mean': 'int',
            'median': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'min': 'min',
            'max': 'max',
            'mean': 'mean',
            'median': 'median'
        }
        return attributes

    @property
    def min(self):
        # type: () -> int
        """Gets the min of this LiveEncodingHeartbeatTotalProcessingStatsMs.

        Minimum total processing duration in milliseconds.

        :return: The min of this LiveEncodingHeartbeatTotalProcessingStatsMs.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min_):
        # type: (int) -> None
        """Sets the min of this LiveEncodingHeartbeatTotalProcessingStatsMs.

        Minimum total processing duration in milliseconds.

        :param min_: The min of this LiveEncodingHeartbeatTotalProcessingStatsMs.
        :type: int
        """

        if min_ is not None:
            if not isinstance(min_, int):
                raise TypeError("Invalid type for `min`, type has to be `int`")

        self._min = min_

    @property
    def max(self):
        # type: () -> int
        """Gets the max of this LiveEncodingHeartbeatTotalProcessingStatsMs.

        Maximum total processing duration in milliseconds.

        :return: The max of this LiveEncodingHeartbeatTotalProcessingStatsMs.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max_):
        # type: (int) -> None
        """Sets the max of this LiveEncodingHeartbeatTotalProcessingStatsMs.

        Maximum total processing duration in milliseconds.

        :param max_: The max of this LiveEncodingHeartbeatTotalProcessingStatsMs.
        :type: int
        """

        if max_ is not None:
            if not isinstance(max_, int):
                raise TypeError("Invalid type for `max`, type has to be `int`")

        self._max = max_

    @property
    def mean(self):
        # type: () -> int
        """Gets the mean of this LiveEncodingHeartbeatTotalProcessingStatsMs.

        Mean total processing duration in milliseconds.

        :return: The mean of this LiveEncodingHeartbeatTotalProcessingStatsMs.
        :rtype: int
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        # type: (int) -> None
        """Sets the mean of this LiveEncodingHeartbeatTotalProcessingStatsMs.

        Mean total processing duration in milliseconds.

        :param mean: The mean of this LiveEncodingHeartbeatTotalProcessingStatsMs.
        :type: int
        """

        if mean is not None:
            if not isinstance(mean, int):
                raise TypeError("Invalid type for `mean`, type has to be `int`")

        self._mean = mean

    @property
    def median(self):
        # type: () -> int
        """Gets the median of this LiveEncodingHeartbeatTotalProcessingStatsMs.

        Median total processing duration in milliseconds.

        :return: The median of this LiveEncodingHeartbeatTotalProcessingStatsMs.
        :rtype: int
        """
        return self._median

    @median.setter
    def median(self, median):
        # type: (int) -> None
        """Sets the median of this LiveEncodingHeartbeatTotalProcessingStatsMs.

        Median total processing duration in milliseconds.

        :param median: The median of this LiveEncodingHeartbeatTotalProcessingStatsMs.
        :type: int
        """

        if median is not None:
            if not isinstance(median, int):
                raise TypeError("Invalid type for `median`, type has to be `int`")

        self._median = median

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
        if not isinstance(other, LiveEncodingHeartbeatTotalProcessingStatsMs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
