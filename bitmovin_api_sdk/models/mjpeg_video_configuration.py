# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.codec_configuration import CodecConfiguration
from bitmovin_api_sdk.models.pixel_format import PixelFormat
import pprint
import six


class MjpegVideoConfiguration(CodecConfiguration):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 width=None,
                 height=None,
                 rate=None,
                 q_scale=None,
                 pixel_format=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, int, int, float, int, PixelFormat) -> None
        super(MjpegVideoConfiguration, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_)

        self._width = None
        self._height = None
        self._rate = None
        self._q_scale = None
        self._pixel_format = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if rate is not None:
            self.rate = rate
        if q_scale is not None:
            self.q_scale = q_scale
        if pixel_format is not None:
            self.pixel_format = pixel_format

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(MjpegVideoConfiguration, self), 'openapi_types'):
            types = getattr(super(MjpegVideoConfiguration, self), 'openapi_types')

        types.update({
            'width': 'int',
            'height': 'int',
            'rate': 'float',
            'q_scale': 'int',
            'pixel_format': 'PixelFormat'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(MjpegVideoConfiguration, self), 'attribute_map'):
            attributes = getattr(super(MjpegVideoConfiguration, self), 'attribute_map')

        attributes.update({
            'width': 'width',
            'height': 'height',
            'rate': 'rate',
            'q_scale': 'qScale',
            'pixel_format': 'pixelFormat'
        })
        return attributes

    @property
    def width(self):
        # type: () -> int
        """Gets the width of this MjpegVideoConfiguration.

        Width of the encoded video

        :return: The width of this MjpegVideoConfiguration.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        # type: (int) -> None
        """Sets the width of this MjpegVideoConfiguration.

        Width of the encoded video

        :param width: The width of this MjpegVideoConfiguration.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

        self._width = width

    @property
    def height(self):
        # type: () -> int
        """Gets the height of this MjpegVideoConfiguration.

        Height of the encoded video

        :return: The height of this MjpegVideoConfiguration.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        # type: (int) -> None
        """Sets the height of this MjpegVideoConfiguration.

        Height of the encoded video

        :param height: The height of this MjpegVideoConfiguration.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

        self._height = height

    @property
    def rate(self):
        # type: () -> float
        """Gets the rate of this MjpegVideoConfiguration.

        Target frame rate of the encoded video! (required)

        :return: The rate of this MjpegVideoConfiguration.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        # type: (float) -> None
        """Sets the rate of this MjpegVideoConfiguration.

        Target frame rate of the encoded video! (required)

        :param rate: The rate of this MjpegVideoConfiguration.
        :type: float
        """

        if rate is not None:
            if not isinstance(rate, (float, int)):
                raise TypeError("Invalid type for `rate`, type has to be `float`")

        self._rate = rate

    @property
    def q_scale(self):
        # type: () -> int
        """Gets the q_scale of this MjpegVideoConfiguration.

        The quality scale parameter (required)

        :return: The q_scale of this MjpegVideoConfiguration.
        :rtype: int
        """
        return self._q_scale

    @q_scale.setter
    def q_scale(self, q_scale):
        # type: (int) -> None
        """Sets the q_scale of this MjpegVideoConfiguration.

        The quality scale parameter (required)

        :param q_scale: The q_scale of this MjpegVideoConfiguration.
        :type: int
        """

        if q_scale is not None:
            if not isinstance(q_scale, int):
                raise TypeError("Invalid type for `q_scale`, type has to be `int`")

        self._q_scale = q_scale

    @property
    def pixel_format(self):
        # type: () -> PixelFormat
        """Gets the pixel_format of this MjpegVideoConfiguration.


        :return: The pixel_format of this MjpegVideoConfiguration.
        :rtype: PixelFormat
        """
        return self._pixel_format

    @pixel_format.setter
    def pixel_format(self, pixel_format):
        # type: (PixelFormat) -> None
        """Sets the pixel_format of this MjpegVideoConfiguration.


        :param pixel_format: The pixel_format of this MjpegVideoConfiguration.
        :type: PixelFormat
        """

        if pixel_format is not None:
            if not isinstance(pixel_format, PixelFormat):
                raise TypeError("Invalid type for `pixel_format`, type has to be `PixelFormat`")

        self._pixel_format = pixel_format

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(MjpegVideoConfiguration, self), "to_dict"):
            result = super(MjpegVideoConfiguration, self).to_dict()
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
        if not isinstance(other, MjpegVideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
