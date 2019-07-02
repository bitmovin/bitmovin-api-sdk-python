# coding: utf-8

from bitmovin.models.bitmovin_resource import BitmovinResource
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class Bif(BitmovinResource):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(Bif, self).openapi_types
        types.update({
            'height': 'int',
            'width': 'int',
            'distance': 'float',
            'filename': 'str',
            'outputs': 'list[EncodingOutput]'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(Bif, self).attribute_map
        attributes.update({
            'height': 'height',
            'width': 'width',
            'distance': 'distance',
            'filename': 'filename',
            'outputs': 'outputs'
        })
        return attributes

    def __init__(self, height=None, width=None, distance=None, filename=None, outputs=None, *args, **kwargs):
        super(Bif, self).__init__(*args, **kwargs)

        self._height = None
        self._width = None
        self._distance = None
        self._filename = None
        self._outputs = list()
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

    @property
    def height(self):
        """Gets the height of this Bif.

        Height of one thumbnail

        :return: The height of this Bif.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
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
        """Gets the width of this Bif.

        Width of one thumbnail. Roku recommends a width of 240 for SD and 320 for HD.

        :return: The width of this Bif.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
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
        """Gets the distance of this Bif.

        Distance in seconds between a screenshot

        :return: The distance of this Bif.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this Bif.

        Distance in seconds between a screenshot

        :param distance: The distance of this Bif.
        :type: float
        """

        if distance is not None:
            if not isinstance(distance, (float, int)):
                raise TypeError("Invalid type for `distance`, type has to be `float`")

        self._distance = distance


    @property
    def filename(self):
        """Gets the filename of this Bif.

        Filename of the Bif image. (required)

        :return: The filename of this Bif.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Bif.

        Filename of the Bif image. (required)

        :param filename: The filename of this Bif.
        :type: str
        """

        if filename is not None:
            if not isinstance(filename, str):
                raise TypeError("Invalid type for `filename`, type has to be `str`")

        self._filename = filename


    @property
    def outputs(self):
        """Gets the outputs of this Bif.


        :return: The outputs of this Bif.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this Bif.


        :param outputs: The outputs of this Bif.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(Bif, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(Bif, dict):
                for key, value in self.items():
                    result[key] = value

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
