# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class ObjectDetectionBoundingBox(object):
    @poscheck_model
    def __init__(self,
                 top_left_x=None,
                 top_left_y=None,
                 bottom_right_x=None,
                 bottom_right_y=None):
        # type: (float, float, float, float) -> None

        self._top_left_x = None
        self._top_left_y = None
        self._bottom_right_x = None
        self._bottom_right_y = None
        self.discriminator = None

        if top_left_x is not None:
            self.top_left_x = top_left_x
        if top_left_y is not None:
            self.top_left_y = top_left_y
        if bottom_right_x is not None:
            self.bottom_right_x = bottom_right_x
        if bottom_right_y is not None:
            self.bottom_right_y = bottom_right_y

    @property
    def openapi_types(self):
        types = {
            'top_left_x': 'float',
            'top_left_y': 'float',
            'bottom_right_x': 'float',
            'bottom_right_y': 'float'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'top_left_x': 'topLeftX',
            'top_left_y': 'topLeftY',
            'bottom_right_x': 'bottomRightX',
            'bottom_right_y': 'bottomRightY'
        }
        return attributes

    @property
    def top_left_x(self):
        # type: () -> float
        """Gets the top_left_x of this ObjectDetectionBoundingBox.

        Horizontal position of the top left corner, given as a fraction of the frame width

        :return: The top_left_x of this ObjectDetectionBoundingBox.
        :rtype: float
        """
        return self._top_left_x

    @top_left_x.setter
    def top_left_x(self, top_left_x):
        # type: (float) -> None
        """Sets the top_left_x of this ObjectDetectionBoundingBox.

        Horizontal position of the top left corner, given as a fraction of the frame width

        :param top_left_x: The top_left_x of this ObjectDetectionBoundingBox.
        :type: float
        """

        if top_left_x is not None:
            if not isinstance(top_left_x, (float, int)):
                raise TypeError("Invalid type for `top_left_x`, type has to be `float`")

        self._top_left_x = top_left_x

    @property
    def top_left_y(self):
        # type: () -> float
        """Gets the top_left_y of this ObjectDetectionBoundingBox.

        Vertical position of the top left corner, given as a fraction of the frame height

        :return: The top_left_y of this ObjectDetectionBoundingBox.
        :rtype: float
        """
        return self._top_left_y

    @top_left_y.setter
    def top_left_y(self, top_left_y):
        # type: (float) -> None
        """Sets the top_left_y of this ObjectDetectionBoundingBox.

        Vertical position of the top left corner, given as a fraction of the frame height

        :param top_left_y: The top_left_y of this ObjectDetectionBoundingBox.
        :type: float
        """

        if top_left_y is not None:
            if not isinstance(top_left_y, (float, int)):
                raise TypeError("Invalid type for `top_left_y`, type has to be `float`")

        self._top_left_y = top_left_y

    @property
    def bottom_right_x(self):
        # type: () -> float
        """Gets the bottom_right_x of this ObjectDetectionBoundingBox.

        Horizontal position of the bottom right corner, given as a fraction of the frame width

        :return: The bottom_right_x of this ObjectDetectionBoundingBox.
        :rtype: float
        """
        return self._bottom_right_x

    @bottom_right_x.setter
    def bottom_right_x(self, bottom_right_x):
        # type: (float) -> None
        """Sets the bottom_right_x of this ObjectDetectionBoundingBox.

        Horizontal position of the bottom right corner, given as a fraction of the frame width

        :param bottom_right_x: The bottom_right_x of this ObjectDetectionBoundingBox.
        :type: float
        """

        if bottom_right_x is not None:
            if not isinstance(bottom_right_x, (float, int)):
                raise TypeError("Invalid type for `bottom_right_x`, type has to be `float`")

        self._bottom_right_x = bottom_right_x

    @property
    def bottom_right_y(self):
        # type: () -> float
        """Gets the bottom_right_y of this ObjectDetectionBoundingBox.

        Vertical position of the bottom right corner, given as a fraction of the frame height

        :return: The bottom_right_y of this ObjectDetectionBoundingBox.
        :rtype: float
        """
        return self._bottom_right_y

    @bottom_right_y.setter
    def bottom_right_y(self, bottom_right_y):
        # type: (float) -> None
        """Sets the bottom_right_y of this ObjectDetectionBoundingBox.

        Vertical position of the bottom right corner, given as a fraction of the frame height

        :param bottom_right_y: The bottom_right_y of this ObjectDetectionBoundingBox.
        :type: float
        """

        if bottom_right_y is not None:
            if not isinstance(bottom_right_y, (float, int)):
                raise TypeError("Invalid type for `bottom_right_y`, type has to be `float`")

        self._bottom_right_y = bottom_right_y

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
        if not isinstance(other, ObjectDetectionBoundingBox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
