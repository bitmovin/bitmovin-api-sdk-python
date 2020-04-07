# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.webhook import Webhook
from bitmovin_api_sdk.notifications.webhooks.encoding.encodings.error.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.notifications.webhooks.encoding.encodings.error.webhook_list_query_params import WebhookListQueryParams
from bitmovin_api_sdk.notifications.webhooks.encoding.encodings.error.webhook_list_by_encoding_id_query_params import WebhookListByEncodingIdQueryParams


class ErrorApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ErrorApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, webhook, **kwargs):
        # type: (Webhook, dict) -> Webhook
        """Add Encoding Error Webhook

        :param webhook: The Encoding Error Webhook to be added. **Note:** A maximum number of 5 webhooks is allowed
        :type webhook: Webhook, required
        :return: Webhook Details
        :rtype: Webhook
        """

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/error',
            webhook,
            type=Webhook,
            **kwargs
        )

    def create_by_encoding_id(self, encoding_id, webhook, **kwargs):
        # type: (string_types, Webhook, dict) -> Webhook
        """Add Encoding Error Webhook for specific Encoding Resource. **Note:** A maximum number of 5 webhooks is allowed

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param webhook: The Encoding Error Webhook to be added
        :type webhook: Webhook, required
        :return: Webhook Details
        :rtype: Webhook
        """

        return self.api_client.post(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error',
            webhook,
            path_params={'encoding_id': encoding_id},
            type=Webhook,
            **kwargs
        )

    def delete_by_encoding_id_and_webhook_id(self, encoding_id, webhook_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Encoding Error Webhook for specific Encoding Resource

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param webhook_id: Id of the webhook
        :type webhook_id: string_types, required
        :return: Id of the webhook
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error/{webhook_id}',
            path_params={'encoding_id': encoding_id, 'webhook_id': webhook_id},
            type=BitmovinResponse,
            **kwargs
        )

    def delete_by_webhook_id(self, webhook_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Encoding Error Webhook

        :param webhook_id: Id of the webhook
        :type webhook_id: string_types, required
        :return: Id of the webhook
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/notifications/webhooks/encoding/encodings/error/{webhook_id}',
            path_params={'webhook_id': webhook_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get_by_encoding_id_and_webhook_id(self, encoding_id, webhook_id, **kwargs):
        # type: (string_types, string_types, dict) -> Webhook
        """Encoding Error Webhook Details for specific Encoding Resource

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param webhook_id: Id of the webhook
        :type webhook_id: string_types, required
        :return: Webhook Details
        :rtype: Webhook
        """

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error/{webhook_id}',
            path_params={'encoding_id': encoding_id, 'webhook_id': webhook_id},
            type=Webhook,
            **kwargs
        )

    def get_by_webhook_id(self, webhook_id, **kwargs):
        # type: (string_types, dict) -> Webhook
        """Encoding Error Webhook Details

        :param webhook_id: Id of the webhook
        :type webhook_id: string_types, required
        :return: Webhook Details
        :rtype: Webhook
        """

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/error/{webhook_id}',
            path_params={'webhook_id': webhook_id},
            type=Webhook,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (WebhookListQueryParams, dict) -> Webhook
        """List Encoding Error Webhooks

        :param query_params: Query parameters
        :type query_params: WebhookListQueryParams
        :return: List of Encoding Error Webhooks
        :rtype: Webhook
        """

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/error',
            query_params=query_params,
            pagination_response=True,
            type=Webhook,
            **kwargs
        )

    def list_by_encoding_id(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, WebhookListByEncodingIdQueryParams, dict) -> Webhook
        """List Encoding Error Webhooks for specific Encoding Resource

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: WebhookListByEncodingIdQueryParams
        :return: List of Encoding Error Webhooks
        :rtype: Webhook
        """

        return self.api_client.get(
            '/notifications/webhooks/encoding/encodings/{encoding_id}/error',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Webhook,
            **kwargs
        )
