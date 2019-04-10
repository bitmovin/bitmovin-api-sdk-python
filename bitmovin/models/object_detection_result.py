# coding: utf-8

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.object_detection_bounding_box import ObjectDetectionBoundingBox
import pprint
import six
from datetime import datetime
from enum import Enum


class ObjectDetectionResult(BitmovinResponse):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(ObjectDetectionResult, self).openapi_types
        types.update({
            'detected_object': 'str',
            'timestamp': 'float',
            'score': 'float',
            'bounding_box': 'ObjectDetectionBoundingBox'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(ObjectDetectionResult, self).attribute_map
        attributes.update({
            'detected_object': 'detectedObject',
            'timestamp': 'timestamp',
            'score': 'score',
            'bounding_box': 'boundingBox'
        })
        return attributes

    def __init__(self, detected_object=None, timestamp=None, score=None, bounding_box=None, *args, **kwargs):
        super(ObjectDetectionResult, self).__init__(*args, **kwargs)

        self._detected_object = None
        self._timestamp = None
        self._score = None
        self._bounding_box = None
        self.discriminator = None

        if detected_object is not None:
            self.detected_object = detected_object
        if timestamp is not None:
            self.timestamp = timestamp
        if score is not None:
            self.score = score
        if bounding_box is not None:
            self.bounding_box = bounding_box

    @property
    def detected_object(self):
        """Gets the detected_object of this ObjectDetectionResult.

        Name of the object that has been detected (in English)

        :return: The detected_object of this ObjectDetectionResult.
        :rtype: str
        """
        return self._detected_object

    @detected_object.setter
    def detected_object(self, detected_object):
        """Sets the detected_object of this ObjectDetectionResult.

        Name of the object that has been detected (in English)

        :param detected_object: The detected_object of this ObjectDetectionResult.
        :type: str
        """

        if detected_object is not None:
            if not isinstance(detected_object, str):
                raise TypeError("Invalid type for `detected_object`, type has to be `str`")

            self._detected_object = detected_object


    @property
    def timestamp(self):
        """Gets the timestamp of this ObjectDetectionResult.

        Time in seconds where the object was detected in the video

        :return: The timestamp of this ObjectDetectionResult.
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ObjectDetectionResult.

        Time in seconds where the object was detected in the video

        :param timestamp: The timestamp of this ObjectDetectionResult.
        :type: float
        """

        if timestamp is not None:
            if not isinstance(timestamp, float):
                raise TypeError("Invalid type for `timestamp`, type has to be `float`")

            self._timestamp = timestamp


    @property
    def score(self):
        """Gets the score of this ObjectDetectionResult.

        A number between 0 and 1 indicating the confidence of the detection

        :return: The score of this ObjectDetectionResult.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ObjectDetectionResult.

        A number between 0 and 1 indicating the confidence of the detection

        :param score: The score of this ObjectDetectionResult.
        :type: float
        """

        if score is not None:
            if not isinstance(score, float):
                raise TypeError("Invalid type for `score`, type has to be `float`")

            self._score = score


    @property
    def bounding_box(self):
        """Gets the bounding_box of this ObjectDetectionResult.

        A box indicating the position and size of the detected object within the frame

        :return: The bounding_box of this ObjectDetectionResult.
        :rtype: ObjectDetectionBoundingBox
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        """Sets the bounding_box of this ObjectDetectionResult.

        A box indicating the position and size of the detected object within the frame

        :param bounding_box: The bounding_box of this ObjectDetectionResult.
        :type: ObjectDetectionBoundingBox
        """

        if bounding_box is not None:
            if not isinstance(bounding_box, ObjectDetectionBoundingBox):
                raise TypeError("Invalid type for `bounding_box`, type has to be `ObjectDetectionBoundingBox`")

            self._bounding_box = bounding_box

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(ObjectDetectionResult, self).to_dict()

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
            if issubclass(ObjectDetectionResult, dict):
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
        if not isinstance(other, ObjectDetectionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
