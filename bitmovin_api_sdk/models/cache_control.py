# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class CacheControl(object):
    @poscheck_model
    def __init__(self,
                 cache_control=None):
        # type: (string_types) -> None

        self._cache_control = None
        self.discriminator = None

        if cache_control is not None:
            self.cache_control = cache_control

    @property
    def openapi_types(self):
        types = {
            'cache_control': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'cache_control': 'cacheControl'
        }
        return attributes

    @property
    def cache_control(self):
        # type: () -> string_types
        """Gets the cache_control of this CacheControl.

        Cache control for storing data on CDN. Example \"public, max-age=0, no-cache\".

        :return: The cache_control of this CacheControl.
        :rtype: string_types
        """
        return self._cache_control

    @cache_control.setter
    def cache_control(self, cache_control):
        # type: (string_types) -> None
        """Sets the cache_control of this CacheControl.

        Cache control for storing data on CDN. Example \"public, max-age=0, no-cache\".

        :param cache_control: The cache_control of this CacheControl.
        :type: string_types
        """

        if cache_control is not None:
            if not isinstance(cache_control, string_types):
                raise TypeError("Invalid type for `cache_control`, type has to be `string_types`")

        self._cache_control = cache_control

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
        if not isinstance(other, CacheControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
