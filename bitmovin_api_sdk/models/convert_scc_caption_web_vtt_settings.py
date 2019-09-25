# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.convert_scc_position_mode import ConvertSccPositionMode
import pprint
import six


class ConvertSccCaptionWebVttSettings(object):
    @poscheck_model
    def __init__(self,
                 position_mode=None,
                 remove_flash=None,
                 remove_color=None):
        # type: (ConvertSccPositionMode, bool, bool) -> None

        self._position_mode = None
        self._remove_flash = None
        self._remove_color = None
        self.discriminator = None

        if position_mode is not None:
            self.position_mode = position_mode
        if remove_flash is not None:
            self.remove_flash = remove_flash
        if remove_color is not None:
            self.remove_color = remove_color

    @property
    def openapi_types(self):
        types = {
            'position_mode': 'ConvertSccPositionMode',
            'remove_flash': 'bool',
            'remove_color': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'position_mode': 'positionMode',
            'remove_flash': 'removeFlash',
            'remove_color': 'removeColor'
        }
        return attributes

    @property
    def position_mode(self):
        # type: () -> ConvertSccPositionMode
        """Gets the position_mode of this ConvertSccCaptionWebVttSettings.


        :return: The position_mode of this ConvertSccCaptionWebVttSettings.
        :rtype: ConvertSccPositionMode
        """
        return self._position_mode

    @position_mode.setter
    def position_mode(self, position_mode):
        # type: (ConvertSccPositionMode) -> None
        """Sets the position_mode of this ConvertSccCaptionWebVttSettings.


        :param position_mode: The position_mode of this ConvertSccCaptionWebVttSettings.
        :type: ConvertSccPositionMode
        """

        if position_mode is not None:
            if not isinstance(position_mode, ConvertSccPositionMode):
                raise TypeError("Invalid type for `position_mode`, type has to be `ConvertSccPositionMode`")

        self._position_mode = position_mode

    @property
    def remove_flash(self):
        # type: () -> bool
        """Gets the remove_flash of this ConvertSccCaptionWebVttSettings.

        Remove flash (blinking) information when converting SCC to WebVTT

        :return: The remove_flash of this ConvertSccCaptionWebVttSettings.
        :rtype: bool
        """
        return self._remove_flash

    @remove_flash.setter
    def remove_flash(self, remove_flash):
        # type: (bool) -> None
        """Sets the remove_flash of this ConvertSccCaptionWebVttSettings.

        Remove flash (blinking) information when converting SCC to WebVTT

        :param remove_flash: The remove_flash of this ConvertSccCaptionWebVttSettings.
        :type: bool
        """

        if remove_flash is not None:
            if not isinstance(remove_flash, bool):
                raise TypeError("Invalid type for `remove_flash`, type has to be `bool`")

        self._remove_flash = remove_flash

    @property
    def remove_color(self):
        # type: () -> bool
        """Gets the remove_color of this ConvertSccCaptionWebVttSettings.

        Remove color information when converting SCC to WebVTT

        :return: The remove_color of this ConvertSccCaptionWebVttSettings.
        :rtype: bool
        """
        return self._remove_color

    @remove_color.setter
    def remove_color(self, remove_color):
        # type: (bool) -> None
        """Sets the remove_color of this ConvertSccCaptionWebVttSettings.

        Remove color information when converting SCC to WebVTT

        :param remove_color: The remove_color of this ConvertSccCaptionWebVttSettings.
        :type: bool
        """

        if remove_color is not None:
            if not isinstance(remove_color, bool):
                raise TypeError("Invalid type for `remove_color`, type has to be `bool`")

        self._remove_color = remove_color

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
        if not isinstance(other, ConvertSccCaptionWebVttSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
