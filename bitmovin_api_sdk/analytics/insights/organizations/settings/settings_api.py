# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_insights_organization_settings import AnalyticsInsightsOrganizationSettings
from bitmovin_api_sdk.models.analytics_insights_organization_settings_request import AnalyticsInsightsOrganizationSettingsRequest
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class SettingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SettingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, organization_id, **kwargs):
        # type: (string_types, dict) -> AnalyticsInsightsOrganizationSettings
        """Get the current organization settings for industry insights

        :param organization_id: Organization id
        :type organization_id: string_types, required
        :return: Analytics organization settings
        :rtype: AnalyticsInsightsOrganizationSettings
        """

        return self.api_client.get(
            '/analytics/insights/organizations/{organization_id}/settings',
            path_params={'organization_id': organization_id},
            type=AnalyticsInsightsOrganizationSettings,
            **kwargs
        )

    def update(self, organization_id, analytics_insights_organization_settings_request, **kwargs):
        # type: (string_types, AnalyticsInsightsOrganizationSettingsRequest, dict) -> AnalyticsInsightsOrganizationSettings
        """Update the organization settings for industry insights

        :param organization_id: Organization id
        :type organization_id: string_types, required
        :param analytics_insights_organization_settings_request: Organization settings to be updated
        :type analytics_insights_organization_settings_request: AnalyticsInsightsOrganizationSettingsRequest, required
        :return: Updated analytics organization settings
        :rtype: AnalyticsInsightsOrganizationSettings
        """

        return self.api_client.put(
            '/analytics/insights/organizations/{organization_id}/settings',
            analytics_insights_organization_settings_request,
            path_params={'organization_id': organization_id},
            type=AnalyticsInsightsOrganizationSettings,
            **kwargs
        )
