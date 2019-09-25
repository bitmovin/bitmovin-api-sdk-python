# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_encoding_event_name import LiveEncodingEventName
import pprint
import six


class LiveEncodingStatsEventDetails(object):
    @poscheck_model
    def __init__(self,
                 event_name=None,
                 av_drift_in_seconds=None,
                 idle_duration_in_seconds=None,
                 error_message=None):
        # type: (LiveEncodingEventName, int, int, string_types) -> None

        self._event_name = None
        self._av_drift_in_seconds = None
        self._idle_duration_in_seconds = None
        self._error_message = None
        self.discriminator = None

        if event_name is not None:
            self.event_name = event_name
        if av_drift_in_seconds is not None:
            self.av_drift_in_seconds = av_drift_in_seconds
        if idle_duration_in_seconds is not None:
            self.idle_duration_in_seconds = idle_duration_in_seconds
        if error_message is not None:
            self.error_message = error_message

    @property
    def openapi_types(self):
        types = {
            'event_name': 'LiveEncodingEventName',
            'av_drift_in_seconds': 'int',
            'idle_duration_in_seconds': 'int',
            'error_message': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'event_name': 'eventName',
            'av_drift_in_seconds': 'avDriftInSeconds',
            'idle_duration_in_seconds': 'idleDurationInSeconds',
            'error_message': 'errorMessage'
        }
        return attributes

    @property
    def event_name(self):
        # type: () -> LiveEncodingEventName
        """Gets the event_name of this LiveEncodingStatsEventDetails.


        :return: The event_name of this LiveEncodingStatsEventDetails.
        :rtype: LiveEncodingEventName
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        # type: (LiveEncodingEventName) -> None
        """Sets the event_name of this LiveEncodingStatsEventDetails.


        :param event_name: The event_name of this LiveEncodingStatsEventDetails.
        :type: LiveEncodingEventName
        """

        if event_name is not None:
            if not isinstance(event_name, LiveEncodingEventName):
                raise TypeError("Invalid type for `event_name`, type has to be `LiveEncodingEventName`")

        self._event_name = event_name

    @property
    def av_drift_in_seconds(self):
        # type: () -> int
        """Gets the av_drift_in_seconds of this LiveEncodingStatsEventDetails.

        The Audio/Video Drift in seconds. The drift was corrected by the RESYNCING event (occurs at event: RESYNCING)

        :return: The av_drift_in_seconds of this LiveEncodingStatsEventDetails.
        :rtype: int
        """
        return self._av_drift_in_seconds

    @av_drift_in_seconds.setter
    def av_drift_in_seconds(self, av_drift_in_seconds):
        # type: (int) -> None
        """Sets the av_drift_in_seconds of this LiveEncodingStatsEventDetails.

        The Audio/Video Drift in seconds. The drift was corrected by the RESYNCING event (occurs at event: RESYNCING)

        :param av_drift_in_seconds: The av_drift_in_seconds of this LiveEncodingStatsEventDetails.
        :type: int
        """

        if av_drift_in_seconds is not None:
            if not isinstance(av_drift_in_seconds, int):
                raise TypeError("Invalid type for `av_drift_in_seconds`, type has to be `int`")

        self._av_drift_in_seconds = av_drift_in_seconds

    @property
    def idle_duration_in_seconds(self):
        # type: () -> int
        """Gets the idle_duration_in_seconds of this LiveEncodingStatsEventDetails.

        The time the stream was in idle state in seconds (occurs at event: IDLE)

        :return: The idle_duration_in_seconds of this LiveEncodingStatsEventDetails.
        :rtype: int
        """
        return self._idle_duration_in_seconds

    @idle_duration_in_seconds.setter
    def idle_duration_in_seconds(self, idle_duration_in_seconds):
        # type: (int) -> None
        """Sets the idle_duration_in_seconds of this LiveEncodingStatsEventDetails.

        The time the stream was in idle state in seconds (occurs at event: IDLE)

        :param idle_duration_in_seconds: The idle_duration_in_seconds of this LiveEncodingStatsEventDetails.
        :type: int
        """

        if idle_duration_in_seconds is not None:
            if not isinstance(idle_duration_in_seconds, int):
                raise TypeError("Invalid type for `idle_duration_in_seconds`, type has to be `int`")

        self._idle_duration_in_seconds = idle_duration_in_seconds

    @property
    def error_message(self):
        # type: () -> string_types
        """Gets the error_message of this LiveEncodingStatsEventDetails.

        An optional error message, when the event is in error state (occurs at event: ERROR)

        :return: The error_message of this LiveEncodingStatsEventDetails.
        :rtype: string_types
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        # type: (string_types) -> None
        """Sets the error_message of this LiveEncodingStatsEventDetails.

        An optional error message, when the event is in error state (occurs at event: ERROR)

        :param error_message: The error_message of this LiveEncodingStatsEventDetails.
        :type: string_types
        """

        if error_message is not None:
            if not isinstance(error_message, string_types):
                raise TypeError("Invalid type for `error_message`, type has to be `string_types`")

        self._error_message = error_message

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
