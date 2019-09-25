# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class WebVttSidecarFileSegmentation(object):
    @poscheck_model
    def __init__(self,
                 segment_length=None):
        # type: (float) -> None

        self._segment_length = None
        self.discriminator = None

        if segment_length is not None:
            self.segment_length = segment_length

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

    @property
    def segment_length(self):
        # type: () -> float
        """Gets the segment_length of this WebVttSidecarFileSegmentation.

        The length of the WebVTT fragments in seconds (required)

        :return: The segment_length of this WebVttSidecarFileSegmentation.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        # type: (float) -> None
        """Sets the segment_length of this WebVttSidecarFileSegmentation.

        The length of the WebVTT fragments in seconds (required)

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
        if not isinstance(other, WebVttSidecarFileSegmentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
