# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.tenant import Tenant


class TenantsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TenantsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, organization_id, group_id, tenant, **kwargs):
        """Add Tenant to Group"""

        return self.api_client.post(
            '/account/organizations/{organization_id}/groups/{group_id}/tenants',
            tenant,
            path_params={'organization_id': organization_id, 'group_id': group_id},
            type=Tenant,
            **kwargs
        )

    def delete(self, organization_id, group_id, tenant_id, **kwargs):
        """Delete Tenant"""

        return self.api_client.delete(
            '/account/organizations/{organization_id}/groups/{group_id}/tenants/{tenant_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id, 'tenant_id': tenant_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, organization_id, group_id, tenant_id, **kwargs):
        """Tenant Details"""

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}/tenants/{tenant_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id, 'tenant_id': tenant_id},
            type=Tenant,
            **kwargs
        )

    def list(self, organization_id, group_id, **kwargs):
        """List Tenants"""

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}/tenants',
            path_params={'organization_id': organization_id, 'group_id': group_id},
            pagination_response=True,
            type=Tenant,
            **kwargs
        )
