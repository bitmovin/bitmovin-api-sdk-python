# coding: utf-8
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class WebVttSidecarFileSegmentation(object):
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
            'segment_length': 'float'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'segment_length': 'segmentLength'
        }
        return attributes

    def __init__(self, segment_length=None, *args, **kwargs):

        self._segment_length = None
        self.discriminator = None

        if segment_length is not None:
            self.segment_length = segment_length

    @property
    def segment_length(self):
        """Gets the segment_length of this WebVttSidecarFileSegmentation.

        The length of the WebVTT fragments in seconds

        :return: The segment_length of this WebVttSidecarFileSegmentation.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        """Sets the segment_length of this WebVttSidecarFileSegmentation.

        The length of the WebVTT fragments in seconds

        :param segment_length: The segment_length of this WebVttSidecarFileSegmentation.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, (float, int)):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

        self._segment_length = segment_length

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
            if issubclass(WebVttSidecarFileSegmentation, dict):
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
        if not isinstance(other, WebVttSidecarFileSegmentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
