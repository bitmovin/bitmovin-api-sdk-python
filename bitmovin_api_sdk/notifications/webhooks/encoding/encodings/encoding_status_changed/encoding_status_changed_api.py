# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.webhook_notification_with_stream_conditions import WebhookNotificationWithStreamConditions
from bitmovin_api_sdk.models.webhook_notification_with_stream_conditions_request import WebhookNotificationWithStreamConditionsRequest


class EncodingStatusChangedApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EncodingStatusChangedApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, webhook_notification_with_stream_conditions_request, **kwargs):
        # type: (WebhookNotificationWithStreamConditionsRequest, dict) -> WebhookNotificationWithStreamConditions
        """Add Encoding Changed Webhook Notification (All Encodings)

        :param webhook_notification_with_stream_conditions_request: The webhook notifications object. For conditions, following attributes are possible: &#39;type&#39;: &#39;Input file download&#39;, &#39;Input file analysis&#39;, &#39;Per-Title analysis&#39;, &#39;Encoding&#39;, &#39;Progressive Muxing&#39; &#39;progress&#39;: number in range of 0-100 &#39;status&#39;: &#39;RUNNING&#39;, &#39;FINISHED&#39;, &#39;ERROR&#39; Examples: To only get notified about the encoding process, create a Condition object and set attribute&#x3D;&#39;type&#39;, value&#x3D;&#39;Encoding&#39;, operator&#x3D;EQUAL To only get notified if a workflow step is finished, create a Condition object and set attribute&#x3D;&#39;status&#39;, value&#x3D;&#39;FINISHED&#39;, operator&#x3D;EQUAL To only get notified if a workflow step is over 50%,  create a Condition object and set attribute&#x3D;&#39;progress&#39;, value&#x3D;&#39;50&#39;, operator&#x3D;GREATER_THAN
        :type webhook_notification_with_stream_conditions_request: WebhookNotificationWithStreamConditionsRequest, required
        :return: Notification Details
        :rtype: WebhookNotificationWithStreamConditions
        """

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/encoding-status-changed',
            webhook_notification_with_stream_conditions_request,
            type=WebhookNotificationWithStreamConditions,
            **kwargs
        )

    def create_by_encoding_id(self, encoding_id, webhook_notification_with_stream_conditions_request, **kwargs):
        # type: (string_types, WebhookNotificationWithStreamConditionsRequest, dict) -> WebhookNotificationWithStreamConditions
        """Add Encoding Changed Webhook Notification (Specific Encoding)

        :param encoding_id: Id of the encoding resource
        :type encoding_id: string_types, required
        :param webhook_notification_with_stream_conditions_request: The webhook notifications object. For conditions, following attributes are possible: &#39;type&#39;: &#39;Input file download&#39;, &#39;Input file analysis&#39;, &#39;Per-Title analysis&#39;, &#39;Encoding&#39;, &#39;Progressive Muxing&#39; &#39;progress&#39;: number in range of 0-100 &#39;status&#39;: &#39;RUNNING&#39;, &#39;FINISHED&#39;, &#39;ERROR&#39; Examples: To only get notified about the encoding process, create a Condition object and set attribute&#x3D;&#39;type&#39;, value&#x3D;&#39;Encoding&#39;, operator&#x3D;EQUAL To only get notified if a workflow step is finished, create a Condition object and set attribute&#x3D;&#39;status&#39;, value&#x3D;&#39;FINISHED&#39;, operator&#x3D;EQUAL To only get notified if a workflow step is over 50%,  create a Condition object and set attribute&#x3D;&#39;progress&#39;, value&#x3D;&#39;50&#39;, operator&#x3D;GREATER_THAN 
        :type webhook_notification_with_stream_conditions_request: WebhookNotificationWithStreamConditionsRequest, required
        :return: Notification Details
        :rtype: WebhookNotificationWithStreamConditions
        """

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/encoding-status-changed',
            webhook_notification_with_stream_conditions_request,
            path_params={'encoding_id': encoding_id},
            type=WebhookNotificationWithStreamConditions,
            **kwargs
        )

    def delete_by_webhook_id(self, notification_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Encoding Status Changed Webhook

        :param notification_id: Id of the webhook
        :type notification_id: string_types, required
        :return: Id of the webhook
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/notifications/webhooks/encoding/encodings/encoding-status-changed/{notification_id}',
            path_params={'notification_id': notification_id},
            type=BitmovinResponse,
            **kwargs
        )

    def update(self, notification_id, webhook_notification_with_stream_conditions_request, **kwargs):
        # type: (string_types, WebhookNotificationWithStreamConditionsRequest, dict) -> WebhookNotificationWithStreamConditions
        """Replace Encoding Status Changed Webhook Notification

        :param notification_id: Id of the webhook notification
        :type notification_id: string_types, required
        :param webhook_notification_with_stream_conditions_request: The webhook notification with the updated values
        :type webhook_notification_with_stream_conditions_request: WebhookNotificationWithStreamConditionsRequest, required
        :return: Notification Details
        :rtype: WebhookNotificationWithStreamConditions
        """

        return self.api_client.put(
            '/notifications/webhooks/encoding/encodings/encoding-status-changed/{notification_id}',
            webhook_notification_with_stream_conditions_request,
            path_params={'notification_id': notification_id},
            type=WebhookNotificationWithStreamConditions,
            **kwargs
        )
