# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsThresholdRuleOptions(object):
    @poscheck_model
    def __init__(self,
                 threshold=None,
                 persistence=None,
                 sample_size=None,
                 recovery=None,
                 repeat_interval=None,
                 notify_on_resolved=None):
        # type: (float, int, int, int, int, bool) -> None

        self._threshold = None
        self._persistence = None
        self._sample_size = None
        self._recovery = None
        self._repeat_interval = None
        self._notify_on_resolved = None
        self.discriminator = None

        if threshold is not None:
            self.threshold = threshold
        if persistence is not None:
            self.persistence = persistence
        if sample_size is not None:
            self.sample_size = sample_size
        if recovery is not None:
            self.recovery = recovery
        if repeat_interval is not None:
            self.repeat_interval = repeat_interval
        if notify_on_resolved is not None:
            self.notify_on_resolved = notify_on_resolved

    @property
    def openapi_types(self):
        types = {
            'threshold': 'float',
            'persistence': 'int',
            'sample_size': 'int',
            'recovery': 'int',
            'repeat_interval': 'int',
            'notify_on_resolved': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'threshold': 'threshold',
            'persistence': 'persistence',
            'sample_size': 'sampleSize',
            'recovery': 'recovery',
            'repeat_interval': 'repeatInterval',
            'notify_on_resolved': 'notifyOnResolved'
        }
        return attributes

    @property
    def threshold(self):
        # type: () -> float
        """Gets the threshold of this AnalyticsThresholdRuleOptions.

        Threshold for triggering alert (required)

        :return: The threshold of this AnalyticsThresholdRuleOptions.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        # type: (float) -> None
        """Sets the threshold of this AnalyticsThresholdRuleOptions.

        Threshold for triggering alert (required)

        :param threshold: The threshold of this AnalyticsThresholdRuleOptions.
        :type: float
        """

        if threshold is not None:
            if not isinstance(threshold, (float, int)):
                raise TypeError("Invalid type for `threshold`, type has to be `float`")

        self._threshold = threshold

    @property
    def persistence(self):
        # type: () -> int
        """Gets the persistence of this AnalyticsThresholdRuleOptions.

        Persistence of threshold violation in minutes (required)

        :return: The persistence of this AnalyticsThresholdRuleOptions.
        :rtype: int
        """
        return self._persistence

    @persistence.setter
    def persistence(self, persistence):
        # type: (int) -> None
        """Sets the persistence of this AnalyticsThresholdRuleOptions.

        Persistence of threshold violation in minutes (required)

        :param persistence: The persistence of this AnalyticsThresholdRuleOptions.
        :type: int
        """

        if persistence is not None:
            if not isinstance(persistence, int):
                raise TypeError("Invalid type for `persistence`, type has to be `int`")

        self._persistence = persistence

    @property
    def sample_size(self):
        # type: () -> int
        """Gets the sample_size of this AnalyticsThresholdRuleOptions.

        Sample size for rule processing (required)

        :return: The sample_size of this AnalyticsThresholdRuleOptions.
        :rtype: int
        """
        return self._sample_size

    @sample_size.setter
    def sample_size(self, sample_size):
        # type: (int) -> None
        """Sets the sample_size of this AnalyticsThresholdRuleOptions.

        Sample size for rule processing (required)

        :param sample_size: The sample_size of this AnalyticsThresholdRuleOptions.
        :type: int
        """

        if sample_size is not None:
            if not isinstance(sample_size, int):
                raise TypeError("Invalid type for `sample_size`, type has to be `int`")

        self._sample_size = sample_size

    @property
    def recovery(self):
        # type: () -> int
        """Gets the recovery of this AnalyticsThresholdRuleOptions.

        Number of minutes without violation after which incident is considered as recovered (required)

        :return: The recovery of this AnalyticsThresholdRuleOptions.
        :rtype: int
        """
        return self._recovery

    @recovery.setter
    def recovery(self, recovery):
        # type: (int) -> None
        """Sets the recovery of this AnalyticsThresholdRuleOptions.

        Number of minutes without violation after which incident is considered as recovered (required)

        :param recovery: The recovery of this AnalyticsThresholdRuleOptions.
        :type: int
        """

        if recovery is not None:
            if not isinstance(recovery, int):
                raise TypeError("Invalid type for `recovery`, type has to be `int`")

        self._recovery = recovery

    @property
    def repeat_interval(self):
        # type: () -> int
        """Gets the repeat_interval of this AnalyticsThresholdRuleOptions.

        Interval for repeating notifications (required)

        :return: The repeat_interval of this AnalyticsThresholdRuleOptions.
        :rtype: int
        """
        return self._repeat_interval

    @repeat_interval.setter
    def repeat_interval(self, repeat_interval):
        # type: (int) -> None
        """Sets the repeat_interval of this AnalyticsThresholdRuleOptions.

        Interval for repeating notifications (required)

        :param repeat_interval: The repeat_interval of this AnalyticsThresholdRuleOptions.
        :type: int
        """

        if repeat_interval is not None:
            if not isinstance(repeat_interval, int):
                raise TypeError("Invalid type for `repeat_interval`, type has to be `int`")

        self._repeat_interval = repeat_interval

    @property
    def notify_on_resolved(self):
        # type: () -> bool
        """Gets the notify_on_resolved of this AnalyticsThresholdRuleOptions.

        Send notification after incident is resolved

        :return: The notify_on_resolved of this AnalyticsThresholdRuleOptions.
        :rtype: bool
        """
        return self._notify_on_resolved

    @notify_on_resolved.setter
    def notify_on_resolved(self, notify_on_resolved):
        # type: (bool) -> None
        """Sets the notify_on_resolved of this AnalyticsThresholdRuleOptions.

        Send notification after incident is resolved

        :param notify_on_resolved: The notify_on_resolved of this AnalyticsThresholdRuleOptions.
        :type: bool
        """

        if notify_on_resolved is not None:
            if not isinstance(notify_on_resolved, bool):
                raise TypeError("Invalid type for `notify_on_resolved`, type has to be `bool`")

        self._notify_on_resolved = notify_on_resolved

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
        if not isinstance(other, AnalyticsThresholdRuleOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
