# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.invitation import Invitation
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


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

    def list(self, organization_id, group_id, **kwargs):
        # type: (string_types, string_types, dict) -> Invitation
        """List Invitations

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :param group_id: Id of the group
        :type group_id: string_types, required
        :return: List of invitations
        :rtype: Invitation
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}/groups/{group_id}/invitations',
            path_params={'organization_id': organization_id, 'group_id': group_id},
            pagination_response=True,
            type=Invitation,
            **kwargs
        )
