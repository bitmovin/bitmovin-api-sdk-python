# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.cache_control_settings_dash import CacheControlSettingsDash
from bitmovin_api_sdk.models.cache_control_settings_hls import CacheControlSettingsHls
from bitmovin_api_sdk.models.cache_control_settings_segments import CacheControlSettingsSegments
import pprint
import six


class CacheControlSettings(object):
    @poscheck_model
    def __init__(self,
                 hls=None,
                 dash=None,
                 segments=None):
        # type: (CacheControlSettingsHls, CacheControlSettingsDash, CacheControlSettingsSegments) -> None

        self._hls = None
        self._dash = None
        self._segments = None
        self.discriminator = None

        if hls is not None:
            self.hls = hls
        if dash is not None:
            self.dash = dash
        if segments is not None:
            self.segments = segments

    @property
    def openapi_types(self):
        types = {
            'hls': 'CacheControlSettingsHls',
            'dash': 'CacheControlSettingsDash',
            'segments': 'CacheControlSettingsSegments'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'hls': 'hls',
            'dash': 'dash',
            'segments': 'segments'
        }
        return attributes

    @property
    def hls(self):
        # type: () -> CacheControlSettingsHls
        """Gets the hls of this CacheControlSettings.

        Cache control settings for HLS manifest.

        :return: The hls of this CacheControlSettings.
        :rtype: CacheControlSettingsHls
        """
        return self._hls

    @hls.setter
    def hls(self, hls):
        # type: (CacheControlSettingsHls) -> None
        """Sets the hls of this CacheControlSettings.

        Cache control settings for HLS manifest.

        :param hls: The hls of this CacheControlSettings.
        :type: CacheControlSettingsHls
        """

        if hls is not None:
            if not isinstance(hls, CacheControlSettingsHls):
                raise TypeError("Invalid type for `hls`, type has to be `CacheControlSettingsHls`")

        self._hls = hls

    @property
    def dash(self):
        # type: () -> CacheControlSettingsDash
        """Gets the dash of this CacheControlSettings.

        Cache control settings for DASH manifest.

        :return: The dash of this CacheControlSettings.
        :rtype: CacheControlSettingsDash
        """
        return self._dash

    @dash.setter
    def dash(self, dash):
        # type: (CacheControlSettingsDash) -> None
        """Sets the dash of this CacheControlSettings.

        Cache control settings for DASH manifest.

        :param dash: The dash of this CacheControlSettings.
        :type: CacheControlSettingsDash
        """

        if dash is not None:
            if not isinstance(dash, CacheControlSettingsDash):
                raise TypeError("Invalid type for `dash`, type has to be `CacheControlSettingsDash`")

        self._dash = dash

    @property
    def segments(self):
        # type: () -> CacheControlSettingsSegments
        """Gets the segments of this CacheControlSettings.

        Cache control settings for segments.

        :return: The segments of this CacheControlSettings.
        :rtype: CacheControlSettingsSegments
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        # type: (CacheControlSettingsSegments) -> None
        """Sets the segments of this CacheControlSettings.

        Cache control settings for segments.

        :param segments: The segments of this CacheControlSettings.
        :type: CacheControlSettingsSegments
        """

        if segments is not None:
            if not isinstance(segments, CacheControlSettingsSegments):
                raise TypeError("Invalid type for `segments`, type has to be `CacheControlSettingsSegments`")

        self._segments = segments

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
        if not isinstance(other, CacheControlSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
