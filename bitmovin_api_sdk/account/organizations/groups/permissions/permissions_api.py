# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.acl import Acl
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class PermissionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PermissionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, organization_id, group_id, acl, **kwargs):
        # type: (string_types, string_types, Acl, dict) -> Acl
        """Set Group Permissions

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :param acl: Group Permissions
        :type acl: Acl, required
        :return: Tenant details
        :rtype: Acl
        """

        return self.api_client.post(
            '/account/organizations/{organization_id}/groups/{group_id}/permissions',
            acl,
            path_params={'organization_id': organization_id, 'group_id': group_id},
            type=Acl,
            **kwargs
        )

    def delete(self, organization_id, group_id, permission_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Permission

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :param permission_id: Id of the permission
        :type permission_id: string_types, required
        :return:
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/account/organizations/{organization_id}/groups/{group_id}/permissions/{permission_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id, 'permission_id': permission_id},
            type=BitmovinResponse,
            **kwargs
        )

    def list(self, organization_id, group_id, **kwargs):
        # type: (string_types, string_types, dict) -> Acl
        """Get Group Permissions

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :return: Service specific result
        :rtype: Acl
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}/permissions',
            path_params={'organization_id': organization_id, 'group_id': group_id},
            pagination_response=True,
            type=Acl,
            **kwargs
        )
