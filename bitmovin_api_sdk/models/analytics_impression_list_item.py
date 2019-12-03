# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsImpressionListItem(object):
    @poscheck_model
    def __init__(self,
                 impression_id=None):
        # type: (string_types) -> None

        self._impression_id = None
        self.discriminator = None

        if impression_id is not None:
            self.impression_id = impression_id

    @property
    def openapi_types(self):
        types = {
            'impression_id': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'impression_id': 'impressionId'
        }
        return attributes

    @property
    def impression_id(self):
        # type: () -> string_types
        """Gets the impression_id of this AnalyticsImpressionListItem.

        Impression ID (required)

        :return: The impression_id of this AnalyticsImpressionListItem.
        :rtype: string_types
        """
        return self._impression_id

    @impression_id.setter
    def impression_id(self, impression_id):
        # type: (string_types) -> None
        """Sets the impression_id of this AnalyticsImpressionListItem.

        Impression ID (required)

        :param impression_id: The impression_id of this AnalyticsImpressionListItem.
        :type: string_types
        """

        if impression_id is not None:
            if not isinstance(impression_id, string_types):
                raise TypeError("Invalid type for `impression_id`, type has to be `string_types`")

        self._impression_id = impression_id

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
        if not isinstance(other, AnalyticsImpressionListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
