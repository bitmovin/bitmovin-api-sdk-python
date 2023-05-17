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
                 auto_level_setup=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, int, float, PixelFormat, ColorConfig, int, int, DisplayAspectRatio, EncodingMode, Av1PresetConfiguration, AutoLevelSetup) -> None
        super(Av1VideoConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, width=width, height=height, bitrate=bitrate, rate=rate, pixel_format=pixel_format, color_config=color_config, sample_aspect_ratio_numerator=sample_aspect_ratio_numerator, sample_aspect_ratio_denominator=sample_aspect_ratio_denominator, display_aspect_ratio=display_aspect_ratio, encoding_mode=encoding_mode)

        self._preset_configuration = None
        self._auto_level_setup = None
        self.discriminator = None

        if preset_configuration is not None:
            self.preset_configuration = preset_configuration
        if auto_level_setup is not None:
            self.auto_level_setup = auto_level_setup

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Av1VideoConfiguration, self), 'openapi_types'):
            types = getattr(super(Av1VideoConfiguration, self), 'openapi_types')

        types.update({
            'preset_configuration': 'Av1PresetConfiguration',
            'auto_level_setup': 'AutoLevelSetup'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Av1VideoConfiguration, self), 'attribute_map'):
            attributes = getattr(super(Av1VideoConfiguration, self), 'attribute_map')

        attributes.update({
            'preset_configuration': 'presetConfiguration',
            'auto_level_setup': 'autoLevelSetup'
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
