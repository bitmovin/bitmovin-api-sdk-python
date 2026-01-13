# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class EsamMediaPoint(object):
    @poscheck_model
    def __init__(self,
                 match_time=None,
                 signals=None,
                 conditions=None):
        # type: (datetime, list[EsamSignal], list[EsamCondition]) -> None

        self._match_time = None
        self._signals = list()
        self._conditions = list()
        self.discriminator = None

        if match_time is not None:
            self.match_time = match_time
        if signals is not None:
            self.signals = signals
        if conditions is not None:
            self.conditions = conditions

    @property
    def openapi_types(self):
        types = {
            'match_time': 'datetime',
            'signals': 'list[EsamSignal]',
            'conditions': 'list[EsamCondition]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'match_time': 'matchTime',
            'signals': 'signals',
            'conditions': 'conditions'
        }
        return attributes

    @property
    def match_time(self):
        # type: () -> datetime
        """Gets the match_time of this EsamMediaPoint.

        ISO 8601 date-time specifying when the signal should be matched and inserted into the live stream

        :return: The match_time of this EsamMediaPoint.
        :rtype: datetime
        """
        return self._match_time

    @match_time.setter
    def match_time(self, match_time):
        # type: (datetime) -> None
        """Sets the match_time of this EsamMediaPoint.

        ISO 8601 date-time specifying when the signal should be matched and inserted into the live stream

        :param match_time: The match_time of this EsamMediaPoint.
        :type: datetime
        """

        if match_time is not None:
            if not isinstance(match_time, datetime):
                raise TypeError("Invalid type for `match_time`, type has to be `datetime`")

        self._match_time = match_time

    @property
    def signals(self):
        # type: () -> list[EsamSignal]
        """Gets the signals of this EsamMediaPoint.

        Array of ESAM signals containing SCTE-35 binary data. At least one signal is required (required)

        :return: The signals of this EsamMediaPoint.
        :rtype: list[EsamSignal]
        """
        return self._signals

    @signals.setter
    def signals(self, signals):
        # type: (list) -> None
        """Sets the signals of this EsamMediaPoint.

        Array of ESAM signals containing SCTE-35 binary data. At least one signal is required (required)

        :param signals: The signals of this EsamMediaPoint.
        :type: list[EsamSignal]
        """

        if signals is not None:
            if not isinstance(signals, list):
                raise TypeError("Invalid type for `signals`, type has to be `list[EsamSignal]`")

        self._signals = signals

    @property
    def conditions(self):
        # type: () -> list[EsamCondition]
        """Gets the conditions of this EsamMediaPoint.

        Optional array of ESAM conditions with timing offsets and directional markers (OUT/IN) for signaling content boundaries

        :return: The conditions of this EsamMediaPoint.
        :rtype: list[EsamCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        # type: (list) -> None
        """Sets the conditions of this EsamMediaPoint.

        Optional array of ESAM conditions with timing offsets and directional markers (OUT/IN) for signaling content boundaries

        :param conditions: The conditions of this EsamMediaPoint.
        :type: list[EsamCondition]
        """

        if conditions is not None:
            if not isinstance(conditions, list):
                raise TypeError("Invalid type for `conditions`, type has to be `list[EsamCondition]`")

        self._conditions = conditions

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
        if not isinstance(other, EsamMediaPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
