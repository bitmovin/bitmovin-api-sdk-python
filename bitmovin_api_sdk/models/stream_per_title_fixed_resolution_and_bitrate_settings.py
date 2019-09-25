# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitrate_selection_mode import BitrateSelectionMode
import pprint
import six


class StreamPerTitleFixedResolutionAndBitrateSettings(object):
    @poscheck_model
    def __init__(self,
                 min_bitrate=None,
                 max_bitrate=None,
                 bitrate_selection_mode=None,
                 low_complexity_boundary_for_max_bitrate=None,
                 high_complexity_boundary_for_max_bitrate=None):
        # type: (int, int, BitrateSelectionMode, int, int) -> None

        self._min_bitrate = None
        self._max_bitrate = None
        self._bitrate_selection_mode = None
        self._low_complexity_boundary_for_max_bitrate = None
        self._high_complexity_boundary_for_max_bitrate = None
        self.discriminator = None

        if min_bitrate is not None:
            self.min_bitrate = min_bitrate
        if max_bitrate is not None:
            self.max_bitrate = max_bitrate
        if bitrate_selection_mode is not None:
            self.bitrate_selection_mode = bitrate_selection_mode
        if low_complexity_boundary_for_max_bitrate is not None:
            self.low_complexity_boundary_for_max_bitrate = low_complexity_boundary_for_max_bitrate
        if high_complexity_boundary_for_max_bitrate is not None:
            self.high_complexity_boundary_for_max_bitrate = high_complexity_boundary_for_max_bitrate

    @property
    def openapi_types(self):
        types = {
            'min_bitrate': 'int',
            'max_bitrate': 'int',
            'bitrate_selection_mode': 'BitrateSelectionMode',
            'low_complexity_boundary_for_max_bitrate': 'int',
            'high_complexity_boundary_for_max_bitrate': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'min_bitrate': 'minBitrate',
            'max_bitrate': 'maxBitrate',
            'bitrate_selection_mode': 'bitrateSelectionMode',
            'low_complexity_boundary_for_max_bitrate': 'lowComplexityBoundaryForMaxBitrate',
            'high_complexity_boundary_for_max_bitrate': 'highComplexityBoundaryForMaxBitrate'
        }
        return attributes

    @property
    def min_bitrate(self):
        # type: () -> int
        """Gets the min_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.

        The minimum bitrate that will be used for that template.

        :return: The min_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.
        :rtype: int
        """
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, min_bitrate):
        # type: (int) -> None
        """Sets the min_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.

        The minimum bitrate that will be used for that template.

        :param min_bitrate: The min_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.
        :type: int
        """

        if min_bitrate is not None:
            if not isinstance(min_bitrate, int):
                raise TypeError("Invalid type for `min_bitrate`, type has to be `int`")

        self._min_bitrate = min_bitrate

    @property
    def max_bitrate(self):
        # type: () -> int
        """Gets the max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.

        The maximum bitrate that will be used for that template.

        :return: The max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.
        :rtype: int
        """
        return self._max_bitrate

    @max_bitrate.setter
    def max_bitrate(self, max_bitrate):
        # type: (int) -> None
        """Sets the max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.

        The maximum bitrate that will be used for that template.

        :param max_bitrate: The max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.
        :type: int
        """

        if max_bitrate is not None:
            if not isinstance(max_bitrate, int):
                raise TypeError("Invalid type for `max_bitrate`, type has to be `int`")

        self._max_bitrate = max_bitrate

    @property
    def bitrate_selection_mode(self):
        # type: () -> BitrateSelectionMode
        """Gets the bitrate_selection_mode of this StreamPerTitleFixedResolutionAndBitrateSettings.

        Bitrate selection mode

        :return: The bitrate_selection_mode of this StreamPerTitleFixedResolutionAndBitrateSettings.
        :rtype: BitrateSelectionMode
        """
        return self._bitrate_selection_mode

    @bitrate_selection_mode.setter
    def bitrate_selection_mode(self, bitrate_selection_mode):
        # type: (BitrateSelectionMode) -> None
        """Sets the bitrate_selection_mode of this StreamPerTitleFixedResolutionAndBitrateSettings.

        Bitrate selection mode

        :param bitrate_selection_mode: The bitrate_selection_mode of this StreamPerTitleFixedResolutionAndBitrateSettings.
        :type: BitrateSelectionMode
        """

        if bitrate_selection_mode is not None:
            if not isinstance(bitrate_selection_mode, BitrateSelectionMode):
                raise TypeError("Invalid type for `bitrate_selection_mode`, type has to be `BitrateSelectionMode`")

        self._bitrate_selection_mode = bitrate_selection_mode

    @property
    def low_complexity_boundary_for_max_bitrate(self):
        # type: () -> int
        """Gets the low_complexity_boundary_for_max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.

        Low complexity boundary for max bitrate

        :return: The low_complexity_boundary_for_max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.
        :rtype: int
        """
        return self._low_complexity_boundary_for_max_bitrate

    @low_complexity_boundary_for_max_bitrate.setter
    def low_complexity_boundary_for_max_bitrate(self, low_complexity_boundary_for_max_bitrate):
        # type: (int) -> None
        """Sets the low_complexity_boundary_for_max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.

        Low complexity boundary for max bitrate

        :param low_complexity_boundary_for_max_bitrate: The low_complexity_boundary_for_max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.
        :type: int
        """

        if low_complexity_boundary_for_max_bitrate is not None:
            if not isinstance(low_complexity_boundary_for_max_bitrate, int):
                raise TypeError("Invalid type for `low_complexity_boundary_for_max_bitrate`, type has to be `int`")

        self._low_complexity_boundary_for_max_bitrate = low_complexity_boundary_for_max_bitrate

    @property
    def high_complexity_boundary_for_max_bitrate(self):
        # type: () -> int
        """Gets the high_complexity_boundary_for_max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.

        High complexity boundary for max bitrate

        :return: The high_complexity_boundary_for_max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.
        :rtype: int
        """
        return self._high_complexity_boundary_for_max_bitrate

    @high_complexity_boundary_for_max_bitrate.setter
    def high_complexity_boundary_for_max_bitrate(self, high_complexity_boundary_for_max_bitrate):
        # type: (int) -> None
        """Sets the high_complexity_boundary_for_max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.

        High complexity boundary for max bitrate

        :param high_complexity_boundary_for_max_bitrate: The high_complexity_boundary_for_max_bitrate of this StreamPerTitleFixedResolutionAndBitrateSettings.
        :type: int
        """

        if high_complexity_boundary_for_max_bitrate is not None:
            if not isinstance(high_complexity_boundary_for_max_bitrate, int):
                raise TypeError("Invalid type for `high_complexity_boundary_for_max_bitrate`, type has to be `int`")

        self._high_complexity_boundary_for_max_bitrate = high_complexity_boundary_for_max_bitrate

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
        if not isinstance(other, StreamPerTitleFixedResolutionAndBitrateSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
