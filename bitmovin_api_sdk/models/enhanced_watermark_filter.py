# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.filter import Filter
from bitmovin_api_sdk.models.position_unit import PositionUnit
import pprint
import six


class EnhancedWatermarkFilter(Filter):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 image=None,
                 left=None,
                 right=None,
                 top=None,
                 bottom=None,
                 unit=None,
                 opacity=None,
                 width=None,
                 height=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, string_types, float, float, float, float, PositionUnit, float, float, float) -> None
        super(EnhancedWatermarkFilter, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._image = None
        self._left = None
        self._right = None
        self._top = None
        self._bottom = None
        self._unit = None
        self._opacity = None
        self._width = None
        self._height = None
        self.discriminator = None

        if image is not None:
            self.image = image
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
        if opacity is not None:
            self.opacity = opacity
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(EnhancedWatermarkFilter, self), 'openapi_types'):
            types = getattr(super(EnhancedWatermarkFilter, self), 'openapi_types')

        types.update({
            'image': 'string_types',
            'left': 'float',
            'right': 'float',
            'top': 'float',
            'bottom': 'float',
            'unit': 'PositionUnit',
            'opacity': 'float',
            'width': 'float',
            'height': 'float'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(EnhancedWatermarkFilter, self), 'attribute_map'):
            attributes = getattr(super(EnhancedWatermarkFilter, self), 'attribute_map')

        attributes.update({
            'image': 'image',
            'left': 'left',
            'right': 'right',
            'top': 'top',
            'bottom': 'bottom',
            'unit': 'unit',
            'opacity': 'opacity',
            'width': 'width',
            'height': 'height'
        })
        return attributes

    @property
    def image(self):
        # type: () -> string_types
        """Gets the image of this EnhancedWatermarkFilter.

        URL of the file to be used as watermark image. Supported image formats: PNG, JPEG, BMP, GIF (required)

        :return: The image of this EnhancedWatermarkFilter.
        :rtype: string_types
        """
        return self._image

    @image.setter
    def image(self, image):
        # type: (string_types) -> None
        """Sets the image of this EnhancedWatermarkFilter.

        URL of the file to be used as watermark image. Supported image formats: PNG, JPEG, BMP, GIF (required)

        :param image: The image of this EnhancedWatermarkFilter.
        :type: string_types
        """

        if image is not None:
            if not isinstance(image, string_types):
                raise TypeError("Invalid type for `image`, type has to be `string_types`")

        self._image = image

    @property
    def left(self):
        # type: () -> float
        """Gets the left of this EnhancedWatermarkFilter.

        Distance from the left edge of the input video to the left edge of the watermark image. May not be set if 'right' is set.

        :return: The left of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        # type: (float) -> None
        """Sets the left of this EnhancedWatermarkFilter.

        Distance from the left edge of the input video to the left edge of the watermark image. May not be set if 'right' is set.

        :param left: The left of this EnhancedWatermarkFilter.
        :type: float
        """

        if left is not None:
            if not isinstance(left, (float, int)):
                raise TypeError("Invalid type for `left`, type has to be `float`")

        self._left = left

    @property
    def right(self):
        # type: () -> float
        """Gets the right of this EnhancedWatermarkFilter.

        Distance from the right edge of the input video to the right edge of the watermark image . May not be set if 'left' is set.

        :return: The right of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._right

    @right.setter
    def right(self, right):
        # type: (float) -> None
        """Sets the right of this EnhancedWatermarkFilter.

        Distance from the right edge of the input video to the right edge of the watermark image . May not be set if 'left' is set.

        :param right: The right of this EnhancedWatermarkFilter.
        :type: float
        """

        if right is not None:
            if not isinstance(right, (float, int)):
                raise TypeError("Invalid type for `right`, type has to be `float`")

        self._right = right

    @property
    def top(self):
        # type: () -> float
        """Gets the top of this EnhancedWatermarkFilter.

        Distance from the top edge of the input video to the top edge of the watermark image. May not be set if 'bottom' is set.

        :return: The top of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        # type: (float) -> None
        """Sets the top of this EnhancedWatermarkFilter.

        Distance from the top edge of the input video to the top edge of the watermark image. May not be set if 'bottom' is set.

        :param top: The top of this EnhancedWatermarkFilter.
        :type: float
        """

        if top is not None:
            if not isinstance(top, (float, int)):
                raise TypeError("Invalid type for `top`, type has to be `float`")

        self._top = top

    @property
    def bottom(self):
        # type: () -> float
        """Gets the bottom of this EnhancedWatermarkFilter.

        Distance from the bottom edge of the input video to the bottom edge of the watermark image. May not be set if 'top' is set.

        :return: The bottom of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        # type: (float) -> None
        """Sets the bottom of this EnhancedWatermarkFilter.

        Distance from the bottom edge of the input video to the bottom edge of the watermark image. May not be set if 'top' is set.

        :param bottom: The bottom of this EnhancedWatermarkFilter.
        :type: float
        """

        if bottom is not None:
            if not isinstance(bottom, (float, int)):
                raise TypeError("Invalid type for `bottom`, type has to be `float`")

        self._bottom = bottom

    @property
    def unit(self):
        # type: () -> PositionUnit
        """Gets the unit of this EnhancedWatermarkFilter.


        :return: The unit of this EnhancedWatermarkFilter.
        :rtype: PositionUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        # type: (PositionUnit) -> None
        """Sets the unit of this EnhancedWatermarkFilter.


        :param unit: The unit of this EnhancedWatermarkFilter.
        :type: PositionUnit
        """

        if unit is not None:
            if not isinstance(unit, PositionUnit):
                raise TypeError("Invalid type for `unit`, type has to be `PositionUnit`")

        self._unit = unit

    @property
    def opacity(self):
        # type: () -> float
        """Gets the opacity of this EnhancedWatermarkFilter.

        Opacity to apply on the watermark image. Valid values are from 0.0 (completely transparent) to 1.0 (not transparent at all)

        :return: The opacity of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        # type: (float) -> None
        """Sets the opacity of this EnhancedWatermarkFilter.

        Opacity to apply on the watermark image. Valid values are from 0.0 (completely transparent) to 1.0 (not transparent at all)

        :param opacity: The opacity of this EnhancedWatermarkFilter.
        :type: float
        """

        if opacity is not None:
            if not isinstance(opacity, (float, int)):
                raise TypeError("Invalid type for `opacity`, type has to be `float`")

        self._opacity = opacity

    @property
    def width(self):
        # type: () -> float
        """Gets the width of this EnhancedWatermarkFilter.

        Desired width of the watermark image, the unit of the parameter is specified separately by the parameter 'unit'. If both width and height are set the watermark size is fixed. If only one is set the aspect ratio of the image will be used to rescale it

        :return: The width of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        # type: (float) -> None
        """Sets the width of this EnhancedWatermarkFilter.

        Desired width of the watermark image, the unit of the parameter is specified separately by the parameter 'unit'. If both width and height are set the watermark size is fixed. If only one is set the aspect ratio of the image will be used to rescale it

        :param width: The width of this EnhancedWatermarkFilter.
        :type: float
        """

        if width is not None:
            if not isinstance(width, (float, int)):
                raise TypeError("Invalid type for `width`, type has to be `float`")

        self._width = width

    @property
    def height(self):
        # type: () -> float
        """Gets the height of this EnhancedWatermarkFilter.

        Desired height of the watermark image, the unit of the parameter is specified separately by the parameter 'unit'. If both width and height are set the watermark size is fixed. If only one is set the aspect ratio of the image will be used to rescale it

        :return: The height of this EnhancedWatermarkFilter.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        # type: (float) -> None
        """Sets the height of this EnhancedWatermarkFilter.

        Desired height of the watermark image, the unit of the parameter is specified separately by the parameter 'unit'. If both width and height are set the watermark size is fixed. If only one is set the aspect ratio of the image will be used to rescale it

        :param height: The height of this EnhancedWatermarkFilter.
        :type: float
        """

        if height is not None:
            if not isinstance(height, (float, int)):
                raise TypeError("Invalid type for `height`, type has to be `float`")

        self._height = height

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(EnhancedWatermarkFilter, self), "to_dict"):
            result = super(EnhancedWatermarkFilter, self).to_dict()
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
        if not isinstance(other, EnhancedWatermarkFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
