# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.thumbnail_unit import ThumbnailUnit
import pprint
import six


class Thumbnail(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 height=None,
                 width=None,
                 pattern=None,
                 interval=None,
                 positions=None,
                 outputs=None,
                 unit=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, string_types, float, list[float], list[EncodingOutput], ThumbnailUnit) -> None
        super(Thumbnail, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._height = None
        self._width = None
        self._pattern = None
        self._interval = None
        self._positions = list()
        self._outputs = list()
        self._unit = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if pattern is not None:
            self.pattern = pattern
        if interval is not None:
            self.interval = interval
        if positions is not None:
            self.positions = positions
        if outputs is not None:
            self.outputs = outputs
        if unit is not None:
            self.unit = unit

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Thumbnail, self), 'openapi_types'):
            types = getattr(super(Thumbnail, self), 'openapi_types')

        types.update({
            'height': 'int',
            'width': 'int',
            'pattern': 'string_types',
            'interval': 'float',
            'positions': 'list[float]',
            'outputs': 'list[EncodingOutput]',
            'unit': 'ThumbnailUnit'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Thumbnail, self), 'attribute_map'):
            attributes = getattr(super(Thumbnail, self), 'attribute_map')

        attributes.update({
            'height': 'height',
            'width': 'width',
            'pattern': 'pattern',
            'interval': 'interval',
            'positions': 'positions',
            'outputs': 'outputs',
            'unit': 'unit'
        })
        return attributes

    @property
    def height(self):
        # type: () -> int
        """Gets the height of this Thumbnail.

        Height of the thumbnail, either height or width are required fields. If only one is given the encoder will calculate the other way value based on the aspect ratio of the video file. If the encoder version is below 2.83.0 only height is supported and mandatory. 

        :return: The height of this Thumbnail.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        # type: (int) -> None
        """Sets the height of this Thumbnail.

        Height of the thumbnail, either height or width are required fields. If only one is given the encoder will calculate the other way value based on the aspect ratio of the video file. If the encoder version is below 2.83.0 only height is supported and mandatory. 

        :param height: The height of this Thumbnail.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

        self._height = height

    @property
    def width(self):
        # type: () -> int
        """Gets the width of this Thumbnail.

        Width of the thumbnail, either height or width are required fields. If only one is given the encoder will calculate the other way value based on the aspect ratio of the video file. If the encoder version is below 2.83.0 only height is supported 

        :return: The width of this Thumbnail.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        # type: (int) -> None
        """Sets the width of this Thumbnail.

        Width of the thumbnail, either height or width are required fields. If only one is given the encoder will calculate the other way value based on the aspect ratio of the video file. If the encoder version is below 2.83.0 only height is supported 

        :param width: The width of this Thumbnail.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

        self._width = width

    @property
    def pattern(self):
        # type: () -> string_types
        """Gets the pattern of this Thumbnail.

         Pattern which describes the thumbnail filenames. For example with thumbnail-%number%.png as pattern and 3 positions: thumbnail-3_0.png, thumbnail-5_0.png and thumbnail-25_5.png. (The number represents the position in the source video in seconds, in the previous example the first filename represents the thumbnail at 3s, the second one at 5s and the third one at 25.5s). (required)

        :return: The pattern of this Thumbnail.
        :rtype: string_types
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        # type: (string_types) -> None
        """Sets the pattern of this Thumbnail.

         Pattern which describes the thumbnail filenames. For example with thumbnail-%number%.png as pattern and 3 positions: thumbnail-3_0.png, thumbnail-5_0.png and thumbnail-25_5.png. (The number represents the position in the source video in seconds, in the previous example the first filename represents the thumbnail at 3s, the second one at 5s and the third one at 25.5s). (required)

        :param pattern: The pattern of this Thumbnail.
        :type: string_types
        """

        if pattern is not None:
            if not isinstance(pattern, string_types):
                raise TypeError("Invalid type for `pattern`, type has to be `string_types`")

        self._pattern = pattern

    @property
    def interval(self):
        # type: () -> float
        """Gets the interval of this Thumbnail.

        The interval in which to create thumbnails. In seconds (E.g. a value of 4 means create a thumbnail every 4 seconds). Mutually exclusive with positions/unit. Has to be equal to or greater than 1.

        :return: The interval of this Thumbnail.
        :rtype: float
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        # type: (float) -> None
        """Sets the interval of this Thumbnail.

        The interval in which to create thumbnails. In seconds (E.g. a value of 4 means create a thumbnail every 4 seconds). Mutually exclusive with positions/unit. Has to be equal to or greater than 1.

        :param interval: The interval of this Thumbnail.
        :type: float
        """

        if interval is not None:
            if not isinstance(interval, (float, int)):
                raise TypeError("Invalid type for `interval`, type has to be `float`")

        self._interval = interval

    @property
    def positions(self):
        # type: () -> list[float]
        """Gets the positions of this Thumbnail.

        Position in the unit where the thumbnail should be created from. Mutually exclusive with interval.

        :return: The positions of this Thumbnail.
        :rtype: list[float]
        """
        return self._positions

    @positions.setter
    def positions(self, positions):
        # type: (list) -> None
        """Sets the positions of this Thumbnail.

        Position in the unit where the thumbnail should be created from. Mutually exclusive with interval.

        :param positions: The positions of this Thumbnail.
        :type: list[float]
        """

        if positions is not None:
            if not isinstance(positions, list):
                raise TypeError("Invalid type for `positions`, type has to be `list[float]`")

        self._positions = positions

    @property
    def outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the outputs of this Thumbnail.


        :return: The outputs of this Thumbnail.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this Thumbnail.


        :param outputs: The outputs of this Thumbnail.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

    @property
    def unit(self):
        # type: () -> ThumbnailUnit
        """Gets the unit of this Thumbnail.

        Unit of the values in the positions array.

        :return: The unit of this Thumbnail.
        :rtype: ThumbnailUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        # type: (ThumbnailUnit) -> None
        """Sets the unit of this Thumbnail.

        Unit of the values in the positions array.

        :param unit: The unit of this Thumbnail.
        :type: ThumbnailUnit
        """

        if unit is not None:
            if not isinstance(unit, ThumbnailUnit):
                raise TypeError("Invalid type for `unit`, type has to be `ThumbnailUnit`")

        self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Thumbnail, self), "to_dict"):
            result = super(Thumbnail, self).to_dict()
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
        if not isinstance(other, Thumbnail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
