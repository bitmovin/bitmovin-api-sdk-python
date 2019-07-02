# coding: utf-8
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class TsProgramClockReferenceConfiguration(object):
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
            'pid': 'int',
            'interval': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'pid': 'pid',
            'interval': 'interval'
        }
        return attributes

    def __init__(self, pid=None, interval=None, *args, **kwargs):

        self._pid = None
        self._interval = None
        self.discriminator = None

        if pid is not None:
            self.pid = pid
        if interval is not None:
            self.interval = interval

    @property
    def pid(self):
        """Gets the pid of this TsProgramClockReferenceConfiguration.

        An integer value. Packet Identifier (PID) for the MPEG Transport Stream PCR. This should generally point to the video stream PID. If it is not explicitly set it will point to the video stream PID if exists, otherwise to the audio stream PID.

        :return: The pid of this TsProgramClockReferenceConfiguration.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this TsProgramClockReferenceConfiguration.

        An integer value. Packet Identifier (PID) for the MPEG Transport Stream PCR. This should generally point to the video stream PID. If it is not explicitly set it will point to the video stream PID if exists, otherwise to the audio stream PID.

        :param pid: The pid of this TsProgramClockReferenceConfiguration.
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


    @property
    def interval(self):
        """Gets the interval of this TsProgramClockReferenceConfiguration.

        An integer value. Nominal time between MPEG Transport Stream PCRs in milliseconds.

        :return: The interval of this TsProgramClockReferenceConfiguration.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this TsProgramClockReferenceConfiguration.

        An integer value. Nominal time between MPEG Transport Stream PCRs in milliseconds.

        :param interval: The interval of this TsProgramClockReferenceConfiguration.
        :type: int
        """

        if interval is not None:
            if interval is not None and interval > 65535:
                raise ValueError("Invalid value for `interval`, must be a value less than or equal to `65535`")
            if interval is not None and interval < 1:
                raise ValueError("Invalid value for `interval`, must be a value greater than or equal to `1`")
            if not isinstance(interval, int):
                raise TypeError("Invalid type for `interval`, type has to be `int`")

        self._interval = interval

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
            if issubclass(TsProgramClockReferenceConfiguration, dict):
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
        if not isinstance(other, TsProgramClockReferenceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
