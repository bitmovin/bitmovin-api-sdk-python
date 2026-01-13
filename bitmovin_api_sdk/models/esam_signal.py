# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class EsamSignal(object):
    @poscheck_model
    def __init__(self,
                 offset=None,
                 binary=None,
                 interval=None,
                 end=None):
        # type: (string_types, string_types, string_types, string_types) -> None

        self._offset = None
        self._binary = None
        self._interval = None
        self._end = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if binary is not None:
            self.binary = binary
        if interval is not None:
            self.interval = interval
        if end is not None:
            self.end = end

    @property
    def openapi_types(self):
        types = {
            'offset': 'string_types',
            'binary': 'string_types',
            'interval': 'string_types',
            'end': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'offset': 'offset',
            'binary': 'binary',
            'interval': 'interval',
            'end': 'end'
        }
        return attributes

    @property
    def offset(self):
        # type: () -> string_types
        """Gets the offset of this EsamSignal.

        The offset from the matched signal in ISO 8601 duration format, accurate to milliseconds

        :return: The offset of this EsamSignal.
        :rtype: string_types
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        # type: (string_types) -> None
        """Sets the offset of this EsamSignal.

        The offset from the matched signal in ISO 8601 duration format, accurate to milliseconds

        :param offset: The offset of this EsamSignal.
        :type: string_types
        """

        if offset is not None:
            if not isinstance(offset, string_types):
                raise TypeError("Invalid type for `offset`, type has to be `string_types`")

        self._offset = offset

    @property
    def binary(self):
        # type: () -> string_types
        """Gets the binary of this EsamSignal.

        Base64-encoded SCTE-35 binary data to be inserted into the stream (required)

        :return: The binary of this EsamSignal.
        :rtype: string_types
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        # type: (string_types) -> None
        """Sets the binary of this EsamSignal.

        Base64-encoded SCTE-35 binary data to be inserted into the stream (required)

        :param binary: The binary of this EsamSignal.
        :type: string_types
        """

        if binary is not None:
            if not isinstance(binary, string_types):
                raise TypeError("Invalid type for `binary`, type has to be `string_types`")

        self._binary = binary

    @property
    def interval(self):
        # type: () -> string_types
        """Gets the interval of this EsamSignal.

        Interval in ISO 8601 duration format for which the signal should be repeated.  A signal may be specified as repeating when the interval and end attributes are present.  In this case, the signal is executed at the time specified by offset and again at the time  specified by adding interval to offset. This should be continued until reaching the duration  of offset + end. 

        :return: The interval of this EsamSignal.
        :rtype: string_types
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        # type: (string_types) -> None
        """Sets the interval of this EsamSignal.

        Interval in ISO 8601 duration format for which the signal should be repeated.  A signal may be specified as repeating when the interval and end attributes are present.  In this case, the signal is executed at the time specified by offset and again at the time  specified by adding interval to offset. This should be continued until reaching the duration  of offset + end. 

        :param interval: The interval of this EsamSignal.
        :type: string_types
        """

        if interval is not None:
            if not isinstance(interval, string_types):
                raise TypeError("Invalid type for `interval`, type has to be `string_types`")

        self._interval = interval

    @property
    def end(self):
        # type: () -> string_types
        """Gets the end of this EsamSignal.

        End duration in ISO 8601 duration format when a repeated signal should stop being repeated

        :return: The end of this EsamSignal.
        :rtype: string_types
        """
        return self._end

    @end.setter
    def end(self, end):
        # type: (string_types) -> None
        """Sets the end of this EsamSignal.

        End duration in ISO 8601 duration format when a repeated signal should stop being repeated

        :param end: The end of this EsamSignal.
        :type: string_types
        """

        if end is not None:
            if not isinstance(end, string_types):
                raise TypeError("Invalid type for `end`, type has to be `string_types`")

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
        if not isinstance(other, EsamSignal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
