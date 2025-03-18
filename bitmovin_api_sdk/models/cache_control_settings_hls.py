# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.cache_control import CacheControl
import pprint
import six


class CacheControlSettingsHls(object):
    @poscheck_model
    def __init__(self,
                 multi_variant_playlist=None,
                 variant_playlist=None):
        # type: (CacheControl, CacheControl) -> None

        self._multi_variant_playlist = None
        self._variant_playlist = None
        self.discriminator = None

        if multi_variant_playlist is not None:
            self.multi_variant_playlist = multi_variant_playlist
        if variant_playlist is not None:
            self.variant_playlist = variant_playlist

    @property
    def openapi_types(self):
        types = {
            'multi_variant_playlist': 'CacheControl',
            'variant_playlist': 'CacheControl'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'multi_variant_playlist': 'multiVariantPlaylist',
            'variant_playlist': 'variantPlaylist'
        }
        return attributes

    @property
    def multi_variant_playlist(self):
        # type: () -> CacheControl
        """Gets the multi_variant_playlist of this CacheControlSettingsHls.

        Cache control settings for HLS Multivariant playlist.

        :return: The multi_variant_playlist of this CacheControlSettingsHls.
        :rtype: CacheControl
        """
        return self._multi_variant_playlist

    @multi_variant_playlist.setter
    def multi_variant_playlist(self, multi_variant_playlist):
        # type: (CacheControl) -> None
        """Sets the multi_variant_playlist of this CacheControlSettingsHls.

        Cache control settings for HLS Multivariant playlist.

        :param multi_variant_playlist: The multi_variant_playlist of this CacheControlSettingsHls.
        :type: CacheControl
        """

        if multi_variant_playlist is not None:
            if not isinstance(multi_variant_playlist, CacheControl):
                raise TypeError("Invalid type for `multi_variant_playlist`, type has to be `CacheControl`")

        self._multi_variant_playlist = multi_variant_playlist

    @property
    def variant_playlist(self):
        # type: () -> CacheControl
        """Gets the variant_playlist of this CacheControlSettingsHls.

        Cache control settings for HLS Media playlist.

        :return: The variant_playlist of this CacheControlSettingsHls.
        :rtype: CacheControl
        """
        return self._variant_playlist

    @variant_playlist.setter
    def variant_playlist(self, variant_playlist):
        # type: (CacheControl) -> None
        """Sets the variant_playlist of this CacheControlSettingsHls.

        Cache control settings for HLS Media playlist.

        :param variant_playlist: The variant_playlist of this CacheControlSettingsHls.
        :type: CacheControl
        """

        if variant_playlist is not None:
            if not isinstance(variant_playlist, CacheControl):
                raise TypeError("Invalid type for `variant_playlist`, type has to be `CacheControl`")

        self._variant_playlist = variant_playlist

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
        if not isinstance(other, CacheControlSettingsHls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
