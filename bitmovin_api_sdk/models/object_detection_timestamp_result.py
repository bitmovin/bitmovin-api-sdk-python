# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
import pprint
import six


class ObjectDetectionTimestampResult(BitmovinResponse):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 timestamp=None,
                 objects=None):
        # type: (string_types, float, list[ObjectDetectionResult]) -> None
        super(ObjectDetectionTimestampResult, self).__init__(id_=id_)

        self._timestamp = None
        self._objects = list()
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if objects is not None:
            self.objects = objects

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ObjectDetectionTimestampResult, self), 'openapi_types'):
            types = getattr(super(ObjectDetectionTimestampResult, self), 'openapi_types')

        types.update({
            'timestamp': 'float',
            'objects': 'list[ObjectDetectionResult]'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ObjectDetectionTimestampResult, self), 'attribute_map'):
            attributes = getattr(super(ObjectDetectionTimestampResult, self), 'attribute_map')

        attributes.update({
            'timestamp': 'timestamp',
            'objects': 'objects'
        })
        return attributes

    @property
    def timestamp(self):
        # type: () -> float
        """Gets the timestamp of this ObjectDetectionTimestampResult.

        Time in seconds where the object was detected in the video

        :return: The timestamp of this ObjectDetectionTimestampResult.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        # type: (float) -> None
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
        # type: () -> list[ObjectDetectionResult]
        """Gets the objects of this ObjectDetectionTimestampResult.

        Objects detected for the given timestamp

        :return: The objects of this ObjectDetectionTimestampResult.
        :rtype: list[ObjectDetectionResult]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        # type: (list) -> None
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
        result = {}

        if hasattr(super(ObjectDetectionTimestampResult, self), "to_dict"):
            result = super(ObjectDetectionTimestampResult, self).to_dict()
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
        if not isinstance(other, ObjectDetectionTimestampResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
