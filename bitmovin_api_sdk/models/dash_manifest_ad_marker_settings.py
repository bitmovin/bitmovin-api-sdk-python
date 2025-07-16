# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dash_scte35_event_stream_signalling import DashScte35EventStreamSignalling
from bitmovin_api_sdk.models.dash_scte35_period_option import DashScte35PeriodOption
import pprint
import six


class DashManifestAdMarkerSettings(object):
    @poscheck_model
    def __init__(self,
                 period_option=None,
                 event_stream_signalling=None):
        # type: (DashScte35PeriodOption, DashScte35EventStreamSignalling) -> None

        self._period_option = None
        self._event_stream_signalling = None
        self.discriminator = None

        if period_option is not None:
            self.period_option = period_option
        if event_stream_signalling is not None:
            self.event_stream_signalling = event_stream_signalling

    @property
    def openapi_types(self):
        types = {
            'period_option': 'DashScte35PeriodOption',
            'event_stream_signalling': 'DashScte35EventStreamSignalling'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'period_option': 'periodOption',
            'event_stream_signalling': 'eventStreamSignalling'
        }
        return attributes

    @property
    def period_option(self):
        # type: () -> DashScte35PeriodOption
        """Gets the period_option of this DashManifestAdMarkerSettings.


        :return: The period_option of this DashManifestAdMarkerSettings.
        :rtype: DashScte35PeriodOption
        """
        return self._period_option

    @period_option.setter
    def period_option(self, period_option):
        # type: (DashScte35PeriodOption) -> None
        """Sets the period_option of this DashManifestAdMarkerSettings.


        :param period_option: The period_option of this DashManifestAdMarkerSettings.
        :type: DashScte35PeriodOption
        """

        if period_option is not None:
            if not isinstance(period_option, DashScte35PeriodOption):
                raise TypeError("Invalid type for `period_option`, type has to be `DashScte35PeriodOption`")

        self._period_option = period_option

    @property
    def event_stream_signalling(self):
        # type: () -> DashScte35EventStreamSignalling
        """Gets the event_stream_signalling of this DashManifestAdMarkerSettings.


        :return: The event_stream_signalling of this DashManifestAdMarkerSettings.
        :rtype: DashScte35EventStreamSignalling
        """
        return self._event_stream_signalling

    @event_stream_signalling.setter
    def event_stream_signalling(self, event_stream_signalling):
        # type: (DashScte35EventStreamSignalling) -> None
        """Sets the event_stream_signalling of this DashManifestAdMarkerSettings.


        :param event_stream_signalling: The event_stream_signalling of this DashManifestAdMarkerSettings.
        :type: DashScte35EventStreamSignalling
        """

        if event_stream_signalling is not None:
            if not isinstance(event_stream_signalling, DashScte35EventStreamSignalling):
                raise TypeError("Invalid type for `event_stream_signalling`, type has to be `DashScte35EventStreamSignalling`")

        self._event_stream_signalling = event_stream_signalling

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
        if not isinstance(other, DashManifestAdMarkerSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
