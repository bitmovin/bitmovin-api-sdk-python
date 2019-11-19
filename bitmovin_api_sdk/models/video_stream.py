# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.media_stream import MediaStream
import pprint
import six


class VideoStream(MediaStream):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 position=None,
                 duration=None,
                 codec=None,
                 fps=None,
                 bitrate=None,
                 rate=None,
                 width=None,
                 height=None,
                 par=None,
                 rotation=None):
        # type: (string_types, int, float, string_types, string_types, string_types, int, int, int, float, int) -> None
        super(VideoStream, self).__init__(id_=id_, position=position, duration=duration, codec=codec)

        self._fps = None
        self._bitrate = None
        self._rate = None
        self._width = None
        self._height = None
        self._par = None
        self._rotation = None
        self.discriminator = None

        if fps is not None:
            self.fps = fps
        if bitrate is not None:
            self.bitrate = bitrate
        if rate is not None:
            self.rate = rate
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if par is not None:
            self.par = par
        if rotation is not None:
            self.rotation = rotation

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(VideoStream, self), 'openapi_types'):
            types = getattr(super(VideoStream, self), 'openapi_types')

        types.update({
            'fps': 'string_types',
            'bitrate': 'string_types',
            'rate': 'int',
            'width': 'int',
            'height': 'int',
            'par': 'float',
            'rotation': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(VideoStream, self), 'attribute_map'):
            attributes = getattr(super(VideoStream, self), 'attribute_map')

        attributes.update({
            'fps': 'fps',
            'bitrate': 'bitrate',
            'rate': 'rate',
            'width': 'width',
            'height': 'height',
            'par': 'par',
            'rotation': 'rotation'
        })
        return attributes

    @property
    def fps(self):
        # type: () -> string_types
        """Gets the fps of this VideoStream.

        Frame rate of the video

        :return: The fps of this VideoStream.
        :rtype: string_types
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        # type: (string_types) -> None
        """Sets the fps of this VideoStream.

        Frame rate of the video

        :param fps: The fps of this VideoStream.
        :type: string_types
        """

        if fps is not None:
            if not isinstance(fps, string_types):
                raise TypeError("Invalid type for `fps`, type has to be `string_types`")

        self._fps = fps

    @property
    def bitrate(self):
        # type: () -> string_types
        """Gets the bitrate of this VideoStream.

        Bitrate in bps

        :return: The bitrate of this VideoStream.
        :rtype: string_types
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        # type: (string_types) -> None
        """Sets the bitrate of this VideoStream.

        Bitrate in bps

        :param bitrate: The bitrate of this VideoStream.
        :type: string_types
        """

        if bitrate is not None:
            if not isinstance(bitrate, string_types):
                raise TypeError("Invalid type for `bitrate`, type has to be `string_types`")

        self._bitrate = bitrate

    @property
    def rate(self):
        # type: () -> int
        """Gets the rate of this VideoStream.

        Bitrate in bps (the same as bitrate, but represented as an integer value)

        :return: The rate of this VideoStream.
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        # type: (int) -> None
        """Sets the rate of this VideoStream.

        Bitrate in bps (the same as bitrate, but represented as an integer value)

        :param rate: The rate of this VideoStream.
        :type: int
        """

        if rate is not None:
            if not isinstance(rate, int):
                raise TypeError("Invalid type for `rate`, type has to be `int`")

        self._rate = rate

    @property
    def width(self):
        # type: () -> int
        """Gets the width of this VideoStream.

        Width of the video (required)

        :return: The width of this VideoStream.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        # type: (int) -> None
        """Sets the width of this VideoStream.

        Width of the video (required)

        :param width: The width of this VideoStream.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

        self._width = width

    @property
    def height(self):
        # type: () -> int
        """Gets the height of this VideoStream.

        Height of the video (required)

        :return: The height of this VideoStream.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        # type: (int) -> None
        """Sets the height of this VideoStream.

        Height of the video (required)

        :param height: The height of this VideoStream.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

        self._height = height

    @property
    def par(self):
        # type: () -> float
        """Gets the par of this VideoStream.

        Pixel aspect ratio of the video. Default is 1.0

        :return: The par of this VideoStream.
        :rtype: float
        """
        return self._par

    @par.setter
    def par(self, par):
        # type: (float) -> None
        """Sets the par of this VideoStream.

        Pixel aspect ratio of the video. Default is 1.0

        :param par: The par of this VideoStream.
        :type: float
        """

        if par is not None:
            if not isinstance(par, (float, int)):
                raise TypeError("Invalid type for `par`, type has to be `float`")

        self._par = par

    @property
    def rotation(self):
        # type: () -> int
        """Gets the rotation of this VideoStream.

        Rotation of the video for mobile devices. Default is 0.

        :return: The rotation of this VideoStream.
        :rtype: int
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        # type: (int) -> None
        """Sets the rotation of this VideoStream.

        Rotation of the video for mobile devices. Default is 0.

        :param rotation: The rotation of this VideoStream.
        :type: int
        """

        if rotation is not None:
            if not isinstance(rotation, int):
                raise TypeError("Invalid type for `rotation`, type has to be `int`")

        self._rotation = rotation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(VideoStream, self), "to_dict"):
            result = super(VideoStream, self).to_dict()
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
        if not isinstance(other, VideoStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
