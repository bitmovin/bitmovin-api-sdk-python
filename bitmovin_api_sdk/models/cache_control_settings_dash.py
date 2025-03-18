# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.cache_control import CacheControl
import pprint
import six


class CacheControlSettingsDash(object):
    @poscheck_model
    def __init__(self,
                 timeline_manifest=None,
                 template_manifest=None):
        # type: (CacheControl, CacheControl) -> None

        self._timeline_manifest = None
        self._template_manifest = None
        self.discriminator = None

        if timeline_manifest is not None:
            self.timeline_manifest = timeline_manifest
        if template_manifest is not None:
            self.template_manifest = template_manifest

    @property
    def openapi_types(self):
        types = {
            'timeline_manifest': 'CacheControl',
            'template_manifest': 'CacheControl'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'timeline_manifest': 'timelineManifest',
            'template_manifest': 'templateManifest'
        }
        return attributes

    @property
    def timeline_manifest(self):
        # type: () -> CacheControl
        """Gets the timeline_manifest of this CacheControlSettingsDash.

        Cache control settings for DASH Timeline manifest.

        :return: The timeline_manifest of this CacheControlSettingsDash.
        :rtype: CacheControl
        """
        return self._timeline_manifest

    @timeline_manifest.setter
    def timeline_manifest(self, timeline_manifest):
        # type: (CacheControl) -> None
        """Sets the timeline_manifest of this CacheControlSettingsDash.

        Cache control settings for DASH Timeline manifest.

        :param timeline_manifest: The timeline_manifest of this CacheControlSettingsDash.
        :type: CacheControl
        """

        if timeline_manifest is not None:
            if not isinstance(timeline_manifest, CacheControl):
                raise TypeError("Invalid type for `timeline_manifest`, type has to be `CacheControl`")

        self._timeline_manifest = timeline_manifest

    @property
    def template_manifest(self):
        # type: () -> CacheControl
        """Gets the template_manifest of this CacheControlSettingsDash.

        Cache control settings for DASH Template manifest.

        :return: The template_manifest of this CacheControlSettingsDash.
        :rtype: CacheControl
        """
        return self._template_manifest

    @template_manifest.setter
    def template_manifest(self, template_manifest):
        # type: (CacheControl) -> None
        """Sets the template_manifest of this CacheControlSettingsDash.

        Cache control settings for DASH Template manifest.

        :param template_manifest: The template_manifest of this CacheControlSettingsDash.
        :type: CacheControl
        """

        if template_manifest is not None:
            if not isinstance(template_manifest, CacheControl):
                raise TypeError("Invalid type for `template_manifest`, type has to be `CacheControl`")

        self._template_manifest = template_manifest

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
        if not isinstance(other, CacheControlSettingsDash):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
