# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.live_encoding_heartbeat_ingest import LiveEncodingHeartbeatIngest
import pprint
import six


class LiveEncodingHeartbeat(object):
    @poscheck_model
    def __init__(self,
                 timestamp=None,
                 ingest=None,
                 events=None):
        # type: (datetime, LiveEncodingHeartbeatIngest, list[LiveEncodingHeartbeatEvent]) -> None

        self._timestamp = None
        self._ingest = None
        self._events = list()
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if ingest is not None:
            self.ingest = ingest
        if events is not None:
            self.events = events

    @property
    def openapi_types(self):
        types = {
            'timestamp': 'datetime',
            'ingest': 'LiveEncodingHeartbeatIngest',
            'events': 'list[LiveEncodingHeartbeatEvent]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'timestamp': 'timestamp',
            'ingest': 'ingest',
            'events': 'events'
        }
        return attributes

    @property
    def timestamp(self):
        # type: () -> datetime
        """Gets the timestamp of this LiveEncodingHeartbeat.

        timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The timestamp of this LiveEncodingHeartbeat.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        # type: (datetime) -> None
        """Sets the timestamp of this LiveEncodingHeartbeat.

        timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param timestamp: The timestamp of this LiveEncodingHeartbeat.
        :type: datetime
        """

        if timestamp is not None:
            if not isinstance(timestamp, datetime):
                raise TypeError("Invalid type for `timestamp`, type has to be `datetime`")

        self._timestamp = timestamp

    @property
    def ingest(self):
        # type: () -> LiveEncodingHeartbeatIngest
        """Gets the ingest of this LiveEncodingHeartbeat.

        Information about the live ingestion status 

        :return: The ingest of this LiveEncodingHeartbeat.
        :rtype: LiveEncodingHeartbeatIngest
        """
        return self._ingest

    @ingest.setter
    def ingest(self, ingest):
        # type: (LiveEncodingHeartbeatIngest) -> None
        """Sets the ingest of this LiveEncodingHeartbeat.

        Information about the live ingestion status 

        :param ingest: The ingest of this LiveEncodingHeartbeat.
        :type: LiveEncodingHeartbeatIngest
        """

        if ingest is not None:
            if not isinstance(ingest, LiveEncodingHeartbeatIngest):
                raise TypeError("Invalid type for `ingest`, type has to be `LiveEncodingHeartbeatIngest`")

        self._ingest = ingest

    @property
    def events(self):
        # type: () -> list[LiveEncodingHeartbeatEvent]
        """Gets the events of this LiveEncodingHeartbeat.

        Live encoding heartbeat events 

        :return: The events of this LiveEncodingHeartbeat.
        :rtype: list[LiveEncodingHeartbeatEvent]
        """
        return self._events

    @events.setter
    def events(self, events):
        # type: (list) -> None
        """Sets the events of this LiveEncodingHeartbeat.

        Live encoding heartbeat events 

        :param events: The events of this LiveEncodingHeartbeat.
        :type: list[LiveEncodingHeartbeatEvent]
        """

        if events is not None:
            if not isinstance(events, list):
                raise TypeError("Invalid type for `events`, type has to be `list[LiveEncodingHeartbeatEvent]`")

        self._events = events

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
        if not isinstance(other, LiveEncodingHeartbeat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
