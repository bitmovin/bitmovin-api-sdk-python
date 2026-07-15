# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.auto_level_setup import AutoLevelSetup
from bitmovin_api_sdk.models.av1_preset_configuration import Av1PresetConfiguration
from bitmovin_api_sdk.models.color_config import ColorConfig
from bitmovin_api_sdk.models.display_aspect_ratio import DisplayAspectRatio
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.pixel_format import PixelFormat
from bitmovin_api_sdk.models.video_configuration import VideoConfiguration
import pprint
import six


class Av1VideoConfiguration(VideoConfiguration):
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
                 auto_level_setup=None,
                 master_display=None,
                 max_content_light_level=None,
                 max_picture_average_light_level=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, int, float, PixelFormat, ColorConfig, int, int, DisplayAspectRatio, EncodingMode, Av1PresetConfiguration, AutoLevelSetup, string_types, int, int) -> None
        super(Av1VideoConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, width=width, height=height, bitrate=bitrate, rate=rate, pixel_format=pixel_format, color_config=color_config, sample_aspect_ratio_numerator=sample_aspect_ratio_numerator, sample_aspect_ratio_denominator=sample_aspect_ratio_denominator, display_aspect_ratio=display_aspect_ratio, encoding_mode=encoding_mode)

        self._preset_configuration = None
        self._auto_level_setup = None
        self._master_display = None
        self._max_content_light_level = None
        self._max_picture_average_light_level = None
        self.discriminator = None

        if preset_configuration is not None:
            self.preset_configuration = preset_configuration
        if auto_level_setup is not None:
            self.auto_level_setup = auto_level_setup
        if master_display is not None:
            self.master_display = master_display
        if max_content_light_level is not None:
            self.max_content_light_level = max_content_light_level
        if max_picture_average_light_level is not None:
            self.max_picture_average_light_level = max_picture_average_light_level

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Av1VideoConfiguration, self), 'openapi_types'):
            types = getattr(super(Av1VideoConfiguration, self), 'openapi_types')

        types.update({
            'preset_configuration': 'Av1PresetConfiguration',
            'auto_level_setup': 'AutoLevelSetup',
            'master_display': 'string_types',
            'max_content_light_level': 'int',
            'max_picture_average_light_level': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Av1VideoConfiguration, self), 'attribute_map'):
            attributes = getattr(super(Av1VideoConfiguration, self), 'attribute_map')

        attributes.update({
            'preset_configuration': 'presetConfiguration',
            'auto_level_setup': 'autoLevelSetup',
            'master_display': 'masterDisplay',
            'max_content_light_level': 'maxContentLightLevel',
            'max_picture_average_light_level': 'maxPictureAverageLightLevel'
        })
        return attributes

    @property
    def preset_configuration(self):
        # type: () -> Av1PresetConfiguration
        """Gets the preset_configuration of this Av1VideoConfiguration.

        Use a set of well defined configurations preset to support certain use cases. Can be overwritten with more specific values.

        :return: The preset_configuration of this Av1VideoConfiguration.
        :rtype: Av1PresetConfiguration
        """
        return self._preset_configuration

    @preset_configuration.setter
    def preset_configuration(self, preset_configuration):
        # type: (Av1PresetConfiguration) -> None
        """Sets the preset_configuration of this Av1VideoConfiguration.

        Use a set of well defined configurations preset to support certain use cases. Can be overwritten with more specific values.

        :param preset_configuration: The preset_configuration of this Av1VideoConfiguration.
        :type: Av1PresetConfiguration
        """

        if preset_configuration is not None:
            if not isinstance(preset_configuration, Av1PresetConfiguration):
                raise TypeError("Invalid type for `preset_configuration`, type has to be `Av1PresetConfiguration`")

        self._preset_configuration = preset_configuration

    @property
    def auto_level_setup(self):
        # type: () -> AutoLevelSetup
        """Gets the auto_level_setup of this Av1VideoConfiguration.

        Enable/disable automatic calculation of level, maxBitrate, and bufsize based on the least level that satisfies maximum property values for picture resolution, frame rate, and bit rate. In the case the target level is set explicitly, the maximum bitrate and buffer size are calculated based on the defined level. Explicitly setting maxBitrate, or bufsize properties will disable the automatic calculation.

        :return: The auto_level_setup of this Av1VideoConfiguration.
        :rtype: AutoLevelSetup
        """
        return self._auto_level_setup

    @auto_level_setup.setter
    def auto_level_setup(self, auto_level_setup):
        # type: (AutoLevelSetup) -> None
        """Sets the auto_level_setup of this Av1VideoConfiguration.

        Enable/disable automatic calculation of level, maxBitrate, and bufsize based on the least level that satisfies maximum property values for picture resolution, frame rate, and bit rate. In the case the target level is set explicitly, the maximum bitrate and buffer size are calculated based on the defined level. Explicitly setting maxBitrate, or bufsize properties will disable the automatic calculation.

        :param auto_level_setup: The auto_level_setup of this Av1VideoConfiguration.
        :type: AutoLevelSetup
        """

        if auto_level_setup is not None:
            if not isinstance(auto_level_setup, AutoLevelSetup):
                raise TypeError("Invalid type for `auto_level_setup`, type has to be `AutoLevelSetup`")

        self._auto_level_setup = auto_level_setup

    @property
    def master_display(self):
        # type: () -> string_types
        """Gets the master_display of this Av1VideoConfiguration.

        Set the mastering display color volume metadata. The chromaticity coordinates for the green (G), blue (B), red (R) primaries and the white point (WP) are given in increments of 0.00002 (i.e. multiply the actual value by 50000), and the luminance values (L) are given in increments of 0.0001 cd/m² (i.e. multiply the actual value by 10000). For example `G(13250,34500)B(7500,3000)R(34000,16000)WP(15635,16450)L(10000000,1)` describes a P3D65 1000-nits monitor, where G(x=0.265, y=0.690), B(x=0.150, y=0.060), R(x=0.680, y=0.320), WP(x=0.3127, y=0.3290), L(max=1000, min=0.0001). Part of HDR-10 metadata.

        :return: The master_display of this Av1VideoConfiguration.
        :rtype: string_types
        """
        return self._master_display

    @master_display.setter
    def master_display(self, master_display):
        # type: (string_types) -> None
        """Sets the master_display of this Av1VideoConfiguration.

        Set the mastering display color volume metadata. The chromaticity coordinates for the green (G), blue (B), red (R) primaries and the white point (WP) are given in increments of 0.00002 (i.e. multiply the actual value by 50000), and the luminance values (L) are given in increments of 0.0001 cd/m² (i.e. multiply the actual value by 10000). For example `G(13250,34500)B(7500,3000)R(34000,16000)WP(15635,16450)L(10000000,1)` describes a P3D65 1000-nits monitor, where G(x=0.265, y=0.690), B(x=0.150, y=0.060), R(x=0.680, y=0.320), WP(x=0.3127, y=0.3290), L(max=1000, min=0.0001). Part of HDR-10 metadata.

        :param master_display: The master_display of this Av1VideoConfiguration.
        :type: string_types
        """

        if master_display is not None:
            if not isinstance(master_display, string_types):
                raise TypeError("Invalid type for `master_display`, type has to be `string_types`")

        self._master_display = master_display

    @property
    def max_content_light_level(self):
        # type: () -> int
        """Gets the max_content_light_level of this Av1VideoConfiguration.

        Set the max content light level (MaxCLL). Use together with maxPictureAverageLightLevel (which will be 0 if not set). Part of HDR-10 metadata.

        :return: The max_content_light_level of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._max_content_light_level

    @max_content_light_level.setter
    def max_content_light_level(self, max_content_light_level):
        # type: (int) -> None
        """Sets the max_content_light_level of this Av1VideoConfiguration.

        Set the max content light level (MaxCLL). Use together with maxPictureAverageLightLevel (which will be 0 if not set). Part of HDR-10 metadata.

        :param max_content_light_level: The max_content_light_level of this Av1VideoConfiguration.
        :type: int
        """

        if max_content_light_level is not None:
            if max_content_light_level is not None and max_content_light_level > 65535:
                raise ValueError("Invalid value for `max_content_light_level`, must be a value less than or equal to `65535`")
            if max_content_light_level is not None and max_content_light_level < 0:
                raise ValueError("Invalid value for `max_content_light_level`, must be a value greater than or equal to `0`")
            if not isinstance(max_content_light_level, int):
                raise TypeError("Invalid type for `max_content_light_level`, type has to be `int`")

        self._max_content_light_level = max_content_light_level

    @property
    def max_picture_average_light_level(self):
        # type: () -> int
        """Gets the max_picture_average_light_level of this Av1VideoConfiguration.

        Set the maximum picture average light level (MaxFALL). Use together with maxContentLightLevel (which will be 0 if not set). Part of HDR-10 metadata.

        :return: The max_picture_average_light_level of this Av1VideoConfiguration.
        :rtype: int
        """
        return self._max_picture_average_light_level

    @max_picture_average_light_level.setter
    def max_picture_average_light_level(self, max_picture_average_light_level):
        # type: (int) -> None
        """Sets the max_picture_average_light_level of this Av1VideoConfiguration.

        Set the maximum picture average light level (MaxFALL). Use together with maxContentLightLevel (which will be 0 if not set). Part of HDR-10 metadata.

        :param max_picture_average_light_level: The max_picture_average_light_level of this Av1VideoConfiguration.
        :type: int
        """

        if max_picture_average_light_level is not None:
            if max_picture_average_light_level is not None and max_picture_average_light_level > 65535:
                raise ValueError("Invalid value for `max_picture_average_light_level`, must be a value less than or equal to `65535`")
            if max_picture_average_light_level is not None and max_picture_average_light_level < 0:
                raise ValueError("Invalid value for `max_picture_average_light_level`, must be a value greater than or equal to `0`")
            if not isinstance(max_picture_average_light_level, int):
                raise TypeError("Invalid type for `max_picture_average_light_level`, type has to be `int`")

        self._max_picture_average_light_level = max_picture_average_light_level

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Av1VideoConfiguration, self), "to_dict"):
            result = super(Av1VideoConfiguration, self).to_dict()
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
        if not isinstance(other, Av1VideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
