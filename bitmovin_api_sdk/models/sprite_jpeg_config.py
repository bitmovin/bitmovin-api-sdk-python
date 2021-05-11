# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class SpriteJpegConfig(object):
    @poscheck_model
    def __init__(self,
                 quality=None):
        # type: (int) -> None

        self._quality = None
        self.discriminator = None

        if quality is not None:
            self.quality = quality

    @property
    def openapi_types(self):
        types = {
            'quality': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'quality': 'quality'
        }
        return attributes

    @property
    def quality(self):
        # type: () -> int
        """Gets the quality of this SpriteJpegConfig.

        Quality of the JPEG file in percent. Allowed values 20 - 100 (required)

        :return: The quality of this SpriteJpegConfig.
        :rtype: int
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        # type: (int) -> None
        """Sets the quality of this SpriteJpegConfig.

        Quality of the JPEG file in percent. Allowed values 20 - 100 (required)

        :param quality: The quality of this SpriteJpegConfig.
        :type: int
        """

        if quality is not None:
            if quality is not None and quality > 100:
                raise ValueError("Invalid value for `quality`, must be a value less than or equal to `100`")
            if quality is not None and quality < 20:
                raise ValueError("Invalid value for `quality`, must be a value greater than or equal to `20`")
            if not isinstance(quality, int):
                raise TypeError("Invalid type for `quality`, type has to be `int`")

        self._quality = quality

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
        if not isinstance(other, SpriteJpegConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
