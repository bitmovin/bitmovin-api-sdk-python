# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_license import AnalyticsLicense
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.analytics.licenses.domains.domains_api import DomainsApi
from bitmovin_api_sdk.analytics.licenses.analytics_license_list_query_params import AnalyticsLicenseListQueryParams


class LicensesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LicensesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.domains = DomainsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, analytics_license, **kwargs):
        # type: (AnalyticsLicense, dict) -> AnalyticsLicense
        """Create Analytics License

        :param analytics_license: Analytics License to be created
        :type analytics_license: AnalyticsLicense, required
        :return: Created Analytics license
        :rtype: AnalyticsLicense
        """

        return self.api_client.post(
            '/analytics/licenses',
            analytics_license,
            type=AnalyticsLicense,
            **kwargs
        )

    def get(self, license_id, **kwargs):
        # type: (string_types, dict) -> AnalyticsLicense
        """Get License

        :param license_id: License id
        :type license_id: string_types, required
        :return: Analytics License
        :rtype: AnalyticsLicense
        """

        return self.api_client.get(
            '/analytics/licenses/{license_id}',
            path_params={'license_id': license_id},
            type=AnalyticsLicense,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AnalyticsLicenseListQueryParams, dict) -> AnalyticsLicense
        """List Analytics Licenses

        :param query_params: Query parameters
        :type query_params: AnalyticsLicenseListQueryParams
        :return: List of Analytics Licenses
        :rtype: AnalyticsLicense
        """

        return self.api_client.get(
            '/analytics/licenses',
            query_params=query_params,
            pagination_response=True,
            type=AnalyticsLicense,
            **kwargs
        )

    def update(self, license_id, analytics_license, **kwargs):
        # type: (string_types, AnalyticsLicense, dict) -> AnalyticsLicense
        """Update Analytics License

        :param license_id: License id
        :type license_id: string_types, required
        :param analytics_license: Analytics License details to be updated
        :type analytics_license: AnalyticsLicense, required
        :return: Updated Analytics License
        :rtype: AnalyticsLicense
        """

        return self.api_client.put(
            '/analytics/licenses/{license_id}',
            analytics_license,
            path_params={'license_id': license_id},
            type=AnalyticsLicense,
            **kwargs
        )
