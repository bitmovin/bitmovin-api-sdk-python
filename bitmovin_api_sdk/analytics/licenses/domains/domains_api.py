# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.domain import Domain
from bitmovin_api_sdk.models.domain_list import DomainList
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

    def create(self, license_id, domain, **kwargs):
        # type: (string_types, Domain, dict) -> Domain
        """Add Domain

        :param license_id: License id
        :type license_id: string_types, required
        :param domain: The domain to be added
        :type domain: Domain, required
        :return: Id of the domain
        :rtype: Domain
        """

        return self.api_client.post(
            '/analytics/licenses/{license_id}/domains',
            domain,
            path_params={'license_id': license_id},
            type=Domain,
            **kwargs
        )

    def delete(self, license_id, domain_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Domain

        :param license_id: License id
        :type license_id: string_types, required
        :param domain_id: id of domain to delete
        :type domain_id: string_types, required
        :return: id of deleted domain
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/analytics/licenses/{license_id}/domains/{domain_id}',
            path_params={'license_id': license_id, 'domain_id': domain_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, license_id, **kwargs):
        # type: (string_types, dict) -> DomainList
        """List License Domains

        :param license_id: License id
        :type license_id: string_types, required
        :return:
        :rtype: DomainList
        """

        return self.api_client.get(
            '/analytics/licenses/{license_id}/domains',
            path_params={'license_id': license_id},
            type=DomainList,
            **kwargs
        )
