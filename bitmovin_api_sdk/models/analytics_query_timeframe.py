# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsQueryTimeframe(object):
    @poscheck_model
    def __init__(self,
                 start=None,
                 end=None):
        # type: (datetime, datetime) -> None

        self._start = None
        self._end = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    @property
    def openapi_types(self):
        types = {
            'start': 'datetime',
            'end': 'datetime'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'start': 'start',
            'end': 'end'
        }
        return attributes

    @property
    def start(self):
        # type: () -> datetime
        """Gets the start of this AnalyticsQueryTimeframe.

        Start of timeframe which is queried in UTC format.

        :return: The start of this AnalyticsQueryTimeframe.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        # type: (datetime) -> None
        """Sets the start of this AnalyticsQueryTimeframe.

        Start of timeframe which is queried in UTC format.

        :param start: The start of this AnalyticsQueryTimeframe.
        :type: datetime
        """

        if start is not None:
            if not isinstance(start, datetime):
                raise TypeError("Invalid type for `start`, type has to be `datetime`")

        self._start = start

    @property
    def end(self):
        # type: () -> datetime
        """Gets the end of this AnalyticsQueryTimeframe.

        End of timeframe which is queried in UTC format.

        :return: The end of this AnalyticsQueryTimeframe.
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        # type: (datetime) -> None
        """Sets the end of this AnalyticsQueryTimeframe.

        End of timeframe which is queried in UTC format.

        :param end: The end of this AnalyticsQueryTimeframe.
        :type: datetime
        """

        if end is not None:
            if not isinstance(end, datetime):
                raise TypeError("Invalid type for `end`, type has to be `datetime`")

        self._end = end

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
        if not isinstance(other, AnalyticsQueryTimeframe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
