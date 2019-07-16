# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.tenant import Tenant


class TenantsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TenantsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, organization_id, group_id, tenant, **kwargs):
        # type: (string_types, string_types, Tenant, dict) -> Tenant
        """Add Tenant to Group

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :param tenant: Tenant details
        :type tenant: Tenant, required
        :return: Tenant details
        :rtype: Tenant
        """

        return self.api_client.post(
            '/account/organizations/{organization_id}/groups/{group_id}/tenants',
            tenant,
            path_params={'organization_id': organization_id, 'group_id': group_id},
            type=Tenant,
            **kwargs
        )

    def delete(self, organization_id, group_id, tenant_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Tenant

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :param tenant_id: Id of the tenant.
        :type tenant_id: string_types, required
        :return: Id of the group
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/account/organizations/{organization_id}/groups/{group_id}/tenants/{tenant_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id, 'tenant_id': tenant_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, organization_id, group_id, tenant_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> Tenant
        """Tenant Details

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :param tenant_id: Id of the tenant.
        :type tenant_id: string_types, required
        :return: Tenant details
        :rtype: Tenant
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}/tenants/{tenant_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id, 'tenant_id': tenant_id},
            type=Tenant,
            **kwargs
        )

    def list(self, organization_id, group_id, **kwargs):
        # type: (string_types, string_types, dict) -> Tenant
        """List Tenants

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :return: Service specific result
        :rtype: Tenant
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}/tenants',
            path_params={'organization_id': organization_id, 'group_id': group_id},
            pagination_response=True,
            type=Tenant,
            **kwargs
        )
