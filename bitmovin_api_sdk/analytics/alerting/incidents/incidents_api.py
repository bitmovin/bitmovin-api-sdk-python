# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_incident import AnalyticsIncident
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.analytics.alerting.incidents.analytics_incident_list_query_params import AnalyticsIncidentListQueryParams
from bitmovin_api_sdk.analytics.alerting.incidents.analytics_incident_list_by_license_key_query_params import AnalyticsIncidentListByLicenseKeyQueryParams


class IncidentsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(IncidentsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params=None, **kwargs):
        # type: (AnalyticsIncidentListQueryParams, dict) -> AnalyticsIncident
        """List Incidents

        :param query_params: Query parameters
        :type query_params: AnalyticsIncidentListQueryParams
        :return: List of incidents
        :rtype: AnalyticsIncident
        """

        return self.api_client.get(
            '/analytics/alerting/incidents',
            query_params=query_params,
            pagination_response=True,
            type=AnalyticsIncident,
            **kwargs
        )

    def list_by_license_key(self, license_key, query_params=None, **kwargs):
        # type: (string_types, AnalyticsIncidentListByLicenseKeyQueryParams, dict) -> AnalyticsIncident
        """List Incidents per license

        :param license_key: License key
        :type license_key: string_types, required
        :param query_params: Query parameters
        :type query_params: AnalyticsIncidentListByLicenseKeyQueryParams
        :return: List of incidents
        :rtype: AnalyticsIncident
        """

        return self.api_client.get(
            '/analytics/alerting/incidents/{license_key}',
            path_params={'license_key': license_key},
            query_params=query_params,
            pagination_response=True,
            type=AnalyticsIncident,
            **kwargs
        )
