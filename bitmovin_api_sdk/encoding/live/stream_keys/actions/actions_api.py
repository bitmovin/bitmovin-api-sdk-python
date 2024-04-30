# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.stream_keys_unassign_action import StreamKeysUnassignAction


class ActionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ActionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def unassign(self, stream_keys_unassign_action, **kwargs):
        # type: (StreamKeysUnassignAction, dict) -> StreamKeysUnassignAction
        """Unassign stream keys

        :param stream_keys_unassign_action: The action payload for unassigning stream keys
        :type stream_keys_unassign_action: StreamKeysUnassignAction, required
        :return: Stream key
        :rtype: StreamKeysUnassignAction
        """

        return self.api_client.post(
            '/encoding/live/stream-keys/actions/unassign',
            stream_keys_unassign_action,
            type=StreamKeysUnassignAction,
            **kwargs
        )
