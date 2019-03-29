# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.player_third_party_licensing import PlayerThirdPartyLicensing
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class ThirdPartyLicensingApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ThirdPartyLicensingApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, license_id, player_third_party_licensing, **kwargs):
        """Enable Third Party Licensing"""

        return self.api_client.post(
            '/player/licenses/{license_id}/third-party-licensing',
            player_third_party_licensing,
            path_params={'license_id': license_id},
            type=PlayerThirdPartyLicensing,
            **kwargs
        )

    def delete(self, license_id, **kwargs):
        """Delete Third Party Licensing Configuration"""

        return self.api_client.delete(
            '/player/licenses/{license_id}/third-party-licensing',
            path_params={'license_id': license_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, license_id, **kwargs):
        """Get Third Party Licensing Configuration"""

        return self.api_client.get(
            '/player/licenses/{license_id}/third-party-licensing',
            path_params={'license_id': license_id},
            type=PlayerThirdPartyLicensing,
            **kwargs
        )
