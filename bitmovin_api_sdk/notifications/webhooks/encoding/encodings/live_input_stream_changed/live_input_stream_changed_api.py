# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.webhook_notification_with_stream_conditions import WebhookNotificationWithStreamConditions
from bitmovin_api_sdk.models.webhook_notification_with_stream_conditions_request import WebhookNotificationWithStreamConditionsRequest


class LiveInputStreamChangedApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LiveInputStreamChangedApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, webhook_notification_with_stream_conditions_request, **kwargs):
        # type: (WebhookNotificationWithStreamConditionsRequest, dict) -> WebhookNotificationWithStreamConditions
        """Add Live Input Stream Changed Webhook Notification (All Encodings)

        :param webhook_notification_with_stream_conditions_request: The webhook notifications object
        :type webhook_notification_with_stream_conditions_request: WebhookNotificationWithStreamConditionsRequest, required
        :return: Notification Details
        :rtype: WebhookNotificationWithStreamConditions
        """

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/live-input-stream-changed',
            webhook_notification_with_stream_conditions_request,
            type=WebhookNotificationWithStreamConditions,
            **kwargs
        )

    def create_by_encoding_id(self, encoding_id, webhook_notification_with_stream_conditions_request, **kwargs):
        # type: (string_types, WebhookNotificationWithStreamConditionsRequest, dict) -> WebhookNotificationWithStreamConditions
        """Add Live Input Stream Changed Webhook Notification (Specific Encoding)

        :param encoding_id: Id of the encoding resource
        :type encoding_id: string_types, required
        :param webhook_notification_with_stream_conditions_request: The webhook notifications object
        :type webhook_notification_with_stream_conditions_request: WebhookNotificationWithStreamConditionsRequest, required
        :return: Notification Details
        :rtype: WebhookNotificationWithStreamConditions
        """

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/live-input-stream-changed',
            webhook_notification_with_stream_conditions_request,
            path_params={'encoding_id': encoding_id},
            type=WebhookNotificationWithStreamConditions,
            **kwargs
        )

    def update(self, notification_id, webhook_notification_with_stream_conditions_request, **kwargs):
        # type: (string_types, WebhookNotificationWithStreamConditionsRequest, dict) -> WebhookNotificationWithStreamConditions
        """Replace Live Input Stream Changed Webhook Notification

        :param notification_id: Id of the webhook notification
        :type notification_id: string_types, required
        :param webhook_notification_with_stream_conditions_request: The webhook notification with the updated values
        :type webhook_notification_with_stream_conditions_request: WebhookNotificationWithStreamConditionsRequest, required
        :return: Notification Details
        :rtype: WebhookNotificationWithStreamConditions
        """

        return self.api_client.put(
            '/notifications/webhooks/encoding/encodings/live-input-stream-changed/{notification_id}',
            webhook_notification_with_stream_conditions_request,
            path_params={'notification_id': notification_id},
            type=WebhookNotificationWithStreamConditions,
            **kwargs
        )
