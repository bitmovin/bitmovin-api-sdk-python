# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.analytics_license import AnalyticsLicense
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.analytics.licenses.domains.domains_api import DomainsApi


class LicensesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
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

    def get(self, license_id, **kwargs):
        """Get License"""

        return self.api_client.get(
            '/analytics/licenses/{license_id}',
            path_params={'license_id': license_id},
            type=AnalyticsLicense,
            **kwargs
        )

    def list(self, **kwargs):
        """List Analytics Licenses"""

        return self.api_client.get(
            '/analytics/licenses',
            pagination_response=True,
            type=AnalyticsLicense,
            **kwargs
        )
