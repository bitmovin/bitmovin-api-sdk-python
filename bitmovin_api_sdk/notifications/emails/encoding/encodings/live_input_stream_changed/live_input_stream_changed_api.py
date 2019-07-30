# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.email_notification_with_stream_conditions import EmailNotificationWithStreamConditions
from bitmovin_api_sdk.models.email_notification_with_stream_conditions_request import EmailNotificationWithStreamConditionsRequest
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


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

    def create(self, email_notification_with_stream_conditions_request, **kwargs):
        # type: (EmailNotificationWithStreamConditionsRequest, dict) -> EmailNotificationWithStreamConditions
        """Add Live Input Stream Changed Email Notification (All Encodings)

        :param email_notification_with_stream_conditions_request: The email notifications object
        :type email_notification_with_stream_conditions_request: EmailNotificationWithStreamConditionsRequest, required
        :return: Notification Details
        :rtype: EmailNotificationWithStreamConditions
        """

        return self.api_client.post(
            '/notifications/emails/encoding/encodings/live-input-stream-changed',
            email_notification_with_stream_conditions_request,
            type=EmailNotificationWithStreamConditions,
            **kwargs
        )

    def create_by_encoding_id(self, encoding_id, email_notification_with_stream_conditions_request, **kwargs):
        # type: (string_types, EmailNotificationWithStreamConditionsRequest, dict) -> EmailNotificationWithStreamConditions
        """Add Live Input Stream Changed Email Notification (Specific Encoding)

        :param encoding_id: Id of the encoding resource
        :type encoding_id: string_types, required
        :param email_notification_with_stream_conditions_request: The email notifications object
        :type email_notification_with_stream_conditions_request: EmailNotificationWithStreamConditionsRequest, required
        :return: Notification Details
        :rtype: EmailNotificationWithStreamConditions
        """

        return self.api_client.post(
            '/notifications/emails/encoding/encodings/{encoding_id}/live-input-stream-changed',
            email_notification_with_stream_conditions_request,
            path_params={'encoding_id': encoding_id},
            type=EmailNotificationWithStreamConditions,
            **kwargs
        )

    def update(self, notification_id, email_notification_with_stream_conditions_request, **kwargs):
        # type: (string_types, EmailNotificationWithStreamConditionsRequest, dict) -> EmailNotificationWithStreamConditions
        """Replace Live Input Stream Changed Email Notification

        :param notification_id: Id of the email notification
        :type notification_id: string_types, required
        :param email_notification_with_stream_conditions_request: The email notification with the updated values
        :type email_notification_with_stream_conditions_request: EmailNotificationWithStreamConditionsRequest, required
        :return: Notification Details
        :rtype: EmailNotificationWithStreamConditions
        """

        return self.api_client.put(
            '/notifications/emails/encoding/encodings/live-input-stream-changed/{notification_id}',
            email_notification_with_stream_conditions_request,
            path_params={'notification_id': notification_id},
            type=EmailNotificationWithStreamConditions,
            **kwargs
        )
