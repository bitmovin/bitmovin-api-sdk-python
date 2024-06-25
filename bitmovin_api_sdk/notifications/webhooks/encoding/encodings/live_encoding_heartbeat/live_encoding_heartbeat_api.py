# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.live_encoding_heartbeat_webhook import LiveEncodingHeartbeatWebhook
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.notifications.webhooks.encoding.encodings.live_encoding_heartbeat.live_encoding_heartbeat_webhook_list_query_params import LiveEncodingHeartbeatWebhookListQueryParams


class LiveEncodingHeartbeatApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LiveEncodingHeartbeatApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, live_encoding_heartbeat_webhook, **kwargs):
        # type: (LiveEncodingHeartbeatWebhook, dict) -> LiveEncodingHeartbeatWebhook
        """Add &#39;Live Encoding Heartbeat&#39; Webhook

        :param live_encoding_heartbeat_webhook: The &#39;Live Encoding Heartbeat&#39; Webhook to be added.
        :type live_encoding_heartbeat_webhook: LiveEncodingHeartbeatWebhook, required
        :return: Webhook Details
        :rtype: LiveEncodingHeartbeatWebhook
        """

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/live-encoding-heartbeat',
            live_encoding_heartbeat_webhook,
            type=LiveEncodingHeartbeatWebhook,
            **kwargs
        )

    def delete_by_webhook_id(self, webhook_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete &#39;Live Encoding Heartbeat&#39; Webhook

        :param webhook_id: Id of the webhook
        :type webhook_id: string_types, required
        :return: Id of the webhook
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/notifications/webhooks/encoding/encodings/live-encoding-heartbeat/{webhook_id}',
            path_params={'webhook_id': webhook_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get_by_webhook_id(self, webhook_id, **kwargs):
        # type: (string_types, dict) -> LiveEncodingHeartbeatWebhook
        """&#39;Live Encoding Heartbeat&#39; Webhook Details

        :param webhook_id: Id of the webhook
        :type webhook_id: string_types, required
        :return: Webhook Details
        :rtype: LiveEncodingHeartbeatWebhook
        """

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/live-encoding-heartbeat/{webhook_id}',
            path_params={'webhook_id': webhook_id},
            type=LiveEncodingHeartbeatWebhook,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (LiveEncodingHeartbeatWebhookListQueryParams, dict) -> LiveEncodingHeartbeatWebhook
        """List &#39;Live Encoding Heartbeat&#39; Webhooks

        :param query_params: Query parameters
        :type query_params: LiveEncodingHeartbeatWebhookListQueryParams
        :return: List of 'Live Encoding Heartbeat' Webhooks
        :rtype: LiveEncodingHeartbeatWebhook
        """

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/live-encoding-heartbeat',
            query_params=query_params,
            pagination_response=True,
            type=LiveEncodingHeartbeatWebhook,
            **kwargs
        )
