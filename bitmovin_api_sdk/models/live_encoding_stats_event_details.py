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
                 event_type=None):
        # type: (LiveEncodingEventName) -> None

        self._event_type = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type

    @property
    def openapi_types(self):
        types = {
            'event_type': 'LiveEncodingEventName'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'event_type': 'eventType'
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
