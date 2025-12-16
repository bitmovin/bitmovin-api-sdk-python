# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.clock_synchronization_mode import ClockSynchronizationMode
from bitmovin_api_sdk.models.live_encoding_event_name import LiveEncodingEventName
import pprint
import six


class LiveEncodingStatsEventDetails(object):
    @poscheck_model
    def __init__(self,
                 event_type=None,
                 message=None,
                 source=None,
                 year=None,
                 month=None,
                 day=None,
                 hours=None,
                 minutes=None,
                 seconds=None,
                 micro_seconds=None):
        # type: (LiveEncodingEventName, string_types, ClockSynchronizationMode, int, int, int, int, int, int, int) -> None

        self._event_type = None
        self._message = None
        self._source = None
        self._year = None
        self._month = None
        self._day = None
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._micro_seconds = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if message is not None:
            self.message = message
        if source is not None:
            self.source = source
        if year is not None:
            self.year = year
        if month is not None:
            self.month = month
        if day is not None:
            self.day = day
        if hours is not None:
            self.hours = hours
        if minutes is not None:
            self.minutes = minutes
        if seconds is not None:
            self.seconds = seconds
        if micro_seconds is not None:
            self.micro_seconds = micro_seconds

    @property
    def openapi_types(self):
        types = {
            'event_type': 'LiveEncodingEventName',
            'message': 'string_types',
            'source': 'ClockSynchronizationMode',
            'year': 'int',
            'month': 'int',
            'day': 'int',
            'hours': 'int',
            'minutes': 'int',
            'seconds': 'int',
            'micro_seconds': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'event_type': 'eventType',
            'message': 'message',
            'source': 'source',
            'year': 'year',
            'month': 'month',
            'day': 'day',
            'hours': 'hours',
            'minutes': 'minutes',
            'seconds': 'seconds',
            'micro_seconds': 'microSeconds'
        }
        return attributes

    @property
    def event_type(self):
        # type: () -> LiveEncodingEventName
        """Gets the event_type of this LiveEncodingStatsEventDetails.


        :return: The event_type of this LiveEncodingStatsEventDetails.
        :rtype: LiveEncodingEventName
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        # type: (LiveEncodingEventName) -> None
        """Sets the event_type of this LiveEncodingStatsEventDetails.


        :param event_type: The event_type of this LiveEncodingStatsEventDetails.
        :type: LiveEncodingEventName
        """

        if event_type is not None:
            if not isinstance(event_type, LiveEncodingEventName):
                raise TypeError("Invalid type for `event_type`, type has to be `LiveEncodingEventName`")

        self._event_type = event_type

    @property
    def message(self):
        # type: () -> string_types
        """Gets the message of this LiveEncodingStatsEventDetails.

        Short description of the event

        :return: The message of this LiveEncodingStatsEventDetails.
        :rtype: string_types
        """
        return self._message

    @message.setter
    def message(self, message):
        # type: (string_types) -> None
        """Sets the message of this LiveEncodingStatsEventDetails.

        Short description of the event

        :param message: The message of this LiveEncodingStatsEventDetails.
        :type: string_types
        """

        if message is not None:
            if not isinstance(message, string_types):
                raise TypeError("Invalid type for `message`, type has to be `string_types`")

        self._message = message

    @property
    def source(self):
        # type: () -> ClockSynchronizationMode
        """Gets the source of this LiveEncodingStatsEventDetails.

        Source used for clock-synchronization

        :return: The source of this LiveEncodingStatsEventDetails.
        :rtype: ClockSynchronizationMode
        """
        return self._source

    @source.setter
    def source(self, source):
        # type: (ClockSynchronizationMode) -> None
        """Sets the source of this LiveEncodingStatsEventDetails.

        Source used for clock-synchronization

        :param source: The source of this LiveEncodingStatsEventDetails.
        :type: ClockSynchronizationMode
        """

        if source is not None:
            if not isinstance(source, ClockSynchronizationMode):
                raise TypeError("Invalid type for `source`, type has to be `ClockSynchronizationMode`")

        self._source = source

    @property
    def year(self):
        # type: () -> int
        """Gets the year of this LiveEncodingStatsEventDetails.

        Year specified in picture timing

        :return: The year of this LiveEncodingStatsEventDetails.
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        # type: (int) -> None
        """Sets the year of this LiveEncodingStatsEventDetails.

        Year specified in picture timing

        :param year: The year of this LiveEncodingStatsEventDetails.
        :type: int
        """

        if year is not None:
            if not isinstance(year, int):
                raise TypeError("Invalid type for `year`, type has to be `int`")

        self._year = year

    @property
    def month(self):
        # type: () -> int
        """Gets the month of this LiveEncodingStatsEventDetails.

        Month specified in picture timing

        :return: The month of this LiveEncodingStatsEventDetails.
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        # type: (int) -> None
        """Sets the month of this LiveEncodingStatsEventDetails.

        Month specified in picture timing

        :param month: The month of this LiveEncodingStatsEventDetails.
        :type: int
        """

        if month is not None:
            if not isinstance(month, int):
                raise TypeError("Invalid type for `month`, type has to be `int`")

        self._month = month

    @property
    def day(self):
        # type: () -> int
        """Gets the day of this LiveEncodingStatsEventDetails.

        Day specified in picture timing

        :return: The day of this LiveEncodingStatsEventDetails.
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        # type: (int) -> None
        """Sets the day of this LiveEncodingStatsEventDetails.

        Day specified in picture timing

        :param day: The day of this LiveEncodingStatsEventDetails.
        :type: int
        """

        if day is not None:
            if not isinstance(day, int):
                raise TypeError("Invalid type for `day`, type has to be `int`")

        self._day = day

    @property
    def hours(self):
        # type: () -> int
        """Gets the hours of this LiveEncodingStatsEventDetails.

        Hours specified in picture timing

        :return: The hours of this LiveEncodingStatsEventDetails.
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        # type: (int) -> None
        """Sets the hours of this LiveEncodingStatsEventDetails.

        Hours specified in picture timing

        :param hours: The hours of this LiveEncodingStatsEventDetails.
        :type: int
        """

        if hours is not None:
            if not isinstance(hours, int):
                raise TypeError("Invalid type for `hours`, type has to be `int`")

        self._hours = hours

    @property
    def minutes(self):
        # type: () -> int
        """Gets the minutes of this LiveEncodingStatsEventDetails.

        Minutes specified in picture timing

        :return: The minutes of this LiveEncodingStatsEventDetails.
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        # type: (int) -> None
        """Sets the minutes of this LiveEncodingStatsEventDetails.

        Minutes specified in picture timing

        :param minutes: The minutes of this LiveEncodingStatsEventDetails.
        :type: int
        """

        if minutes is not None:
            if not isinstance(minutes, int):
                raise TypeError("Invalid type for `minutes`, type has to be `int`")

        self._minutes = minutes

    @property
    def seconds(self):
        # type: () -> int
        """Gets the seconds of this LiveEncodingStatsEventDetails.

        Seconds specified in picture timing

        :return: The seconds of this LiveEncodingStatsEventDetails.
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        # type: (int) -> None
        """Sets the seconds of this LiveEncodingStatsEventDetails.

        Seconds specified in picture timing

        :param seconds: The seconds of this LiveEncodingStatsEventDetails.
        :type: int
        """

        if seconds is not None:
            if not isinstance(seconds, int):
                raise TypeError("Invalid type for `seconds`, type has to be `int`")

        self._seconds = seconds

    @property
    def micro_seconds(self):
        # type: () -> int
        """Gets the micro_seconds of this LiveEncodingStatsEventDetails.

        Microseconds specified in picture timing

        :return: The micro_seconds of this LiveEncodingStatsEventDetails.
        :rtype: int
        """
        return self._micro_seconds

    @micro_seconds.setter
    def micro_seconds(self, micro_seconds):
        # type: (int) -> None
        """Sets the micro_seconds of this LiveEncodingStatsEventDetails.

        Microseconds specified in picture timing

        :param micro_seconds: The micro_seconds of this LiveEncodingStatsEventDetails.
        :type: int
        """

        if micro_seconds is not None:
            if not isinstance(micro_seconds, int):
                raise TypeError("Invalid type for `micro_seconds`, type has to be `int`")

        self._micro_seconds = micro_seconds

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
        if not isinstance(other, LiveEncodingStatsEventDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
