# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.filter import Filter
from bitmovin_api_sdk.models.text_filter_font import TextFilterFont
import pprint
import six


class TextFilter(Filter):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 font=None,
                 box=None,
                 box_border_width=None,
                 box_color=None,
                 line_spacing=None,
                 border_width=None,
                 fix_bounds=None,
                 font_color=None,
                 font_size=None,
                 font_size_expression=None,
                 alpha=None,
                 shadow_color=None,
                 shadow_x=None,
                 shadow_y=None,
                 timecode=None,
                 text=None,
                 x=None,
                 y=None,
                 rate=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, TextFilterFont, bool, int, string_types, int, int, bool, string_types, int, string_types, float, string_types, int, int, string_types, string_types, string_types, string_types, string_types) -> None
        super(TextFilter, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._font = None
        self._box = None
        self._box_border_width = None
        self._box_color = None
        self._line_spacing = None
        self._border_width = None
        self._fix_bounds = None
        self._font_color = None
        self._font_size = None
        self._font_size_expression = None
        self._alpha = None
        self._shadow_color = None
        self._shadow_x = None
        self._shadow_y = None
        self._timecode = None
        self._text = None
        self._x = None
        self._y = None
        self._rate = None
        self.discriminator = None

        if font is not None:
            self.font = font
        if box is not None:
            self.box = box
        if box_border_width is not None:
            self.box_border_width = box_border_width
        if box_color is not None:
            self.box_color = box_color
        if line_spacing is not None:
            self.line_spacing = line_spacing
        if border_width is not None:
            self.border_width = border_width
        if fix_bounds is not None:
            self.fix_bounds = fix_bounds
        if font_color is not None:
            self.font_color = font_color
        if font_size is not None:
            self.font_size = font_size
        if font_size_expression is not None:
            self.font_size_expression = font_size_expression
        if alpha is not None:
            self.alpha = alpha
        if shadow_color is not None:
            self.shadow_color = shadow_color
        if shadow_x is not None:
            self.shadow_x = shadow_x
        if shadow_y is not None:
            self.shadow_y = shadow_y
        if timecode is not None:
            self.timecode = timecode
        if text is not None:
            self.text = text
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if rate is not None:
            self.rate = rate

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(TextFilter, self), 'openapi_types'):
            types = getattr(super(TextFilter, self), 'openapi_types')

        types.update({
            'font': 'TextFilterFont',
            'box': 'bool',
            'box_border_width': 'int',
            'box_color': 'string_types',
            'line_spacing': 'int',
            'border_width': 'int',
            'fix_bounds': 'bool',
            'font_color': 'string_types',
            'font_size': 'int',
            'font_size_expression': 'string_types',
            'alpha': 'float',
            'shadow_color': 'string_types',
            'shadow_x': 'int',
            'shadow_y': 'int',
            'timecode': 'string_types',
            'text': 'string_types',
            'x': 'string_types',
            'y': 'string_types',
            'rate': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(TextFilter, self), 'attribute_map'):
            attributes = getattr(super(TextFilter, self), 'attribute_map')

        attributes.update({
            'font': 'font',
            'box': 'box',
            'box_border_width': 'boxBorderWidth',
            'box_color': 'boxColor',
            'line_spacing': 'lineSpacing',
            'border_width': 'borderWidth',
            'fix_bounds': 'fixBounds',
            'font_color': 'fontColor',
            'font_size': 'fontSize',
            'font_size_expression': 'fontSizeExpression',
            'alpha': 'alpha',
            'shadow_color': 'shadowColor',
            'shadow_x': 'shadowX',
            'shadow_y': 'shadowY',
            'timecode': 'timecode',
            'text': 'text',
            'x': 'x',
            'y': 'y',
            'rate': 'rate'
        })
        return attributes

    @property
    def font(self):
        # type: () -> TextFilterFont
        """Gets the font of this TextFilter.


        :return: The font of this TextFilter.
        :rtype: TextFilterFont
        """
        return self._font

    @font.setter
    def font(self, font):
        # type: (TextFilterFont) -> None
        """Sets the font of this TextFilter.


        :param font: The font of this TextFilter.
        :type: TextFilterFont
        """

        if font is not None:
            if not isinstance(font, TextFilterFont):
                raise TypeError("Invalid type for `font`, type has to be `TextFilterFont`")

        self._font = font

    @property
    def box(self):
        # type: () -> bool
        """Gets the box of this TextFilter.

        If set to true a box is drawn around the text using the background color.

        :return: The box of this TextFilter.
        :rtype: bool
        """
        return self._box

    @box.setter
    def box(self, box):
        # type: (bool) -> None
        """Sets the box of this TextFilter.

        If set to true a box is drawn around the text using the background color.

        :param box: The box of this TextFilter.
        :type: bool
        """

        if box is not None:
            if not isinstance(box, bool):
                raise TypeError("Invalid type for `box`, type has to be `bool`")

        self._box = box

    @property
    def box_border_width(self):
        # type: () -> int
        """Gets the box_border_width of this TextFilter.

        The width of the box drawn around the text.

        :return: The box_border_width of this TextFilter.
        :rtype: int
        """
        return self._box_border_width

    @box_border_width.setter
    def box_border_width(self, box_border_width):
        # type: (int) -> None
        """Sets the box_border_width of this TextFilter.

        The width of the box drawn around the text.

        :param box_border_width: The box_border_width of this TextFilter.
        :type: int
        """

        if box_border_width is not None:
            if not isinstance(box_border_width, int):
                raise TypeError("Invalid type for `box_border_width`, type has to be `int`")

        self._box_border_width = box_border_width

    @property
    def box_color(self):
        # type: () -> string_types
        """Gets the box_color of this TextFilter.

        The background color to be used for drawing the box.

        :return: The box_color of this TextFilter.
        :rtype: string_types
        """
        return self._box_color

    @box_color.setter
    def box_color(self, box_color):
        # type: (string_types) -> None
        """Sets the box_color of this TextFilter.

        The background color to be used for drawing the box.

        :param box_color: The box_color of this TextFilter.
        :type: string_types
        """

        if box_color is not None:
            if not isinstance(box_color, string_types):
                raise TypeError("Invalid type for `box_color`, type has to be `string_types`")

        self._box_color = box_color

    @property
    def line_spacing(self):
        # type: () -> int
        """Gets the line_spacing of this TextFilter.

        Line spacing of the border around the box in pixels

        :return: The line_spacing of this TextFilter.
        :rtype: int
        """
        return self._line_spacing

    @line_spacing.setter
    def line_spacing(self, line_spacing):
        # type: (int) -> None
        """Sets the line_spacing of this TextFilter.

        Line spacing of the border around the box in pixels

        :param line_spacing: The line_spacing of this TextFilter.
        :type: int
        """

        if line_spacing is not None:
            if not isinstance(line_spacing, int):
                raise TypeError("Invalid type for `line_spacing`, type has to be `int`")

        self._line_spacing = line_spacing

    @property
    def border_width(self):
        # type: () -> int
        """Gets the border_width of this TextFilter.

        Width of the border around the text

        :return: The border_width of this TextFilter.
        :rtype: int
        """
        return self._border_width

    @border_width.setter
    def border_width(self, border_width):
        # type: (int) -> None
        """Sets the border_width of this TextFilter.

        Width of the border around the text

        :param border_width: The border_width of this TextFilter.
        :type: int
        """

        if border_width is not None:
            if not isinstance(border_width, int):
                raise TypeError("Invalid type for `border_width`, type has to be `int`")

        self._border_width = border_width

    @property
    def fix_bounds(self):
        # type: () -> bool
        """Gets the fix_bounds of this TextFilter.

        If set to true, it will fix text coordinates to avoid clipping if necessary

        :return: The fix_bounds of this TextFilter.
        :rtype: bool
        """
        return self._fix_bounds

    @fix_bounds.setter
    def fix_bounds(self, fix_bounds):
        # type: (bool) -> None
        """Sets the fix_bounds of this TextFilter.

        If set to true, it will fix text coordinates to avoid clipping if necessary

        :param fix_bounds: The fix_bounds of this TextFilter.
        :type: bool
        """

        if fix_bounds is not None:
            if not isinstance(fix_bounds, bool):
                raise TypeError("Invalid type for `fix_bounds`, type has to be `bool`")

        self._fix_bounds = fix_bounds

    @property
    def font_color(self):
        # type: () -> string_types
        """Gets the font_color of this TextFilter.

        The color to be used to draw the text

        :return: The font_color of this TextFilter.
        :rtype: string_types
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        # type: (string_types) -> None
        """Sets the font_color of this TextFilter.

        The color to be used to draw the text

        :param font_color: The font_color of this TextFilter.
        :type: string_types
        """

        if font_color is not None:
            if not isinstance(font_color, string_types):
                raise TypeError("Invalid type for `font_color`, type has to be `string_types`")

        self._font_color = font_color

    @property
    def font_size(self):
        # type: () -> int
        """Gets the font_size of this TextFilter.

        Font size to be used to draw the text

        :return: The font_size of this TextFilter.
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        # type: (int) -> None
        """Sets the font_size of this TextFilter.

        Font size to be used to draw the text

        :param font_size: The font_size of this TextFilter.
        :type: int
        """

        if font_size is not None:
            if not isinstance(font_size, int):
                raise TypeError("Invalid type for `font_size`, type has to be `int`")

        self._font_size = font_size

    @property
    def font_size_expression(self):
        # type: () -> string_types
        """Gets the font_size_expression of this TextFilter.

        An expression for the Font size. Either fontSize or fontSizeExpression can be set at the same time. The following variables are valid: main_h, h, H for input height and main_w, w, W for the input_width

        :return: The font_size_expression of this TextFilter.
        :rtype: string_types
        """
        return self._font_size_expression

    @font_size_expression.setter
    def font_size_expression(self, font_size_expression):
        # type: (string_types) -> None
        """Sets the font_size_expression of this TextFilter.

        An expression for the Font size. Either fontSize or fontSizeExpression can be set at the same time. The following variables are valid: main_h, h, H for input height and main_w, w, W for the input_width

        :param font_size_expression: The font_size_expression of this TextFilter.
        :type: string_types
        """

        if font_size_expression is not None:
            if not isinstance(font_size_expression, string_types):
                raise TypeError("Invalid type for `font_size_expression`, type has to be `string_types`")

        self._font_size_expression = font_size_expression

    @property
    def alpha(self):
        # type: () -> float
        """Gets the alpha of this TextFilter.

        If set, alpha blending for the text is applied. Values are valid between 0.0 and 1.0.

        :return: The alpha of this TextFilter.
        :rtype: float
        """
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        # type: (float) -> None
        """Sets the alpha of this TextFilter.

        If set, alpha blending for the text is applied. Values are valid between 0.0 and 1.0.

        :param alpha: The alpha of this TextFilter.
        :type: float
        """

        if alpha is not None:
            if not isinstance(alpha, (float, int)):
                raise TypeError("Invalid type for `alpha`, type has to be `float`")

        self._alpha = alpha

    @property
    def shadow_color(self):
        # type: () -> string_types
        """Gets the shadow_color of this TextFilter.

        Color of the shadow

        :return: The shadow_color of this TextFilter.
        :rtype: string_types
        """
        return self._shadow_color

    @shadow_color.setter
    def shadow_color(self, shadow_color):
        # type: (string_types) -> None
        """Sets the shadow_color of this TextFilter.

        Color of the shadow

        :param shadow_color: The shadow_color of this TextFilter.
        :type: string_types
        """

        if shadow_color is not None:
            if not isinstance(shadow_color, string_types):
                raise TypeError("Invalid type for `shadow_color`, type has to be `string_types`")

        self._shadow_color = shadow_color

    @property
    def shadow_x(self):
        # type: () -> int
        """Gets the shadow_x of this TextFilter.

        X offset of the shadow

        :return: The shadow_x of this TextFilter.
        :rtype: int
        """
        return self._shadow_x

    @shadow_x.setter
    def shadow_x(self, shadow_x):
        # type: (int) -> None
        """Sets the shadow_x of this TextFilter.

        X offset of the shadow

        :param shadow_x: The shadow_x of this TextFilter.
        :type: int
        """

        if shadow_x is not None:
            if not isinstance(shadow_x, int):
                raise TypeError("Invalid type for `shadow_x`, type has to be `int`")

        self._shadow_x = shadow_x

    @property
    def shadow_y(self):
        # type: () -> int
        """Gets the shadow_y of this TextFilter.

        Y offset of the shadow

        :return: The shadow_y of this TextFilter.
        :rtype: int
        """
        return self._shadow_y

    @shadow_y.setter
    def shadow_y(self, shadow_y):
        # type: (int) -> None
        """Sets the shadow_y of this TextFilter.

        Y offset of the shadow

        :param shadow_y: The shadow_y of this TextFilter.
        :type: int
        """

        if shadow_y is not None:
            if not isinstance(shadow_y, int):
                raise TypeError("Invalid type for `shadow_y`, type has to be `int`")

        self._shadow_y = shadow_y

    @property
    def timecode(self):
        # type: () -> string_types
        """Gets the timecode of this TextFilter.

        If set, the timecode representation in \"hh:mm:ss[:;.]ff\" format will be applied

        :return: The timecode of this TextFilter.
        :rtype: string_types
        """
        return self._timecode

    @timecode.setter
    def timecode(self, timecode):
        # type: (string_types) -> None
        """Sets the timecode of this TextFilter.

        If set, the timecode representation in \"hh:mm:ss[:;.]ff\" format will be applied

        :param timecode: The timecode of this TextFilter.
        :type: string_types
        """

        if timecode is not None:
            if not isinstance(timecode, string_types):
                raise TypeError("Invalid type for `timecode`, type has to be `string_types`")

        self._timecode = timecode

    @property
    def text(self):
        # type: () -> string_types
        """Gets the text of this TextFilter.

        String to be drawn

        :return: The text of this TextFilter.
        :rtype: string_types
        """
        return self._text

    @text.setter
    def text(self, text):
        # type: (string_types) -> None
        """Sets the text of this TextFilter.

        String to be drawn

        :param text: The text of this TextFilter.
        :type: string_types
        """

        if text is not None:
            if not isinstance(text, string_types):
                raise TypeError("Invalid type for `text`, type has to be `string_types`")

        self._text = text

    @property
    def x(self):
        # type: () -> string_types
        """Gets the x of this TextFilter.

        X position of the text. Also an expression can be used. The following variables are valid: line_h - height of each text line; main_h - input height; main_w - input width; n - number of input frame; text_h - Text height; text_w - Text width (required)

        :return: The x of this TextFilter.
        :rtype: string_types
        """
        return self._x

    @x.setter
    def x(self, x):
        # type: (string_types) -> None
        """Sets the x of this TextFilter.

        X position of the text. Also an expression can be used. The following variables are valid: line_h - height of each text line; main_h - input height; main_w - input width; n - number of input frame; text_h - Text height; text_w - Text width (required)

        :param x: The x of this TextFilter.
        :type: string_types
        """

        if x is not None:
            if not isinstance(x, string_types):
                raise TypeError("Invalid type for `x`, type has to be `string_types`")

        self._x = x

    @property
    def y(self):
        # type: () -> string_types
        """Gets the y of this TextFilter.

        Y position of the text. Also an expression can be used. The following variables are valid: line_h - height of each text line; main_h - input height; main_w - input width; n - number of input frame; text_h - Text height; text_w - Text width (required)

        :return: The y of this TextFilter.
        :rtype: string_types
        """
        return self._y

    @y.setter
    def y(self, y):
        # type: (string_types) -> None
        """Sets the y of this TextFilter.

        Y position of the text. Also an expression can be used. The following variables are valid: line_h - height of each text line; main_h - input height; main_w - input width; n - number of input frame; text_h - Text height; text_w - Text width (required)

        :param y: The y of this TextFilter.
        :type: string_types
        """

        if y is not None:
            if not isinstance(y, string_types):
                raise TypeError("Invalid type for `y`, type has to be `string_types`")

        self._y = y

    @property
    def rate(self):
        # type: () -> string_types
        """Gets the rate of this TextFilter.


        :return: The rate of this TextFilter.
        :rtype: string_types
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        # type: (string_types) -> None
        """Sets the rate of this TextFilter.


        :param rate: The rate of this TextFilter.
        :type: string_types
        """

        if rate is not None:
            if not isinstance(rate, string_types):
                raise TypeError("Invalid type for `rate`, type has to be `string_types`")

        self._rate = rate

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(TextFilter, self), "to_dict"):
            result = super(TextFilter, self).to_dict()
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
        if not isinstance(other, TextFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
