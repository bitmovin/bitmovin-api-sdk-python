# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class TimeCode(object):
    @poscheck_model
    def __init__(self,
                 time_code_start=None):
        # type: (string_types) -> None

        self._time_code_start = None
        self.discriminator = None

        if time_code_start is not None:
            self.time_code_start = time_code_start

    @property
    def openapi_types(self):
        types = {
            'time_code_start': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'time_code_start': 'timeCodeStart'
        }
        return attributes

    @property
    def time_code_start(self):
        # type: () -> string_types
        """Gets the time_code_start of this TimeCode.

        Specify start timecode for writing.

        :return: The time_code_start of this TimeCode.
        :rtype: string_types
        """
        return self._time_code_start

    @time_code_start.setter
    def time_code_start(self, time_code_start):
        # type: (string_types) -> None
        """Sets the time_code_start of this TimeCode.

        Specify start timecode for writing.

        :param time_code_start: The time_code_start of this TimeCode.
        :type: string_types
        """

        if time_code_start is not None:
            if not isinstance(time_code_start, string_types):
                raise TypeError("Invalid type for `time_code_start`, type has to be `string_types`")

        self._time_code_start = time_code_start

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
        if not isinstance(other, TimeCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
