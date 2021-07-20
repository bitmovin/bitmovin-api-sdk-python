# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.color_config import ColorConfig
from bitmovin_api_sdk.models.display_aspect_ratio import DisplayAspectRatio
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.h262_interlace_mode import H262InterlaceMode
from bitmovin_api_sdk.models.h262_preset_configuration import H262PresetConfiguration
from bitmovin_api_sdk.models.level_h262 import LevelH262
from bitmovin_api_sdk.models.pixel_format import PixelFormat
from bitmovin_api_sdk.models.profile_h262 import ProfileH262
from bitmovin_api_sdk.models.video_configuration import VideoConfiguration
import pprint
import six


class H262VideoConfiguration(VideoConfiguration):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 width=None,
                 height=None,
                 bitrate=None,
                 rate=None,
                 pixel_format=None,
                 color_config=None,
                 sample_aspect_ratio_numerator=None,
                 sample_aspect_ratio_denominator=None,
                 display_aspect_ratio=None,
                 encoding_mode=None,
                 preset_configuration=None,
                 profile=None,
                 bframes=None,
                 max_bitrate=None,
                 min_bitrate=None,
                 bufsize=None,
                 gop_size=None,
                 level=None,
                 interlace_mode=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, int, float, PixelFormat, ColorConfig, int, int, DisplayAspectRatio, EncodingMode, H262PresetConfiguration, ProfileH262, int, int, int, int, int, LevelH262, H262InterlaceMode) -> None
        super(H262VideoConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, width=width, height=height, bitrate=bitrate, rate=rate, pixel_format=pixel_format, color_config=color_config, sample_aspect_ratio_numerator=sample_aspect_ratio_numerator, sample_aspect_ratio_denominator=sample_aspect_ratio_denominator, display_aspect_ratio=display_aspect_ratio, encoding_mode=encoding_mode)

        self._preset_configuration = None
        self._profile = None
        self._bframes = None
        self._max_bitrate = None
        self._min_bitrate = None
        self._bufsize = None
        self._gop_size = None
        self._level = None
        self._interlace_mode = None
        self.discriminator = None

        if preset_configuration is not None:
            self.preset_configuration = preset_configuration
        if profile is not None:
            self.profile = profile
        if bframes is not None:
            self.bframes = bframes
        if max_bitrate is not None:
            self.max_bitrate = max_bitrate
        if min_bitrate is not None:
            self.min_bitrate = min_bitrate
        if bufsize is not None:
            self.bufsize = bufsize
        if gop_size is not None:
            self.gop_size = gop_size
        if level is not None:
            self.level = level
        if interlace_mode is not None:
            self.interlace_mode = interlace_mode

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(H262VideoConfiguration, self), 'openapi_types'):
            types = getattr(super(H262VideoConfiguration, self), 'openapi_types')

        types.update({
            'preset_configuration': 'H262PresetConfiguration',
            'profile': 'ProfileH262',
            'bframes': 'int',
            'max_bitrate': 'int',
            'min_bitrate': 'int',
            'bufsize': 'int',
            'gop_size': 'int',
            'level': 'LevelH262',
            'interlace_mode': 'H262InterlaceMode'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(H262VideoConfiguration, self), 'attribute_map'):
            attributes = getattr(super(H262VideoConfiguration, self), 'attribute_map')

        attributes.update({
            'preset_configuration': 'presetConfiguration',
            'profile': 'profile',
            'bframes': 'bframes',
            'max_bitrate': 'maxBitrate',
            'min_bitrate': 'minBitrate',
            'bufsize': 'bufsize',
            'gop_size': 'gopSize',
            'level': 'level',
            'interlace_mode': 'interlaceMode'
        })
        return attributes

    @property
    def preset_configuration(self):
        # type: () -> H262PresetConfiguration
        """Gets the preset_configuration of this H262VideoConfiguration.

        Use a set of well defined configurations preset to support certain use cases. Can be overwritten with more specific values.

        :return: The preset_configuration of this H262VideoConfiguration.
        :rtype: H262PresetConfiguration
        """
        return self._preset_configuration

    @preset_configuration.setter
    def preset_configuration(self, preset_configuration):
        # type: (H262PresetConfiguration) -> None
        """Sets the preset_configuration of this H262VideoConfiguration.

        Use a set of well defined configurations preset to support certain use cases. Can be overwritten with more specific values.

        :param preset_configuration: The preset_configuration of this H262VideoConfiguration.
        :type: H262PresetConfiguration
        """

        if preset_configuration is not None:
            if not isinstance(preset_configuration, H262PresetConfiguration):
                raise TypeError("Invalid type for `preset_configuration`, type has to be `H262PresetConfiguration`")

        self._preset_configuration = preset_configuration

    @property
    def profile(self):
        # type: () -> ProfileH262
        """Gets the profile of this H262VideoConfiguration.

        When setting a profile, all other settings must not exceed the limits which are defined in the profile. Otherwise, a higher profile may be automatically chosen. (required)

        :return: The profile of this H262VideoConfiguration.
        :rtype: ProfileH262
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        # type: (ProfileH262) -> None
        """Sets the profile of this H262VideoConfiguration.

        When setting a profile, all other settings must not exceed the limits which are defined in the profile. Otherwise, a higher profile may be automatically chosen. (required)

        :param profile: The profile of this H262VideoConfiguration.
        :type: ProfileH262
        """

        if profile is not None:
            if not isinstance(profile, ProfileH262):
                raise TypeError("Invalid type for `profile`, type has to be `ProfileH262`")

        self._profile = profile

    @property
    def bframes(self):
        # type: () -> int
        """Gets the bframes of this H262VideoConfiguration.

        Sets the amount of b frames.

        :return: The bframes of this H262VideoConfiguration.
        :rtype: int
        """
        return self._bframes

    @bframes.setter
    def bframes(self, bframes):
        # type: (int) -> None
        """Sets the bframes of this H262VideoConfiguration.

        Sets the amount of b frames.

        :param bframes: The bframes of this H262VideoConfiguration.
        :type: int
        """

        if bframes is not None:
            if bframes is not None and bframes > 16:
                raise ValueError("Invalid value for `bframes`, must be a value less than or equal to `16`")
            if bframes is not None and bframes < 0:
                raise ValueError("Invalid value for `bframes`, must be a value greater than or equal to `0`")
            if not isinstance(bframes, int):
                raise TypeError("Invalid type for `bframes`, type has to be `int`")

        self._bframes = bframes

    @property
    def max_bitrate(self):
        # type: () -> int
        """Gets the max_bitrate of this H262VideoConfiguration.

        Maximum Bitrate

        :return: The max_bitrate of this H262VideoConfiguration.
        :rtype: int
        """
        return self._max_bitrate

    @max_bitrate.setter
    def max_bitrate(self, max_bitrate):
        # type: (int) -> None
        """Sets the max_bitrate of this H262VideoConfiguration.

        Maximum Bitrate

        :param max_bitrate: The max_bitrate of this H262VideoConfiguration.
        :type: int
        """

        if max_bitrate is not None:
            if not isinstance(max_bitrate, int):
                raise TypeError("Invalid type for `max_bitrate`, type has to be `int`")

        self._max_bitrate = max_bitrate

    @property
    def min_bitrate(self):
        # type: () -> int
        """Gets the min_bitrate of this H262VideoConfiguration.

        Minimum Bitrate

        :return: The min_bitrate of this H262VideoConfiguration.
        :rtype: int
        """
        return self._min_bitrate

    @min_bitrate.setter
    def min_bitrate(self, min_bitrate):
        # type: (int) -> None
        """Sets the min_bitrate of this H262VideoConfiguration.

        Minimum Bitrate

        :param min_bitrate: The min_bitrate of this H262VideoConfiguration.
        :type: int
        """

        if min_bitrate is not None:
            if not isinstance(min_bitrate, int):
                raise TypeError("Invalid type for `min_bitrate`, type has to be `int`")

        self._min_bitrate = min_bitrate

    @property
    def bufsize(self):
        # type: () -> int
        """Gets the bufsize of this H262VideoConfiguration.

        Playback device buffer size

        :return: The bufsize of this H262VideoConfiguration.
        :rtype: int
        """
        return self._bufsize

    @bufsize.setter
    def bufsize(self, bufsize):
        # type: (int) -> None
        """Sets the bufsize of this H262VideoConfiguration.

        Playback device buffer size

        :param bufsize: The bufsize of this H262VideoConfiguration.
        :type: int
        """

        if bufsize is not None:
            if not isinstance(bufsize, int):
                raise TypeError("Invalid type for `bufsize`, type has to be `int`")

        self._bufsize = bufsize

    @property
    def gop_size(self):
        # type: () -> int
        """Gets the gop_size of this H262VideoConfiguration.

        Minimum GOP length, the minimum distance between I-frames

        :return: The gop_size of this H262VideoConfiguration.
        :rtype: int
        """
        return self._gop_size

    @gop_size.setter
    def gop_size(self, gop_size):
        # type: (int) -> None
        """Sets the gop_size of this H262VideoConfiguration.

        Minimum GOP length, the minimum distance between I-frames

        :param gop_size: The gop_size of this H262VideoConfiguration.
        :type: int
        """

        if gop_size is not None:
            if not isinstance(gop_size, int):
                raise TypeError("Invalid type for `gop_size`, type has to be `int`")

        self._gop_size = gop_size

    @property
    def level(self):
        # type: () -> LevelH262
        """Gets the level of this H262VideoConfiguration.

        Specified set of constraints that indicate a degree of required decoder performance for a profile

        :return: The level of this H262VideoConfiguration.
        :rtype: LevelH262
        """
        return self._level

    @level.setter
    def level(self, level):
        # type: (LevelH262) -> None
        """Sets the level of this H262VideoConfiguration.

        Specified set of constraints that indicate a degree of required decoder performance for a profile

        :param level: The level of this H262VideoConfiguration.
        :type: LevelH262
        """

        if level is not None:
            if not isinstance(level, LevelH262):
                raise TypeError("Invalid type for `level`, type has to be `LevelH262`")

        self._level = level

    @property
    def interlace_mode(self):
        # type: () -> H262InterlaceMode
        """Gets the interlace_mode of this H262VideoConfiguration.

        Using TOP_FIELD_FIRST or BOTTOM_FIELD_FIRST will output interlaced video

        :return: The interlace_mode of this H262VideoConfiguration.
        :rtype: H262InterlaceMode
        """
        return self._interlace_mode

    @interlace_mode.setter
    def interlace_mode(self, interlace_mode):
        # type: (H262InterlaceMode) -> None
        """Sets the interlace_mode of this H262VideoConfiguration.

        Using TOP_FIELD_FIRST or BOTTOM_FIELD_FIRST will output interlaced video

        :param interlace_mode: The interlace_mode of this H262VideoConfiguration.
        :type: H262InterlaceMode
        """

        if interlace_mode is not None:
            if not isinstance(interlace_mode, H262InterlaceMode):
                raise TypeError("Invalid type for `interlace_mode`, type has to be `H262InterlaceMode`")

        self._interlace_mode = interlace_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(H262VideoConfiguration, self), "to_dict"):
            result = super(H262VideoConfiguration, self).to_dict()
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
        if not isinstance(other, H262VideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
