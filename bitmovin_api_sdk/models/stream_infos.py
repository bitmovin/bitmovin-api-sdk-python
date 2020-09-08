# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamInfos(object):
    @poscheck_model
    def __init__(self,
                 time=None,
                 stream_infos=None):
        # type: (datetime, list[StreamInfosDetails]) -> None

        self._time = None
        self._stream_infos = list()
        self.discriminator = None

        if time is not None:
            self.time = time
        if stream_infos is not None:
            self.stream_infos = stream_infos

    @property
    def openapi_types(self):
        types = {
            'time': 'datetime',
            'stream_infos': 'list[StreamInfosDetails]'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'time': 'time',
            'stream_infos': 'streamInfos'
        }
        return attributes

    @property
    def time(self):
        # type: () -> datetime
        """Gets the time of this StreamInfos.

        Timestamp of the event, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ (required)

        :return: The time of this StreamInfos.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        # type: (datetime) -> None
        """Sets the time of this StreamInfos.

        Timestamp of the event, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ (required)

        :param time: The time of this StreamInfos.
        :type: datetime
        """

        if time is not None:
            if not isinstance(time, datetime):
                raise TypeError("Invalid type for `time`, type has to be `datetime`")

        self._time = time

    @property
    def stream_infos(self):
        # type: () -> list[StreamInfosDetails]
        """Gets the stream_infos of this StreamInfos.

        Details about billable minutes for each resolution category

        :return: The stream_infos of this StreamInfos.
        :rtype: list[StreamInfosDetails]
        """
        return self._stream_infos

    @stream_infos.setter
    def stream_infos(self, stream_infos):
        # type: (list) -> None
        """Sets the stream_infos of this StreamInfos.

        Details about billable minutes for each resolution category

        :param stream_infos: The stream_infos of this StreamInfos.
        :type: list[StreamInfosDetails]
        """

        if stream_infos is not None:
            if not isinstance(stream_infos, list):
                raise TypeError("Invalid type for `stream_infos`, type has to be `list[StreamInfosDetails]`")

        self._stream_infos = stream_infos

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
        if not isinstance(other, StreamInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
