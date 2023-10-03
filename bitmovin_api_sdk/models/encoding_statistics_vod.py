# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.encoding_statistics import EncodingStatistics
import pprint
import six


class EncodingStatisticsVod(EncodingStatistics):
    @poscheck_model
    def __init__(self,
                 date_=None,
                 bytes_encoded=None,
                 time_encoded=None,
                 bytes_egress=None,
                 billable_encoding_minutes=None,
                 billable_egress_bytes=None,
                 streams=None,
                 muxings=None,
                 features=None,
                 billable_transmuxing_minutes=None,
                 billable_feature_minutes=None,
                 time_enqueued=None,
                 realtime_factor=None):
        # type: (date, int, int, int, list[BillableEncodingMinutes], list[EgressInformation], list[StatisticsPerStream], list[StatisticsPerMuxing], list[BillableEncodingFeatureMinutes], float, float, int, float) -> None
        super(EncodingStatisticsVod, self).__init__(date_=date_, bytes_encoded=bytes_encoded, time_encoded=time_encoded, bytes_egress=bytes_egress, billable_encoding_minutes=billable_encoding_minutes, billable_egress_bytes=billable_egress_bytes, streams=streams, muxings=muxings, features=features, billable_transmuxing_minutes=billable_transmuxing_minutes, billable_feature_minutes=billable_feature_minutes)

        self._time_enqueued = None
        self._realtime_factor = None
        self.discriminator = None

        if time_enqueued is not None:
            self.time_enqueued = time_enqueued
        if realtime_factor is not None:
            self.realtime_factor = realtime_factor

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(EncodingStatisticsVod, self), 'openapi_types'):
            types = getattr(super(EncodingStatisticsVod, self), 'openapi_types')

        types.update({
            'time_enqueued': 'int',
            'realtime_factor': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(EncodingStatisticsVod, self), 'attribute_map'):
            attributes = getattr(super(EncodingStatisticsVod, self), 'attribute_map')

        attributes.update({
            'time_enqueued': 'timeEnqueued',
            'realtime_factor': 'realtimeFactor'
        })
        return attributes

    @property
    def time_enqueued(self):
        # type: () -> int
        """Gets the time_enqueued of this EncodingStatisticsVod.

        Time in seconds encoded for this encoding. (required)

        :return: The time_enqueued of this EncodingStatisticsVod.
        :rtype: int
        """
        return self._time_enqueued

    @time_enqueued.setter
    def time_enqueued(self, time_enqueued):
        # type: (int) -> None
        """Sets the time_enqueued of this EncodingStatisticsVod.

        Time in seconds encoded for this encoding. (required)

        :param time_enqueued: The time_enqueued of this EncodingStatisticsVod.
        :type: int
        """

        if time_enqueued is not None:
            if not isinstance(time_enqueued, int):
                raise TypeError("Invalid type for `time_enqueued`, type has to be `int`")

        self._time_enqueued = time_enqueued

    @property
    def realtime_factor(self):
        # type: () -> float
        """Gets the realtime_factor of this EncodingStatisticsVod.

        The realtime factor. (required)

        :return: The realtime_factor of this EncodingStatisticsVod.
        :rtype: float
        """
        return self._realtime_factor

    @realtime_factor.setter
    def realtime_factor(self, realtime_factor):
        # type: (float) -> None
        """Sets the realtime_factor of this EncodingStatisticsVod.

        The realtime factor. (required)

        :param realtime_factor: The realtime_factor of this EncodingStatisticsVod.
        :type: float
        """

        if realtime_factor is not None:
            if not isinstance(realtime_factor, (float, int)):
                raise TypeError("Invalid type for `realtime_factor`, type has to be `float`")

        self._realtime_factor = realtime_factor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(EncodingStatisticsVod, self), "to_dict"):
            result = super(EncodingStatisticsVod, self).to_dict()
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
        if not isinstance(other, EncodingStatisticsVod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
