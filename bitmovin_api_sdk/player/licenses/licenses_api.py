# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.player_license import PlayerLicense
from bitmovin_api_sdk.models.player_license_update_request import PlayerLicenseUpdateRequest
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.player.licenses.analytics.analytics_api import AnalyticsApi
from bitmovin_api_sdk.player.licenses.domains.domains_api import DomainsApi
from bitmovin_api_sdk.player.licenses.third_party_licensing.third_party_licensing_api import ThirdPartyLicensingApi
from bitmovin_api_sdk.player.licenses.player_license_list_query_params import PlayerLicenseListQueryParams


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

        self.analytics = AnalyticsApi(
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

        self.third_party_licensing = ThirdPartyLicensingApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, player_license, **kwargs):
        # type: (PlayerLicense, dict) -> PlayerLicense
        """Create Player License

        :param player_license: Player License to be created
        :type player_license: PlayerLicense, required
        :return: Created Player license
        :rtype: PlayerLicense
        """

        return self.api_client.post(
            '/player/licenses',
            player_license,
            type=PlayerLicense,
            **kwargs
        )

    def get(self, license_id, **kwargs):
        # type: (string_types, dict) -> PlayerLicense
        """Get License

        :param license_id: ID of the License
        :type license_id: string_types, required
        :return: Id of Player License
        :rtype: PlayerLicense
        """

        return self.api_client.get(
            '/player/licenses/{license_id}',
            path_params={'license_id': license_id},
            type=PlayerLicense,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (PlayerLicenseListQueryParams, dict) -> PlayerLicense
        """List Player Licenses

        :param query_params: Query parameters
        :type query_params: PlayerLicenseListQueryParams
        :return: Service specific result
        :rtype: PlayerLicense
        """

        return self.api_client.get(
            '/player/licenses',
            query_params=query_params,
            pagination_response=True,
            type=PlayerLicense,
            **kwargs
        )

    def update(self, license_id, player_license_update_request, **kwargs):
        # type: (string_types, PlayerLicenseUpdateRequest, dict) -> PlayerLicense
        """Update License

        :param license_id: License id
        :type license_id: string_types, required
        :param player_license_update_request: Player License details to be updated
        :type player_license_update_request: PlayerLicenseUpdateRequest, required
        :return: Updated Player License
        :rtype: PlayerLicense
        """

        return self.api_client.put(
            '/player/licenses/{license_id}',
            player_license_update_request,
            path_params={'license_id': license_id},
            type=PlayerLicense,
            **kwargs
        )
