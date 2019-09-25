# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AppliedStreamSettings(object):
    @poscheck_model
    def __init__(self,
                 width=None,
                 height=None):
        # type: (int, int) -> None

        self._width = None
        self._height = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def openapi_types(self):
        types = {
            'width': 'int',
            'height': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'width': 'width',
            'height': 'height'
        }
        return attributes

    @property
    def width(self):
        # type: () -> int
        """Gets the width of this AppliedStreamSettings.

        The applied width. Useful if the width in the configuration was undefined

        :return: The width of this AppliedStreamSettings.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        # type: (int) -> None
        """Sets the width of this AppliedStreamSettings.

        The applied width. Useful if the width in the configuration was undefined

        :param width: The width of this AppliedStreamSettings.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

        self._width = width

    @property
    def height(self):
        # type: () -> int
        """Gets the height of this AppliedStreamSettings.

        The applied height. Useful if the height in the configuration was undefined

        :return: The height of this AppliedStreamSettings.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        # type: (int) -> None
        """Sets the height of this AppliedStreamSettings.

        The applied height. Useful if the height in the configuration was undefined

        :param height: The height of this AppliedStreamSettings.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

        self._height = height

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
        if not isinstance(other, AppliedStreamSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
