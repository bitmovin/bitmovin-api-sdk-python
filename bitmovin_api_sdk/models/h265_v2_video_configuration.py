# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.color_config import ColorConfig
from bitmovin_api_sdk.models.display_aspect_ratio import DisplayAspectRatio
from bitmovin_api_sdk.models.encoding_mode import EncodingMode
from bitmovin_api_sdk.models.h265_dynamic_range_format import H265DynamicRangeFormat
from bitmovin_api_sdk.models.h265_v2_motion_compensated_temporal_filtering import H265V2MotionCompensatedTemporalFiltering
from bitmovin_api_sdk.models.h265_v2_preset_configuration import H265V2PresetConfiguration
from bitmovin_api_sdk.models.h265_v2_rate_control_mode_config import H265V2RateControlModeConfig
from bitmovin_api_sdk.models.pixel_format import PixelFormat
from bitmovin_api_sdk.models.video_configuration import VideoConfiguration
import pprint
import six


class H265V2VideoConfiguration(VideoConfiguration):
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
                 dynamic_range_format=None,
                 rate_control_mode_config=None,
                 motion_compensated_temporal_filtering=None,
                 level_high_tier=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, int, float, PixelFormat, ColorConfig, int, int, DisplayAspectRatio, EncodingMode, H265V2PresetConfiguration, H265DynamicRangeFormat, H265V2RateControlModeConfig, H265V2MotionCompensatedTemporalFiltering, bool) -> None
        super(H265V2VideoConfiguration, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, width=width, height=height, bitrate=bitrate, rate=rate, pixel_format=pixel_format, color_config=color_config, sample_aspect_ratio_numerator=sample_aspect_ratio_numerator, sample_aspect_ratio_denominator=sample_aspect_ratio_denominator, display_aspect_ratio=display_aspect_ratio, encoding_mode=encoding_mode)

        self._preset_configuration = None
        self._dynamic_range_format = None
        self._rate_control_mode_config = None
        self._motion_compensated_temporal_filtering = None
        self._level_high_tier = None
        self.discriminator = None

        if preset_configuration is not None:
            self.preset_configuration = preset_configuration
        if dynamic_range_format is not None:
            self.dynamic_range_format = dynamic_range_format
        if rate_control_mode_config is not None:
            self.rate_control_mode_config = rate_control_mode_config
        if motion_compensated_temporal_filtering is not None:
            self.motion_compensated_temporal_filtering = motion_compensated_temporal_filtering
        if level_high_tier is not None:
            self.level_high_tier = level_high_tier

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(H265V2VideoConfiguration, self), 'openapi_types'):
            types = getattr(super(H265V2VideoConfiguration, self), 'openapi_types')

        types.update({
            'preset_configuration': 'H265V2PresetConfiguration',
            'dynamic_range_format': 'H265DynamicRangeFormat',
            'rate_control_mode_config': 'H265V2RateControlModeConfig',
            'motion_compensated_temporal_filtering': 'H265V2MotionCompensatedTemporalFiltering',
            'level_high_tier': 'bool'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(H265V2VideoConfiguration, self), 'attribute_map'):
            attributes = getattr(super(H265V2VideoConfiguration, self), 'attribute_map')

        attributes.update({
            'preset_configuration': 'presetConfiguration',
            'dynamic_range_format': 'dynamicRangeFormat',
            'rate_control_mode_config': 'rateControlModeConfig',
            'motion_compensated_temporal_filtering': 'motionCompensatedTemporalFiltering',
            'level_high_tier': 'levelHighTier'
        })
        return attributes

    @property
    def preset_configuration(self):
        # type: () -> H265V2PresetConfiguration
        """Gets the preset_configuration of this H265V2VideoConfiguration.

        Use a set of well defined configurations preset to support certain use cases. Can be overwritten with more specific values.

        :return: The preset_configuration of this H265V2VideoConfiguration.
        :rtype: H265V2PresetConfiguration
        """
        return self._preset_configuration

    @preset_configuration.setter
    def preset_configuration(self, preset_configuration):
        # type: (H265V2PresetConfiguration) -> None
        """Sets the preset_configuration of this H265V2VideoConfiguration.

        Use a set of well defined configurations preset to support certain use cases. Can be overwritten with more specific values.

        :param preset_configuration: The preset_configuration of this H265V2VideoConfiguration.
        :type: H265V2PresetConfiguration
        """

        if preset_configuration is not None:
            if not isinstance(preset_configuration, H265V2PresetConfiguration):
                raise TypeError("Invalid type for `preset_configuration`, type has to be `H265V2PresetConfiguration`")

        self._preset_configuration = preset_configuration

    @property
    def dynamic_range_format(self):
        # type: () -> H265DynamicRangeFormat
        """Gets the dynamic_range_format of this H265V2VideoConfiguration.

        Automatically configures the encoder for the given SDR/HDR format.

        :return: The dynamic_range_format of this H265V2VideoConfiguration.
        :rtype: H265DynamicRangeFormat
        """
        return self._dynamic_range_format

    @dynamic_range_format.setter
    def dynamic_range_format(self, dynamic_range_format):
        # type: (H265DynamicRangeFormat) -> None
        """Sets the dynamic_range_format of this H265V2VideoConfiguration.

        Automatically configures the encoder for the given SDR/HDR format.

        :param dynamic_range_format: The dynamic_range_format of this H265V2VideoConfiguration.
        :type: H265DynamicRangeFormat
        """

        if dynamic_range_format is not None:
            if not isinstance(dynamic_range_format, H265DynamicRangeFormat):
                raise TypeError("Invalid type for `dynamic_range_format`, type has to be `H265DynamicRangeFormat`")

        self._dynamic_range_format = dynamic_range_format

    @property
    def rate_control_mode_config(self):
        # type: () -> H265V2RateControlModeConfig
        """Gets the rate_control_mode_config of this H265V2VideoConfiguration.

        Rate control mode configuration. Used to Configure the Perceptual Encoding Mode Settings.

        :return: The rate_control_mode_config of this H265V2VideoConfiguration.
        :rtype: H265V2RateControlModeConfig
        """
        return self._rate_control_mode_config

    @rate_control_mode_config.setter
    def rate_control_mode_config(self, rate_control_mode_config):
        # type: (H265V2RateControlModeConfig) -> None
        """Sets the rate_control_mode_config of this H265V2VideoConfiguration.

        Rate control mode configuration. Used to Configure the Perceptual Encoding Mode Settings.

        :param rate_control_mode_config: The rate_control_mode_config of this H265V2VideoConfiguration.
        :type: H265V2RateControlModeConfig
        """

        if rate_control_mode_config is not None:
            if not isinstance(rate_control_mode_config, H265V2RateControlModeConfig):
                raise TypeError("Invalid type for `rate_control_mode_config`, type has to be `H265V2RateControlModeConfig`")

        self._rate_control_mode_config = rate_control_mode_config

    @property
    def motion_compensated_temporal_filtering(self):
        # type: () -> H265V2MotionCompensatedTemporalFiltering
        """Gets the motion_compensated_temporal_filtering of this H265V2VideoConfiguration.

        Motion compensated temporal filtering mode.

        :return: The motion_compensated_temporal_filtering of this H265V2VideoConfiguration.
        :rtype: H265V2MotionCompensatedTemporalFiltering
        """
        return self._motion_compensated_temporal_filtering

    @motion_compensated_temporal_filtering.setter
    def motion_compensated_temporal_filtering(self, motion_compensated_temporal_filtering):
        # type: (H265V2MotionCompensatedTemporalFiltering) -> None
        """Sets the motion_compensated_temporal_filtering of this H265V2VideoConfiguration.

        Motion compensated temporal filtering mode.

        :param motion_compensated_temporal_filtering: The motion_compensated_temporal_filtering of this H265V2VideoConfiguration.
        :type: H265V2MotionCompensatedTemporalFiltering
        """

        if motion_compensated_temporal_filtering is not None:
            if not isinstance(motion_compensated_temporal_filtering, H265V2MotionCompensatedTemporalFiltering):
                raise TypeError("Invalid type for `motion_compensated_temporal_filtering`, type has to be `H265V2MotionCompensatedTemporalFiltering`")

        self._motion_compensated_temporal_filtering = motion_compensated_temporal_filtering

    @property
    def level_high_tier(self):
        # type: () -> bool
        """Gets the level_high_tier of this H265V2VideoConfiguration.

        Set codec tier to high when true, main when false.

        :return: The level_high_tier of this H265V2VideoConfiguration.
        :rtype: bool
        """
        return self._level_high_tier

    @level_high_tier.setter
    def level_high_tier(self, level_high_tier):
        # type: (bool) -> None
        """Sets the level_high_tier of this H265V2VideoConfiguration.

        Set codec tier to high when true, main when false.

        :param level_high_tier: The level_high_tier of this H265V2VideoConfiguration.
        :type: bool
        """

        if level_high_tier is not None:
            if not isinstance(level_high_tier, bool):
                raise TypeError("Invalid type for `level_high_tier`, type has to be `bool`")

        self._level_high_tier = level_high_tier

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(H265V2VideoConfiguration, self), "to_dict"):
            result = super(H265V2VideoConfiguration, self).to_dict()
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
        if not isinstance(other, H265V2VideoConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
