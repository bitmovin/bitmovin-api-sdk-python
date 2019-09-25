# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ad_analytics_attribute import AdAnalyticsAttribute
import pprint
import six


class AdAnalyticsAbstractFilter(object):
    @poscheck_model
    def __init__(self,
                 name=None):
        # type: (AdAnalyticsAttribute) -> None

        self._name = None
        self.discriminator = 'operator'

        if name is not None:
            self.name = name

    @property
    def openapi_types(self):
        types = {
            'name': 'AdAnalyticsAttribute'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name'
        }
        return attributes

    discriminator_value_class_map = {
        'IN': 'AdAnalyticsInFilter',
        'EQ': 'AdAnalyticsEqualFilter',
        'NE': 'AdAnalyticsNotEqualFilter',
        'LT': 'AdAnalyticsLessThanFilter',
        'LTE': 'AdAnalyticsLessThanOrEqualFilter',
        'GT': 'AdAnalyticsGreaterThanFilter',
        'GTE': 'AdAnalyticsGreaterThanOrEqualFilter',
        'CONTAINS': 'AdAnalyticsContainsFilter',
        'NOTCONTAINS': 'AdAnalyticsNotContainsFilter'
    }

    @property
    def name(self):
        # type: () -> AdAnalyticsAttribute
        """Gets the name of this AdAnalyticsAbstractFilter.


        :return: The name of this AdAnalyticsAbstractFilter.
        :rtype: AdAnalyticsAttribute
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (AdAnalyticsAttribute) -> None
        """Sets the name of this AdAnalyticsAbstractFilter.


        :param name: The name of this AdAnalyticsAbstractFilter.
        :type: AdAnalyticsAttribute
        """

        if name is not None:
            if not isinstance(name, AdAnalyticsAttribute):
                raise TypeError("Invalid type for `name`, type has to be `AdAnalyticsAttribute`")

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for k, v in iteritems(self.discriminator_value_class_map):
            if v == type(self).__name__:
                result['operator'] = k
                break
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
        if not isinstance(other, AdAnalyticsAbstractFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
