# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class TsProgramMapTableConfiguration(object):
    @poscheck_model
    def __init__(self,
                 pid=None):
        # type: (int) -> None

        self._pid = None
        self.discriminator = None

        if pid is not None:
            self.pid = pid

    @property
    def openapi_types(self):
        types = {
            'pid': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'pid': 'pid'
        }
        return attributes

    @property
    def pid(self):
        # type: () -> int
        """Gets the pid of this TsProgramMapTableConfiguration.

        An integer value. Packet Identifier (PID) for the MPEG Transport Stream PMT.

        :return: The pid of this TsProgramMapTableConfiguration.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        # type: (int) -> None
        """Sets the pid of this TsProgramMapTableConfiguration.

        An integer value. Packet Identifier (PID) for the MPEG Transport Stream PMT.

        :param pid: The pid of this TsProgramMapTableConfiguration.
        :type: int
        """

        if pid is not None:
            if pid is not None and pid > 8190:
                raise ValueError("Invalid value for `pid`, must be a value less than or equal to `8190`")
            if pid is not None and pid < 16:
                raise ValueError("Invalid value for `pid`, must be a value greater than or equal to `16`")
            if not isinstance(pid, int):
                raise TypeError("Invalid type for `pid`, type has to be `int`")

        self._pid = pid

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
        if not isinstance(other, TsProgramMapTableConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
