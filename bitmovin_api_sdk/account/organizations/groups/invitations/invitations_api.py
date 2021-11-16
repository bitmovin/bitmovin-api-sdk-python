# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.invitation import Invitation
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.account.organizations.groups.invitations.invitation_list_query_params import InvitationListQueryParams


class InvitationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(InvitationsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, organization_id, group_id, invitation, **kwargs):
        # type: (string_types, string_types, Invitation, dict) -> Invitation
        """Add Invitation to Group

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :param invitation: Invitation details
        :type invitation: Invitation, required
        :return: Invitation details
        :rtype: Invitation
        """

        return self.api_client.post(
            '/account/organizations/{organization_id}/groups/{group_id}/invitations',
            invitation,
            path_params={'organization_id': organization_id, 'group_id': group_id},
            type=Invitation,
            **kwargs
        )

    def delete(self, organization_id, group_id, invitation_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Invitation

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :param invitation_id: Id of the invitation.
        :type invitation_id: string_types, required
        :return: Id of the group
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/account/organizations/{organization_id}/groups/{group_id}/invitations/{invitation_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id, 'invitation_id': invitation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, organization_id, group_id, invitation_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> Invitation
        """Invitation Details

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :param invitation_id: Id of the invitation.
        :type invitation_id: string_types, required
        :return: Invitation details
        :rtype: Invitation
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}/invitations/{invitation_id}',
            path_params={'organization_id': organization_id, 'group_id': group_id, 'invitation_id': invitation_id},
            type=Invitation,
            **kwargs
        )

    def list(self, organization_id, group_id, query_params=None, **kwargs):
        # type: (string_types, string_types, InvitationListQueryParams, dict) -> Invitation
        """List Invitations

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :param query_params: Query parameters
        :type query_params: InvitationListQueryParams
        :return: List of invitations
        :rtype: Invitation
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}/invitations',
            path_params={'organization_id': organization_id, 'group_id': group_id},
            query_params=query_params,
            pagination_response=True,
            type=Invitation,
            **kwargs
        )
