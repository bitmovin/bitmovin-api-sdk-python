# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.custom_web_player_build_domain import CustomWebPlayerBuildDomain
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class DomainsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DomainsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, custom_web_player_build_domain, **kwargs):
        # type: (CustomWebPlayerBuildDomain, dict) -> CustomWebPlayerBuildDomain
        """Add Domain

        :param custom_web_player_build_domain: The Domain to be added
        :type custom_web_player_build_domain: CustomWebPlayerBuildDomain, required
        :return: Domain details
        :rtype: CustomWebPlayerBuildDomain
        """

        return self.api_client.post(
            '/player/custom-builds/web/domains',
            custom_web_player_build_domain,
            type=CustomWebPlayerBuildDomain,
            **kwargs
        )

    def delete(self, domain_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Domain

        :param domain_id: Id of the domain
        :type domain_id: string_types, required
        :return: Id of the domain
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/player/custom-builds/web/domains/{domain_id}',
            path_params={'domain_id': domain_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, domain_id, **kwargs):
        # type: (string_types, dict) -> CustomWebPlayerBuildDomain
        """Get Domain Details

        :param domain_id: Id of the domain
        :type domain_id: string_types, required
        :return: Id of the domain
        :rtype: CustomWebPlayerBuildDomain
        """

        return self.api_client.get(
            '/player/custom-builds/web/domains/{domain_id}',
            path_params={'domain_id': domain_id},
            type=CustomWebPlayerBuildDomain,
            **kwargs
        )

    def list(self, **kwargs):
        # type: (dict) -> CustomWebPlayerBuildDomain
        """List Domain Details

        :return: List of domain details
        :rtype: CustomWebPlayerBuildDomain
        """

        return self.api_client.get(
            '/player/custom-builds/web/domains',
            pagination_response=True,
            type=CustomWebPlayerBuildDomain,
            **kwargs
        )
