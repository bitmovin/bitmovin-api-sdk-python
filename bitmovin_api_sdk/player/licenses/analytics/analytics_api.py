# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.player_license_analytics import PlayerLicenseAnalytics
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class AnalyticsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AnalyticsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, license_id, player_license_analytics, **kwargs):
        # type: (string_types, PlayerLicenseAnalytics, dict) -> PlayerLicenseAnalytics
        """Activate Analytics

        :param license_id: Id of the Player License
        :type license_id: string_types, required
        :param player_license_analytics: The Analytics key to be added to the Player License
        :type player_license_analytics: PlayerLicenseAnalytics, required
        :return: Analytics details
        :rtype: PlayerLicenseAnalytics
        """

        return self.api_client.post(
            '/player/licenses/{license_id}/analytics',
            player_license_analytics,
            path_params={'license_id': license_id},
            type=PlayerLicenseAnalytics,
            **kwargs
        )

    def delete(self, license_id, **kwargs):
        # type: (string_types, dict) -> PlayerLicenseAnalytics
        """Deactivate Analytics

        :param license_id: Id of license
        :type license_id: string_types, required
        :return: Analytics details that have just been deactivated
        :rtype: PlayerLicenseAnalytics
        """

        return self.api_client.delete(
            '/player/licenses/{license_id}/analytics',
            path_params={'license_id': license_id},
            type=PlayerLicenseAnalytics,
            **kwargs
        )
