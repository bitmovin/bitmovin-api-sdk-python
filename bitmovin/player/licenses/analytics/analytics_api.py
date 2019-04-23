# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.player_license_analytics import PlayerLicenseAnalytics
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class AnalyticsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AnalyticsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, license_id, player_license_analytics, **kwargs):
        """Activate Analytics"""

        return self.api_client.post(
            '/player/licenses/{license_id}/analytics',
            player_license_analytics,
            path_params={'license_id': license_id},
            type=PlayerLicenseAnalytics,
            **kwargs
        )

    def delete(self, license_id, **kwargs):
        """Deactivate Analytics"""

        return self.api_client.delete(
            '/player/licenses/{license_id}/analytics',
            path_params={'license_id': license_id},
            type=PlayerLicenseAnalytics,
            **kwargs
        )
