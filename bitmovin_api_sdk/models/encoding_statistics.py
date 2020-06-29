# coding: utf-8

from enum import Enum
from datetime import date
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class EncodingStatistics(object):
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
                 billable_feature_minutes=None):
        # type: (date, int, int, int, list[BillableEncodingMinutes], list[EgressInformation], list[StatisticsPerStream], list[StatisticsPerMuxing], list[BillableEncodingFeatureMinutes], float, float) -> None

        self._date = None
        self._bytes_encoded = None
        self._time_encoded = None
        self._bytes_egress = None
        self._billable_encoding_minutes = list()
        self._billable_egress_bytes = list()
        self._streams = list()
        self._muxings = list()
        self._features = list()
        self._billable_transmuxing_minutes = None
        self._billable_feature_minutes = None
        self.discriminator = None

        if date_ is not None:
            self.date = date_
        if bytes_encoded is not None:
            self.bytes_encoded = bytes_encoded
        if time_encoded is not None:
            self.time_encoded = time_encoded
        if bytes_egress is not None:
            self.bytes_egress = bytes_egress
        if billable_encoding_minutes is not None:
            self.billable_encoding_minutes = billable_encoding_minutes
        if billable_egress_bytes is not None:
            self.billable_egress_bytes = billable_egress_bytes
        if streams is not None:
            self.streams = streams
        if muxings is not None:
            self.muxings = muxings
        if features is not None:
            self.features = features
        if billable_transmuxing_minutes is not None:
            self.billable_transmuxing_minutes = billable_transmuxing_minutes
        if billable_feature_minutes is not None:
            self.billable_feature_minutes = billable_feature_minutes

    @property
    def openapi_types(self):
        types = {
            'date': 'date',
            'bytes_encoded': 'int',
            'time_encoded': 'int',
            'bytes_egress': 'int',
            'billable_encoding_minutes': 'list[BillableEncodingMinutes]',
            'billable_egress_bytes': 'list[EgressInformation]',
            'streams': 'list[StatisticsPerStream]',
            'muxings': 'list[StatisticsPerMuxing]',
            'features': 'list[BillableEncodingFeatureMinutes]',
            'billable_transmuxing_minutes': 'float',
            'billable_feature_minutes': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'date': 'date',
            'bytes_encoded': 'bytesEncoded',
            'time_encoded': 'timeEncoded',
            'bytes_egress': 'bytesEgress',
            'billable_encoding_minutes': 'billableEncodingMinutes',
            'billable_egress_bytes': 'billableEgressBytes',
            'streams': 'streams',
            'muxings': 'muxings',
            'features': 'features',
            'billable_transmuxing_minutes': 'billableTransmuxingMinutes',
            'billable_feature_minutes': 'billableFeatureMinutes'
        }
        return attributes

    @property
    def date(self):
        # type: () -> date
        """Gets the date of this EncodingStatistics.

        Date, format. yyyy-MM-dd (required)

        :return: The date of this EncodingStatistics.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date_):
        # type: (date) -> None
        """Sets the date of this EncodingStatistics.

        Date, format. yyyy-MM-dd (required)

        :param date_: The date of this EncodingStatistics.
        :type: date
        """

        if date_ is not None:
            if not isinstance(date_, date):
                raise TypeError("Invalid type for `date`, type has to be `date`")

        self._date = date_

    @property
    def bytes_encoded(self):
        # type: () -> int
        """Gets the bytes_encoded of this EncodingStatistics.

        Bytes encoded for this encoding. (required)

        :return: The bytes_encoded of this EncodingStatistics.
        :rtype: int
        """
        return self._bytes_encoded

    @bytes_encoded.setter
    def bytes_encoded(self, bytes_encoded):
        # type: (int) -> None
        """Sets the bytes_encoded of this EncodingStatistics.

        Bytes encoded for this encoding. (required)

        :param bytes_encoded: The bytes_encoded of this EncodingStatistics.
        :type: int
        """

        if bytes_encoded is not None:
            if not isinstance(bytes_encoded, int):
                raise TypeError("Invalid type for `bytes_encoded`, type has to be `int`")

        self._bytes_encoded = bytes_encoded

    @property
    def time_encoded(self):
        # type: () -> int
        """Gets the time_encoded of this EncodingStatistics.

        Time in seconds encoded for this encoding. (required)

        :return: The time_encoded of this EncodingStatistics.
        :rtype: int
        """
        return self._time_encoded

    @time_encoded.setter
    def time_encoded(self, time_encoded):
        # type: (int) -> None
        """Sets the time_encoded of this EncodingStatistics.

        Time in seconds encoded for this encoding. (required)

        :param time_encoded: The time_encoded of this EncodingStatistics.
        :type: int
        """

        if time_encoded is not None:
            if not isinstance(time_encoded, int):
                raise TypeError("Invalid type for `time_encoded`, type has to be `int`")

        self._time_encoded = time_encoded

    @property
    def bytes_egress(self):
        # type: () -> int
        """Gets the bytes_egress of this EncodingStatistics.

        Egress output generated by file transfers in bytes (required)

        :return: The bytes_egress of this EncodingStatistics.
        :rtype: int
        """
        return self._bytes_egress

    @bytes_egress.setter
    def bytes_egress(self, bytes_egress):
        # type: (int) -> None
        """Sets the bytes_egress of this EncodingStatistics.

        Egress output generated by file transfers in bytes (required)

        :param bytes_egress: The bytes_egress of this EncodingStatistics.
        :type: int
        """

        if bytes_egress is not None:
            if not isinstance(bytes_egress, int):
                raise TypeError("Invalid type for `bytes_egress`, type has to be `int`")

        self._bytes_egress = bytes_egress

    @property
    def billable_encoding_minutes(self):
        # type: () -> list[BillableEncodingMinutes]
        """Gets the billable_encoding_minutes of this EncodingStatistics.


        :return: The billable_encoding_minutes of this EncodingStatistics.
        :rtype: list[BillableEncodingMinutes]
        """
        return self._billable_encoding_minutes

    @billable_encoding_minutes.setter
    def billable_encoding_minutes(self, billable_encoding_minutes):
        # type: (list) -> None
        """Sets the billable_encoding_minutes of this EncodingStatistics.


        :param billable_encoding_minutes: The billable_encoding_minutes of this EncodingStatistics.
        :type: list[BillableEncodingMinutes]
        """

        if billable_encoding_minutes is not None:
            if not isinstance(billable_encoding_minutes, list):
                raise TypeError("Invalid type for `billable_encoding_minutes`, type has to be `list[BillableEncodingMinutes]`")

        self._billable_encoding_minutes = billable_encoding_minutes

    @property
    def billable_egress_bytes(self):
        # type: () -> list[EgressInformation]
        """Gets the billable_egress_bytes of this EncodingStatistics.


        :return: The billable_egress_bytes of this EncodingStatistics.
        :rtype: list[EgressInformation]
        """
        return self._billable_egress_bytes

    @billable_egress_bytes.setter
    def billable_egress_bytes(self, billable_egress_bytes):
        # type: (list) -> None
        """Sets the billable_egress_bytes of this EncodingStatistics.


        :param billable_egress_bytes: The billable_egress_bytes of this EncodingStatistics.
        :type: list[EgressInformation]
        """

        if billable_egress_bytes is not None:
            if not isinstance(billable_egress_bytes, list):
                raise TypeError("Invalid type for `billable_egress_bytes`, type has to be `list[EgressInformation]`")

        self._billable_egress_bytes = billable_egress_bytes

    @property
    def streams(self):
        # type: () -> list[StatisticsPerStream]
        """Gets the streams of this EncodingStatistics.


        :return: The streams of this EncodingStatistics.
        :rtype: list[StatisticsPerStream]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        # type: (list) -> None
        """Sets the streams of this EncodingStatistics.


        :param streams: The streams of this EncodingStatistics.
        :type: list[StatisticsPerStream]
        """

        if streams is not None:
            if not isinstance(streams, list):
                raise TypeError("Invalid type for `streams`, type has to be `list[StatisticsPerStream]`")

        self._streams = streams

    @property
    def muxings(self):
        # type: () -> list[StatisticsPerMuxing]
        """Gets the muxings of this EncodingStatistics.


        :return: The muxings of this EncodingStatistics.
        :rtype: list[StatisticsPerMuxing]
        """
        return self._muxings

    @muxings.setter
    def muxings(self, muxings):
        # type: (list) -> None
        """Sets the muxings of this EncodingStatistics.


        :param muxings: The muxings of this EncodingStatistics.
        :type: list[StatisticsPerMuxing]
        """

        if muxings is not None:
            if not isinstance(muxings, list):
                raise TypeError("Invalid type for `muxings`, type has to be `list[StatisticsPerMuxing]`")

        self._muxings = muxings

    @property
    def features(self):
        # type: () -> list[BillableEncodingFeatureMinutes]
        """Gets the features of this EncodingStatistics.


        :return: The features of this EncodingStatistics.
        :rtype: list[BillableEncodingFeatureMinutes]
        """
        return self._features

    @features.setter
    def features(self, features):
        # type: (list) -> None
        """Sets the features of this EncodingStatistics.


        :param features: The features of this EncodingStatistics.
        :type: list[BillableEncodingFeatureMinutes]
        """

        if features is not None:
            if not isinstance(features, list):
                raise TypeError("Invalid type for `features`, type has to be `list[BillableEncodingFeatureMinutes]`")

        self._features = features

    @property
    def billable_transmuxing_minutes(self):
        # type: () -> float
        """Gets the billable_transmuxing_minutes of this EncodingStatistics.

        Billable minutes for the muxings.

        :return: The billable_transmuxing_minutes of this EncodingStatistics.
        :rtype: float
        """
        return self._billable_transmuxing_minutes

    @billable_transmuxing_minutes.setter
    def billable_transmuxing_minutes(self, billable_transmuxing_minutes):
        # type: (float) -> None
        """Sets the billable_transmuxing_minutes of this EncodingStatistics.

        Billable minutes for the muxings.

        :param billable_transmuxing_minutes: The billable_transmuxing_minutes of this EncodingStatistics.
        :type: float
        """

        if billable_transmuxing_minutes is not None:
            if not isinstance(billable_transmuxing_minutes, (float, int)):
                raise TypeError("Invalid type for `billable_transmuxing_minutes`, type has to be `float`")

        self._billable_transmuxing_minutes = billable_transmuxing_minutes

    @property
    def billable_feature_minutes(self):
        # type: () -> float
        """Gets the billable_feature_minutes of this EncodingStatistics.

        Billable minutes for the features.

        :return: The billable_feature_minutes of this EncodingStatistics.
        :rtype: float
        """
        return self._billable_feature_minutes

    @billable_feature_minutes.setter
    def billable_feature_minutes(self, billable_feature_minutes):
        # type: (float) -> None
        """Sets the billable_feature_minutes of this EncodingStatistics.

        Billable minutes for the features.

        :param billable_feature_minutes: The billable_feature_minutes of this EncodingStatistics.
        :type: float
        """

        if billable_feature_minutes is not None:
            if not isinstance(billable_feature_minutes, (float, int)):
                raise TypeError("Invalid type for `billable_feature_minutes`, type has to be `float`")

        self._billable_feature_minutes = billable_feature_minutes

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
        if not isinstance(other, EncodingStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
