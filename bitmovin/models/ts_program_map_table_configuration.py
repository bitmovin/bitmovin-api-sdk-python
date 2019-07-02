# coding: utf-8
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class TsProgramMapTableConfiguration(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

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

    def __init__(self, pid=None, *args, **kwargs):

        self._pid = None
        self.discriminator = None

        if pid is not None:
            self.pid = pid

    @property
    def pid(self):
        """Gets the pid of this TsProgramMapTableConfiguration.

        An integer value. Packet Identifier (PID) for the MPEG Transport Stream PMT.

        :return: The pid of this TsProgramMapTableConfiguration.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
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
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(TsProgramMapTableConfiguration, dict):
                for key, value in self.items():
                    result[key] = value

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
