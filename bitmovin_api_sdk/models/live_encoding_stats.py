# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_encoding_status import LiveEncodingStatus
import pprint
import six


class LiveEncodingStats(object):
    @poscheck_model
    def __init__(self,
                 status=None,
                 events=None,
                 statistics=None):
        # type: (LiveEncodingStatus, list[LiveEncodingStatsEvent], list[StreamInfos]) -> None

        self._status = None
        self._events = list()
        self._statistics = list()
        self.discriminator = None

        if status is not None:
            self.status = status
        if events is not None:
            self.events = events
        if statistics is not None:
            self.statistics = statistics

    @property
    def openapi_types(self):
        types = {
            'status': 'LiveEncodingStatus',
            'events': 'list[LiveEncodingStatsEvent]',
            'statistics': 'list[StreamInfos]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'status': 'status',
            'events': 'events',
            'statistics': 'statistics'
        }
        return attributes

    @property
    def status(self):
        # type: () -> LiveEncodingStatus
        """Gets the status of this LiveEncodingStats.


        :return: The status of this LiveEncodingStats.
        :rtype: LiveEncodingStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        # type: (LiveEncodingStatus) -> None
        """Sets the status of this LiveEncodingStats.


        :param status: The status of this LiveEncodingStats.
        :type: LiveEncodingStatus
        """

        if status is not None:
            if not isinstance(status, LiveEncodingStatus):
                raise TypeError("Invalid type for `status`, type has to be `LiveEncodingStatus`")

        self._status = status

    @property
    def events(self):
        # type: () -> list[LiveEncodingStatsEvent]
        """Gets the events of this LiveEncodingStats.

        List of events

        :return: The events of this LiveEncodingStats.
        :rtype: list[LiveEncodingStatsEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        # type: (list) -> None
        """Sets the events of this LiveEncodingStats.

        List of events

        :param events: The events of this LiveEncodingStats.
        :type: list[LiveEncodingStatsEvent]
        """

        if events is not None:
            if not isinstance(events, list):
                raise TypeError("Invalid type for `events`, type has to be `list[LiveEncodingStatsEvent]`")

        self._events = events

    @property
    def statistics(self):
        # type: () -> list[StreamInfos]
        """Gets the statistics of this LiveEncodingStats.

        List of statistics

        :return: The statistics of this LiveEncodingStats.
        :rtype: list[StreamInfos]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        # type: (list) -> None
        """Sets the statistics of this LiveEncodingStats.

        List of statistics

        :param statistics: The statistics of this LiveEncodingStats.
        :type: list[StreamInfos]
        """

        if statistics is not None:
            if not isinstance(statistics, list):
                raise TypeError("Invalid type for `statistics`, type has to be `list[StreamInfos]`")

        self._statistics = statistics

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
        if not isinstance(other, LiveEncodingStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
