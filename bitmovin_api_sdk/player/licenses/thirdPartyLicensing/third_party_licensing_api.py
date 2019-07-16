# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.player_third_party_licensing import PlayerThirdPartyLicensing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class ThirdPartyLicensingApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ThirdPartyLicensingApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, license_id, player_third_party_licensing, **kwargs):
        # type: (string_types, PlayerThirdPartyLicensing, dict) -> PlayerThirdPartyLicensing
        """Enable Third Party Licensing

        :param license_id: Id of the Player License
        :type license_id: string_types, required
        :param player_third_party_licensing: Third Party Licensing settings to apply to Player License
        :type player_third_party_licensing: PlayerThirdPartyLicensing, required
        :return: Third party licensing details
        :rtype: PlayerThirdPartyLicensing
        """

        return self.api_client.post(
            '/player/licenses/{license_id}/third-party-licensing',
            player_third_party_licensing,
            path_params={'license_id': license_id},
            type=PlayerThirdPartyLicensing,
            **kwargs
        )

    def delete(self, license_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Third Party Licensing Configuration

        :param license_id: Id of the Player License
        :type license_id: string_types, required
        :return: Id of the deleted Third Party Licensing Configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/player/licenses/{license_id}/third-party-licensing',
            path_params={'license_id': license_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, license_id, **kwargs):
        # type: (string_types, dict) -> PlayerThirdPartyLicensing
        """Get Third Party Licensing Configuration

        :param license_id: Id of the Player License
        :type license_id: string_types, required
        :return: Third party licensing details
        :rtype: PlayerThirdPartyLicensing
        """

        return self.api_client.get(
            '/player/licenses/{license_id}/third-party-licensing',
            path_params={'license_id': license_id},
            type=PlayerThirdPartyLicensing,
            **kwargs
        )
