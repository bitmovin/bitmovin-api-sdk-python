# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.organization import Organization
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class SubOrganizationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SubOrganizationsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, organization_id, **kwargs):
        # type: (string_types, dict) -> Organization
        """Organizations under given parent organization

        :param organization_id: ID of the parent organization
        :type organization_id: string_types, required
        :return: Sub-Organizations
        :rtype: Organization
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}/sub-organizations',
            path_params={'organization_id': organization_id},
            pagination_response=True,
            type=Organization,
            **kwargs
        )
