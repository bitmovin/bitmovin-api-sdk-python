# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class EncodingStatistics(object):
    @poscheck_model
    def __init__(self,
                 date_=None,
                 bytes_encoded=None,
                 time_encoded=None):
        # type: (datetime, int, int) -> None

        self._date = None
        self._bytes_encoded = None
        self._time_encoded = None
        self.discriminator = None

        if date_ is not None:
            self.date = date_
        if bytes_encoded is not None:
            self.bytes_encoded = bytes_encoded
        if time_encoded is not None:
            self.time_encoded = time_encoded

    @property
    def openapi_types(self):
        types = {
            'date': 'datetime',
            'bytes_encoded': 'int',
            'time_encoded': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'date': 'date',
            'bytes_encoded': 'bytesEncoded',
            'time_encoded': 'timeEncoded'
        }
        return attributes

    @property
    def date(self):
        # type: () -> datetime
        """Gets the date of this EncodingStatistics.

        Date, format. yyyy-MM-dd (required)

        :return: The date of this EncodingStatistics.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date_):
        # type: (datetime) -> None
        """Sets the date of this EncodingStatistics.

        Date, format. yyyy-MM-dd (required)

        :param date_: The date of this EncodingStatistics.
        :type: datetime
        """

        if date_ is not None:
            if not isinstance(date_, datetime):
                raise TypeError("Invalid type for `date`, type has to be `datetime`")

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
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
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
