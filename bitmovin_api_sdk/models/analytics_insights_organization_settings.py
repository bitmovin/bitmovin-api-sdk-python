# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class AnalyticsInsightsOrganizationSettings(object):
    @poscheck_model
    def __init__(self,
                 org_id=None,
                 include_in_insights=None,
                 industry=None,
                 sub_industry=None,
                 is_trial=None):
        # type: (string_types, bool, string_types, string_types, bool) -> None

        self._org_id = None
        self._include_in_insights = None
        self._industry = None
        self._sub_industry = None
        self._is_trial = None
        self.discriminator = None

        if org_id is not None:
            self.org_id = org_id
        if include_in_insights is not None:
            self.include_in_insights = include_in_insights
        if industry is not None:
            self.industry = industry
        if sub_industry is not None:
            self.sub_industry = sub_industry
        if is_trial is not None:
            self.is_trial = is_trial

    @property
    def openapi_types(self):
        types = {
            'org_id': 'string_types',
            'include_in_insights': 'bool',
            'industry': 'string_types',
            'sub_industry': 'string_types',
            'is_trial': 'bool'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'org_id': 'orgId',
            'include_in_insights': 'includeInInsights',
            'industry': 'industry',
            'sub_industry': 'subIndustry',
            'is_trial': 'isTrial'
        }
        return attributes

    @property
    def org_id(self):
        # type: () -> string_types
        """Gets the org_id of this AnalyticsInsightsOrganizationSettings.

        Organization ID

        :return: The org_id of this AnalyticsInsightsOrganizationSettings.
        :rtype: string_types
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        # type: (string_types) -> None
        """Sets the org_id of this AnalyticsInsightsOrganizationSettings.

        Organization ID

        :param org_id: The org_id of this AnalyticsInsightsOrganizationSettings.
        :type: string_types
        """

        if org_id is not None:
            if not isinstance(org_id, string_types):
                raise TypeError("Invalid type for `org_id`, type has to be `string_types`")

        self._org_id = org_id

    @property
    def include_in_insights(self):
        # type: () -> bool
        """Gets the include_in_insights of this AnalyticsInsightsOrganizationSettings.

        Whether the organization's data is included in the industry insights

        :return: The include_in_insights of this AnalyticsInsightsOrganizationSettings.
        :rtype: bool
        """
        return self._include_in_insights

    @include_in_insights.setter
    def include_in_insights(self, include_in_insights):
        # type: (bool) -> None
        """Sets the include_in_insights of this AnalyticsInsightsOrganizationSettings.

        Whether the organization's data is included in the industry insights

        :param include_in_insights: The include_in_insights of this AnalyticsInsightsOrganizationSettings.
        :type: bool
        """

        if include_in_insights is not None:
            if not isinstance(include_in_insights, bool):
                raise TypeError("Invalid type for `include_in_insights`, type has to be `bool`")

        self._include_in_insights = include_in_insights

    @property
    def industry(self):
        # type: () -> string_types
        """Gets the industry of this AnalyticsInsightsOrganizationSettings.

        Industry of the organization

        :return: The industry of this AnalyticsInsightsOrganizationSettings.
        :rtype: string_types
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        # type: (string_types) -> None
        """Sets the industry of this AnalyticsInsightsOrganizationSettings.

        Industry of the organization

        :param industry: The industry of this AnalyticsInsightsOrganizationSettings.
        :type: string_types
        """

        if industry is not None:
            if not isinstance(industry, string_types):
                raise TypeError("Invalid type for `industry`, type has to be `string_types`")

        self._industry = industry

    @property
    def sub_industry(self):
        # type: () -> string_types
        """Gets the sub_industry of this AnalyticsInsightsOrganizationSettings.

        Subindustry of the organization

        :return: The sub_industry of this AnalyticsInsightsOrganizationSettings.
        :rtype: string_types
        """
        return self._sub_industry

    @sub_industry.setter
    def sub_industry(self, sub_industry):
        # type: (string_types) -> None
        """Sets the sub_industry of this AnalyticsInsightsOrganizationSettings.

        Subindustry of the organization

        :param sub_industry: The sub_industry of this AnalyticsInsightsOrganizationSettings.
        :type: string_types
        """

        if sub_industry is not None:
            if not isinstance(sub_industry, string_types):
                raise TypeError("Invalid type for `sub_industry`, type has to be `string_types`")

        self._sub_industry = sub_industry

    @property
    def is_trial(self):
        # type: () -> bool
        """Gets the is_trial of this AnalyticsInsightsOrganizationSettings.

        Whether the organization is on an analytics trial plan

        :return: The is_trial of this AnalyticsInsightsOrganizationSettings.
        :rtype: bool
        """
        return self._is_trial

    @is_trial.setter
    def is_trial(self, is_trial):
        # type: (bool) -> None
        """Sets the is_trial of this AnalyticsInsightsOrganizationSettings.

        Whether the organization is on an analytics trial plan

        :param is_trial: The is_trial of this AnalyticsInsightsOrganizationSettings.
        :type: bool
        """

        if is_trial is not None:
            if not isinstance(is_trial, bool):
                raise TypeError("Invalid type for `is_trial`, type has to be `bool`")

        self._is_trial = is_trial

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
        if not isinstance(other, AnalyticsInsightsOrganizationSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
