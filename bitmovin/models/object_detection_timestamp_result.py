# coding: utf-8

from bitmovin.models.bitmovin_response import BitmovinResponse
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class ObjectDetectionTimestampResult(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(ObjectDetectionTimestampResult, self).openapi_types
        types.update({
            'timestamp': 'float',
            'objects': 'list[ObjectDetectionResult]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(ObjectDetectionTimestampResult, self).attribute_map
        attributes.update({
            'timestamp': 'timestamp',
            'objects': 'objects'
        })
        return attributes

    def __init__(self, timestamp=None, objects=None, *args, **kwargs):
        super(ObjectDetectionTimestampResult, self).__init__(*args, **kwargs)

        self._timestamp = None
        self._objects = list()
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if objects is not None:
            self.objects = objects

    @property
    def timestamp(self):
        """Gets the timestamp of this ObjectDetectionTimestampResult.

        Time in seconds where the object was detected in the video

        :return: The timestamp of this ObjectDetectionTimestampResult.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ObjectDetectionTimestampResult.

        Time in seconds where the object was detected in the video

        :param timestamp: The timestamp of this ObjectDetectionTimestampResult.
        :type: float
        """

        if timestamp is not None:
            if not isinstance(timestamp, (float, int)):
                raise TypeError("Invalid type for `timestamp`, type has to be `float`")

        self._timestamp = timestamp


    @property
    def objects(self):
        """Gets the objects of this ObjectDetectionTimestampResult.

        Objects detected for the given timestamp

        :return: The objects of this ObjectDetectionTimestampResult.
        :rtype: list[ObjectDetectionResult]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this ObjectDetectionTimestampResult.

        Objects detected for the given timestamp

        :param objects: The objects of this ObjectDetectionTimestampResult.
        :type: list[ObjectDetectionResult]
        """

        if objects is not None:
            if not isinstance(objects, list):
                raise TypeError("Invalid type for `objects`, type has to be `list[ObjectDetectionResult]`")

        self._objects = objects

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(ObjectDetectionTimestampResult, self).to_dict()

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
            if issubclass(ObjectDetectionTimestampResult, dict):
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
        if not isinstance(other, ObjectDetectionTimestampResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
