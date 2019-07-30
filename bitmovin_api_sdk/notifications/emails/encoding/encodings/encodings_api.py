# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.email_notification_with_stream_conditions import EmailNotificationWithStreamConditions
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.notifications.emails.encoding.encodings.live_input_stream_changed.live_input_stream_changed_api import LiveInputStreamChangedApi
from bitmovin_api_sdk.notifications.emails.encoding.encodings.error.error_api import ErrorApi
from bitmovin_api_sdk.notifications.emails.encoding.encodings.email_notification_with_stream_conditions_list_query_params import EmailNotificationWithStreamConditionsListQueryParams


class EncodingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EncodingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.live_input_stream_changed = LiveInputStreamChangedApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.error = ErrorApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, EmailNotificationWithStreamConditionsListQueryParams, dict) -> EmailNotificationWithStreamConditions
        """List Email Notifications (Specific Encoding)

        :param encoding_id: Id of the encoding resource
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: EmailNotificationWithStreamConditionsListQueryParams
        :return: List of Email Notifications
        :rtype: EmailNotificationWithStreamConditions
        """

        return self.api_client.get(
            '/notifications/emails/encoding/encodings/{encoding_id}',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=EmailNotificationWithStreamConditions,
            **kwargs
        )
