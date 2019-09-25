# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_attribute import AnalyticsAttribute
from bitmovin_api_sdk.models.analytics_order import AnalyticsOrder
import pprint
import six


class AnalyticsOrderByEntry(object):
    @poscheck_model
    def __init__(self,
                 name=None,
                 order=None):
        # type: (AnalyticsAttribute, AnalyticsOrder) -> None

        self._name = None
        self._order = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if order is not None:
            self.order = order

    @property
    def openapi_types(self):
        types = {
            'name': 'AnalyticsAttribute',
            'order': 'AnalyticsOrder'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'name': 'name',
            'order': 'order'
        }
        return attributes

    @property
    def name(self):
        # type: () -> AnalyticsAttribute
        """Gets the name of this AnalyticsOrderByEntry.


        :return: The name of this AnalyticsOrderByEntry.
        :rtype: AnalyticsAttribute
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (AnalyticsAttribute) -> None
        """Sets the name of this AnalyticsOrderByEntry.


        :param name: The name of this AnalyticsOrderByEntry.
        :type: AnalyticsAttribute
        """

        if name is not None:
            if not isinstance(name, AnalyticsAttribute):
                raise TypeError("Invalid type for `name`, type has to be `AnalyticsAttribute`")

        self._name = name

    @property
    def order(self):
        # type: () -> AnalyticsOrder
        """Gets the order of this AnalyticsOrderByEntry.


        :return: The order of this AnalyticsOrderByEntry.
        :rtype: AnalyticsOrder
        """
        return self._order

    @order.setter
    def order(self, order):
        # type: (AnalyticsOrder) -> None
        """Sets the order of this AnalyticsOrderByEntry.


        :param order: The order of this AnalyticsOrderByEntry.
        :type: AnalyticsOrder
        """

        if order is not None:
            if not isinstance(order, AnalyticsOrder):
                raise TypeError("Invalid type for `order`, type has to be `AnalyticsOrder`")

        self._order = order

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
        if not isinstance(other, AnalyticsOrderByEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
