# coding: utf-8
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class PlayerLicenseAnalytics(object):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = {
            'analytics_key': 'str'
        }
        return types

    @property
    def attribute_map(self):
        attributes = {
            'analytics_key': 'analyticsKey'
        }
        return attributes

    def __init__(self, analytics_key=None, *args, **kwargs):

        self._analytics_key = None
        self.discriminator = None

        if analytics_key is not None:
            self.analytics_key = analytics_key

    @property
    def analytics_key(self):
        """Gets the analytics_key of this PlayerLicenseAnalytics.

        Analytics License Key (required)

        :return: The analytics_key of this PlayerLicenseAnalytics.
        :rtype: str
        """
        return self._analytics_key

    @analytics_key.setter
    def analytics_key(self, analytics_key):
        """Sets the analytics_key of this PlayerLicenseAnalytics.

        Analytics License Key (required)

        :param analytics_key: The analytics_key of this PlayerLicenseAnalytics.
        :type: str
        """

        if analytics_key is not None:
            if not isinstance(analytics_key, str):
                raise TypeError("Invalid type for `analytics_key`, type has to be `str`")

        self._analytics_key = analytics_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(PlayerLicenseAnalytics, dict):
                for key, value in self.items():
                    result[key] = value

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
