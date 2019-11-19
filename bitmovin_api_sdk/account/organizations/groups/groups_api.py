# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.group import Group
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.account.organizations.groups.tenants.tenants_api import TenantsApi
from bitmovin_api_sdk.account.organizations.groups.invitations.invitations_api import InvitationsApi
from bitmovin_api_sdk.account.organizations.groups.permissions.permissions_api import PermissionsApi


class GroupsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(GroupsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.tenants = TenantsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.invitations = InvitationsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.permissions = PermissionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, organization_id, group, **kwargs):
        # type: (string_types, Group, dict) -> Group
        """Add Group

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group: Tenant Group details
        :type group: Group, required
        :return: Tenatn Group details
        :rtype: Group
        """

        return self.api_client.post(
            '/account/organizations/{organization_id}/groups',
            group,
            path_params={'organization_id': organization_id},
            type=Group,
            **kwargs
        )

    def delete(self, organization_id, group_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Group

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :return: Id of the group
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/account/organizations/{organization_id}/groups/{group_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, organization_id, group_id, **kwargs):
        # type: (string_types, string_types, dict) -> Group
        """Group Details

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group.
        :type group_id: string_types, required
        :return: Encoding transer details
        :rtype: Group
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id},
            type=Group,
            **kwargs
        )

    def list(self, organization_id, **kwargs):
        # type: (string_types, dict) -> Group
        """List Groups

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :return: Service specific result
        :rtype: Group
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups',
            path_params={'organization_id': organization_id},
            pagination_response=True,
            type=Group,
            **kwargs
        )
