# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.ad_analytics_abstract_filter import AdAnalyticsAbstractFilter
from bitmovin_api_sdk.models.ad_analytics_attribute import AdAnalyticsAttribute
import pprint
import six


class AdAnalyticsContainsFilter(AdAnalyticsAbstractFilter):
    @poscheck_model
    def __init__(self,
                 name=None,
                 value=None):
        # type: (AdAnalyticsAttribute, object) -> None
        super(AdAnalyticsContainsFilter, self).__init__(name=name)

        self._value = None
        self.discriminator = None

        if value is not None:
            self.value = value

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AdAnalyticsContainsFilter, self), 'openapi_types'):
            types = getattr(super(AdAnalyticsContainsFilter, self), 'openapi_types')

        types.update({
            'value': 'object'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AdAnalyticsContainsFilter, self), 'attribute_map'):
            attributes = getattr(super(AdAnalyticsContainsFilter, self), 'attribute_map')

        attributes.update({
            'value': 'value'
        })
        return attributes

    @property
    def value(self):
        # type: () -> object
        """Gets the value of this AdAnalyticsContainsFilter.


        :return: The value of this AdAnalyticsContainsFilter.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        # type: (object) -> None
        """Sets the value of this AdAnalyticsContainsFilter.


        :param value: The value of this AdAnalyticsContainsFilter.
        :type: object
        """

        if value is not None:
            if not isinstance(value, object):
                raise TypeError("Invalid type for `value`, type has to be `object`")

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(AdAnalyticsContainsFilter, self), "to_dict"):
            result = super(AdAnalyticsContainsFilter, self).to_dict()
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
        if not isinstance(other, AdAnalyticsContainsFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
