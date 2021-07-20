# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.filter import Filter
from bitmovin_api_sdk.models.position_unit import PositionUnit
import pprint
import six


class CropFilter(Filter):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 left=None,
                 right=None,
                 top=None,
                 bottom=None,
                 unit=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, int, int, PositionUnit) -> None
        super(CropFilter, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._left = None
        self._right = None
        self._top = None
        self._bottom = None
        self._unit = None
        self.discriminator = None

        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        if top is not None:
            self.top = top
        if bottom is not None:
            self.bottom = bottom
        if unit is not None:
            self.unit = unit

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(CropFilter, self), 'openapi_types'):
            types = getattr(super(CropFilter, self), 'openapi_types')

        types.update({
            'left': 'int',
            'right': 'int',
            'top': 'int',
            'bottom': 'int',
            'unit': 'PositionUnit'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(CropFilter, self), 'attribute_map'):
            attributes = getattr(super(CropFilter, self), 'attribute_map')

        attributes.update({
            'left': 'left',
            'right': 'right',
            'top': 'top',
            'bottom': 'bottom',
            'unit': 'unit'
        })
        return attributes

    @property
    def left(self):
        # type: () -> int
        """Gets the left of this CropFilter.

        Amount of pixels that will be cropped of the input video from the left side. Must be zero or a positive value.

        :return: The left of this CropFilter.
        :rtype: int
        """
        return self._left

    @left.setter
    def left(self, left):
        # type: (int) -> None
        """Sets the left of this CropFilter.

        Amount of pixels that will be cropped of the input video from the left side. Must be zero or a positive value.

        :param left: The left of this CropFilter.
        :type: int
        """

        if left is not None:
            if not isinstance(left, int):
                raise TypeError("Invalid type for `left`, type has to be `int`")

        self._left = left

    @property
    def right(self):
        # type: () -> int
        """Gets the right of this CropFilter.

        Amount of pixels that will be cropped of the input video from the right side. Must be zero or a positive value.

        :return: The right of this CropFilter.
        :rtype: int
        """
        return self._right

    @right.setter
    def right(self, right):
        # type: (int) -> None
        """Sets the right of this CropFilter.

        Amount of pixels that will be cropped of the input video from the right side. Must be zero or a positive value.

        :param right: The right of this CropFilter.
        :type: int
        """

        if right is not None:
            if not isinstance(right, int):
                raise TypeError("Invalid type for `right`, type has to be `int`")

        self._right = right

    @property
    def top(self):
        # type: () -> int
        """Gets the top of this CropFilter.

        Amount of pixels that will be cropped of the input video from the top. Must be zero or a positive value.

        :return: The top of this CropFilter.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        # type: (int) -> None
        """Sets the top of this CropFilter.

        Amount of pixels that will be cropped of the input video from the top. Must be zero or a positive value.

        :param top: The top of this CropFilter.
        :type: int
        """

        if top is not None:
            if not isinstance(top, int):
                raise TypeError("Invalid type for `top`, type has to be `int`")

        self._top = top

    @property
    def bottom(self):
        # type: () -> int
        """Gets the bottom of this CropFilter.

        Amount of pixels that will be cropped of the input video from the bottom. Must be zero or a positive value.

        :return: The bottom of this CropFilter.
        :rtype: int
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        # type: (int) -> None
        """Sets the bottom of this CropFilter.

        Amount of pixels that will be cropped of the input video from the bottom. Must be zero or a positive value.

        :param bottom: The bottom of this CropFilter.
        :type: int
        """

        if bottom is not None:
            if not isinstance(bottom, int):
                raise TypeError("Invalid type for `bottom`, type has to be `int`")

        self._bottom = bottom

    @property
    def unit(self):
        # type: () -> PositionUnit
        """Gets the unit of this CropFilter.


        :return: The unit of this CropFilter.
        :rtype: PositionUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        # type: (PositionUnit) -> None
        """Sets the unit of this CropFilter.


        :param unit: The unit of this CropFilter.
        :type: PositionUnit
        """

        if unit is not None:
            if not isinstance(unit, PositionUnit):
                raise TypeError("Invalid type for `unit`, type has to be `PositionUnit`")

        self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(CropFilter, self), "to_dict"):
            result = super(CropFilter, self).to_dict()
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
        if not isinstance(other, CropFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
