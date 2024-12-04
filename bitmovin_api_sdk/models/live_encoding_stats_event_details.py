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
                 event_type=None,
                 message=None,
                 mid_roll_asset_names=None,
                 duration_in_seconds=None):
        # type: (LiveEncodingEventName, string_types, list[string_types], float) -> None

        self._event_type = None
        self._message = None
        self._mid_roll_asset_names = list()
        self._duration_in_seconds = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if message is not None:
            self.message = message
        if mid_roll_asset_names is not None:
            self.mid_roll_asset_names = mid_roll_asset_names
        if duration_in_seconds is not None:
            self.duration_in_seconds = duration_in_seconds

    @property
    def openapi_types(self):
        types = {
            'event_type': 'LiveEncodingEventName',
            'message': 'string_types',
            'mid_roll_asset_names': 'list[string_types]',
            'duration_in_seconds': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'event_type': 'eventType',
            'message': 'message',
            'mid_roll_asset_names': 'midRollAssetNames',
            'duration_in_seconds': 'durationInSeconds'
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
    def mid_roll_asset_names(self):
        # type: () -> list[string_types]
        """Gets the mid_roll_asset_names of this LiveEncodingStatsEventDetails.

        Name of the mid roll asset name

        :return: The mid_roll_asset_names of this LiveEncodingStatsEventDetails.
        :rtype: list[string_types]
        """
        return self._mid_roll_asset_names

    @mid_roll_asset_names.setter
    def mid_roll_asset_names(self, mid_roll_asset_names):
        # type: (list) -> None
        """Sets the mid_roll_asset_names of this LiveEncodingStatsEventDetails.

        Name of the mid roll asset name

        :param mid_roll_asset_names: The mid_roll_asset_names of this LiveEncodingStatsEventDetails.
        :type: list[string_types]
        """

        if mid_roll_asset_names is not None:
            if not isinstance(mid_roll_asset_names, list):
                raise TypeError("Invalid type for `mid_roll_asset_names`, type has to be `list[string_types]`")

        self._mid_roll_asset_names = mid_roll_asset_names

    @property
    def duration_in_seconds(self):
        # type: () -> float
        """Gets the duration_in_seconds of this LiveEncodingStatsEventDetails.

        Duration in seconds

        :return: The duration_in_seconds of this LiveEncodingStatsEventDetails.
        :rtype: float
        """
        return self._duration_in_seconds

    @duration_in_seconds.setter
    def duration_in_seconds(self, duration_in_seconds):
        # type: (float) -> None
        """Sets the duration_in_seconds of this LiveEncodingStatsEventDetails.

        Duration in seconds

        :param duration_in_seconds: The duration_in_seconds of this LiveEncodingStatsEventDetails.
        :type: float
        """

        if duration_in_seconds is not None:
            if not isinstance(duration_in_seconds, (float, int)):
                raise TypeError("Invalid type for `duration_in_seconds`, type has to be `float`")

        self._duration_in_seconds = duration_in_seconds

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
