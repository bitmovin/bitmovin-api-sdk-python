# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class PlayerLicenseAnalytics(object):
    @poscheck_model
    def __init__(self,
                 analytics_key=None):
        # type: (string_types) -> None

        self._analytics_key = None
        self.discriminator = None

        if analytics_key is not None:
            self.analytics_key = analytics_key

    @property
    def openapi_types(self):
        types = {
            'analytics_key': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'analytics_key': 'analyticsKey'
        }
        return attributes

    @property
    def analytics_key(self):
        # type: () -> string_types
        """Gets the analytics_key of this PlayerLicenseAnalytics.

        Analytics License Key (required)

        :return: The analytics_key of this PlayerLicenseAnalytics.
        :rtype: string_types
        """
        return self._analytics_key

    @analytics_key.setter
    def analytics_key(self, analytics_key):
        # type: (string_types) -> None
        """Sets the analytics_key of this PlayerLicenseAnalytics.

        Analytics License Key (required)

        :param analytics_key: The analytics_key of this PlayerLicenseAnalytics.
        :type: string_types
        """

        if analytics_key is not None:
            if not isinstance(analytics_key, string_types):
                raise TypeError("Invalid type for `analytics_key`, type has to be `string_types`")

        self._analytics_key = analytics_key

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
        if not isinstance(other, PlayerLicenseAnalytics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
