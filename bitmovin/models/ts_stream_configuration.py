# coding: utf-8
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class TsStreamConfiguration(object):
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
            'stream_id': 'str',
            'pid': 'int'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'stream_id': 'streamId',
            'pid': 'pid'
        }
        return attributes

    def __init__(self, stream_id=None, pid=None, *args, **kwargs):

        self._stream_id = None
        self._pid = None
        self.discriminator = None

        if stream_id is not None:
            self.stream_id = stream_id
        if pid is not None:
            self.pid = pid

    @property
    def stream_id(self):
        """Gets the stream_id of this TsStreamConfiguration.

        The UUID of the stream to which this configuration belongs to. This has to be a ID of a stream that has been added to the current muxing. (required)

        :return: The stream_id of this TsStreamConfiguration.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this TsStreamConfiguration.

        The UUID of the stream to which this configuration belongs to. This has to be a ID of a stream that has been added to the current muxing. (required)

        :param stream_id: The stream_id of this TsStreamConfiguration.
        :type: str
        """

        if stream_id is not None:
            if not isinstance(stream_id, str):
                raise TypeError("Invalid type for `stream_id`, type has to be `str`")

        self._stream_id = stream_id


    @property
    def pid(self):
        """Gets the pid of this TsStreamConfiguration.

        An integer value. MPEG Transport Stream Packet Identifier (PID) for this stream. (required)

        :return: The pid of this TsStreamConfiguration.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this TsStreamConfiguration.

        An integer value. MPEG Transport Stream Packet Identifier (PID) for this stream. (required)

        :param pid: The pid of this TsStreamConfiguration.
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
            if issubclass(TsStreamConfiguration, dict):
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
        if not isinstance(other, TsStreamConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
