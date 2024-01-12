# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.organization_pending_invitation import OrganizationPendingInvitation
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

    def list(self, organization_id, **kwargs):
        # type: (string_types, dict) -> OrganizationPendingInvitation
        """List all pending invitations of an org id

        :param organization_id: Id of the organization
        :type organization_id: string_types, required
        :return: List of pending invitations
        :rtype: OrganizationPendingInvitation
        """

        return self.api_client.get(
            '/account/organizations/{organization_id}/invitations',
            path_params={'organization_id': organization_id},
            pagination_response=True,
            type=OrganizationPendingInvitation,
            **kwargs
        )
