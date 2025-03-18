# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.cache_control import CacheControl
import pprint
import six


class CacheControlSettingsSegments(object):
    @poscheck_model
    def __init__(self,
                 init_segment=None,
                 media_segment=None):
        # type: (CacheControl, CacheControl) -> None

        self._init_segment = None
        self._media_segment = None
        self.discriminator = None

        if init_segment is not None:
            self.init_segment = init_segment
        if media_segment is not None:
            self.media_segment = media_segment

    @property
    def openapi_types(self):
        types = {
            'init_segment': 'CacheControl',
            'media_segment': 'CacheControl'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'init_segment': 'initSegment',
            'media_segment': 'mediaSegment'
        }
        return attributes

    @property
    def init_segment(self):
        # type: () -> CacheControl
        """Gets the init_segment of this CacheControlSettingsSegments.

        Cache control settings for init segment.

        :return: The init_segment of this CacheControlSettingsSegments.
        :rtype: CacheControl
        """
        return self._init_segment

    @init_segment.setter
    def init_segment(self, init_segment):
        # type: (CacheControl) -> None
        """Sets the init_segment of this CacheControlSettingsSegments.

        Cache control settings for init segment.

        :param init_segment: The init_segment of this CacheControlSettingsSegments.
        :type: CacheControl
        """

        if init_segment is not None:
            if not isinstance(init_segment, CacheControl):
                raise TypeError("Invalid type for `init_segment`, type has to be `CacheControl`")

        self._init_segment = init_segment

    @property
    def media_segment(self):
        # type: () -> CacheControl
        """Gets the media_segment of this CacheControlSettingsSegments.

        Cache control settings for media segment.

        :return: The media_segment of this CacheControlSettingsSegments.
        :rtype: CacheControl
        """
        return self._media_segment

    @media_segment.setter
    def media_segment(self, media_segment):
        # type: (CacheControl) -> None
        """Sets the media_segment of this CacheControlSettingsSegments.

        Cache control settings for media segment.

        :param media_segment: The media_segment of this CacheControlSettingsSegments.
        :type: CacheControl
        """

        if media_segment is not None:
            if not isinstance(media_segment, CacheControl):
                raise TypeError("Invalid type for `media_segment`, type has to be `CacheControl`")

        self._media_segment = media_segment

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
        if not isinstance(other, CacheControlSettingsSegments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
