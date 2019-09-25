# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsInsightsOrganizationSettingsRequest(object):
    @poscheck_model
    def __init__(self,
                 include_in_insights=None):
        # type: (bool) -> None

        self._include_in_insights = None
        self.discriminator = None

        if include_in_insights is not None:
            self.include_in_insights = include_in_insights

    @property
    def openapi_types(self):
        types = {
            'include_in_insights': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'include_in_insights': 'includeInInsights'
        }
        return attributes

    @property
    def include_in_insights(self):
        # type: () -> bool
        """Gets the include_in_insights of this AnalyticsInsightsOrganizationSettingsRequest.

        Whether the organization's data is being contributed to industry insights

        :return: The include_in_insights of this AnalyticsInsightsOrganizationSettingsRequest.
        :rtype: bool
        """
        return self._include_in_insights

    @include_in_insights.setter
    def include_in_insights(self, include_in_insights):
        # type: (bool) -> None
        """Sets the include_in_insights of this AnalyticsInsightsOrganizationSettingsRequest.

        Whether the organization's data is being contributed to industry insights

        :param include_in_insights: The include_in_insights of this AnalyticsInsightsOrganizationSettingsRequest.
        :type: bool
        """

        if include_in_insights is not None:
            if not isinstance(include_in_insights, bool):
                raise TypeError("Invalid type for `include_in_insights`, type has to be `bool`")

        self._include_in_insights = include_in_insights

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
        if not isinstance(other, AnalyticsInsightsOrganizationSettingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
