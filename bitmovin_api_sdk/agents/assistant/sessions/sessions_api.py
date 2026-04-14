# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.agent_session_history_response import AgentSessionHistoryResponse
from bitmovin_api_sdk.models.agent_session_list_response import AgentSessionListResponse
from bitmovin_api_sdk.models.agent_session_response import AgentSessionResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class SessionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SessionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, **kwargs):
        # type: (dict) -> AgentSessionResponse
        """Create Agent Session

        :return: Created agent session
        :rtype: AgentSessionResponse
        """

        return self.api_client.post(
            '/agents/assistant/sessions',
            type=AgentSessionResponse,
            **kwargs
        )

    def delete(self, session_id, **kwargs):
        # type: (string_types, dict) -> AgentSessionResponse
        """Delete Agent Session

        :param session_id: Id of the session
        :type session_id: string_types, required
        :return: Deleted agent session
        :rtype: AgentSessionResponse
        """

        return self.api_client.delete(
            '/agents/assistant/sessions/{session_id}',
            path_params={'session_id': session_id},
            type=AgentSessionResponse,
            **kwargs
        )

    def get(self, session_id, **kwargs):
        # type: (string_types, dict) -> AgentSessionHistoryResponse
        """Get Agent Session Details

        :param session_id: Id of the session
        :type session_id: string_types, required
        :return: Agent session history
        :rtype: AgentSessionHistoryResponse
        """

        return self.api_client.get(
            '/agents/assistant/sessions/{session_id}',
            path_params={'session_id': session_id},
            type=AgentSessionHistoryResponse,
            **kwargs
        )

    def list(self, **kwargs):
        # type: (dict) -> AgentSessionListResponse
        """List Agent Sessions

        :return: Agent sessions list
        :rtype: AgentSessionListResponse
        """

        return self.api_client.get(
            '/agents/assistant/sessions',
            type=AgentSessionListResponse,
            **kwargs
        )
