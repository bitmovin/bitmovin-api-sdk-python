# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.thumbnail_aspect_mode import ThumbnailAspectMode
import pprint
import six


class Bif(BitmovinResource):
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
                 distance=None,
                 filename=None,
                 outputs=None,
                 aspect_mode=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, float, string_types, list[EncodingOutput], ThumbnailAspectMode) -> None
        super(Bif, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._height = None
        self._width = None
        self._distance = None
        self._filename = None
        self._outputs = list()
        self._aspect_mode = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if distance is not None:
            self.distance = distance
        if filename is not None:
            self.filename = filename
        if outputs is not None:
            self.outputs = outputs
        if aspect_mode is not None:
            self.aspect_mode = aspect_mode

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Bif, self), 'openapi_types'):
            types = getattr(super(Bif, self), 'openapi_types')

        types.update({
            'height': 'int',
            'width': 'int',
            'distance': 'float',
            'filename': 'string_types',
            'outputs': 'list[EncodingOutput]',
            'aspect_mode': 'ThumbnailAspectMode'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Bif, self), 'attribute_map'):
            attributes = getattr(super(Bif, self), 'attribute_map')

        attributes.update({
            'height': 'height',
            'width': 'width',
            'distance': 'distance',
            'filename': 'filename',
            'outputs': 'outputs',
            'aspect_mode': 'aspectMode'
        })
        return attributes

    @property
    def height(self):
        # type: () -> int
        """Gets the height of this Bif.

        Height of one thumbnail

        :return: The height of this Bif.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        # type: (int) -> None
        """Sets the height of this Bif.

        Height of one thumbnail

        :param height: The height of this Bif.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

        self._height = height

    @property
    def width(self):
        # type: () -> int
        """Gets the width of this Bif.

        Width of one thumbnail. Roku recommends a width of 240 for SD and 320 for HD.

        :return: The width of this Bif.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        # type: (int) -> None
        """Sets the width of this Bif.

        Width of one thumbnail. Roku recommends a width of 240 for SD and 320 for HD.

        :param width: The width of this Bif.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

        self._width = width

    @property
    def distance(self):
        # type: () -> float
        """Gets the distance of this Bif.

        Distance in seconds between a screenshot (required)

        :return: The distance of this Bif.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        # type: (float) -> None
        """Sets the distance of this Bif.

        Distance in seconds between a screenshot (required)

        :param distance: The distance of this Bif.
        :type: float
        """

        if distance is not None:
            if distance is not None and distance < 0:
                raise ValueError("Invalid value for `distance`, must be a value greater than or equal to `0`")
            if not isinstance(distance, (float, int)):
                raise TypeError("Invalid type for `distance`, type has to be `float`")

        self._distance = distance

    @property
    def filename(self):
        # type: () -> string_types
        """Gets the filename of this Bif.

        Filename of the Bif image. (required)

        :return: The filename of this Bif.
        :rtype: string_types
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        # type: (string_types) -> None
        """Sets the filename of this Bif.

        Filename of the Bif image. (required)

        :param filename: The filename of this Bif.
        :type: string_types
        """

        if filename is not None:
            if not isinstance(filename, string_types):
                raise TypeError("Invalid type for `filename`, type has to be `string_types`")

        self._filename = filename

    @property
    def outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the outputs of this Bif.


        :return: The outputs of this Bif.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this Bif.


        :param outputs: The outputs of this Bif.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

    @property
    def aspect_mode(self):
        # type: () -> ThumbnailAspectMode
        """Gets the aspect_mode of this Bif.

        Specifies the aspect mode that is used when both height and width are specified Only supported starting with encoder version `2.85.0`. 

        :return: The aspect_mode of this Bif.
        :rtype: ThumbnailAspectMode
        """
        return self._aspect_mode

    @aspect_mode.setter
    def aspect_mode(self, aspect_mode):
        # type: (ThumbnailAspectMode) -> None
        """Sets the aspect_mode of this Bif.

        Specifies the aspect mode that is used when both height and width are specified Only supported starting with encoder version `2.85.0`. 

        :param aspect_mode: The aspect_mode of this Bif.
        :type: ThumbnailAspectMode
        """

        if aspect_mode is not None:
            if not isinstance(aspect_mode, ThumbnailAspectMode):
                raise TypeError("Invalid type for `aspect_mode`, type has to be `ThumbnailAspectMode`")

        self._aspect_mode = aspect_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Bif, self), "to_dict"):
            result = super(Bif, self).to_dict()
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
        if not isinstance(other, Bif):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
