# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.email_notification import EmailNotification
from bitmovin_api_sdk.models.encoding_error_email_notification import EncodingErrorEmailNotification
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


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

    def create(self, encoding_error_email_notification, **kwargs):
        # type: (EncodingErrorEmailNotification, dict) -> EncodingErrorEmailNotification
        """Add Encoding Error Email Notification (All Encodings)

        :param encoding_error_email_notification: Add a new email notification if an encoding received an error
        :type encoding_error_email_notification: EncodingErrorEmailNotification, required
        :return: Notification Details
        :rtype: EncodingErrorEmailNotification
        """

        return self.api_client.post(
            '/notifications/emails/encoding/encodings/error',
            encoding_error_email_notification,
            pagination_response=True,
            type=EncodingErrorEmailNotification,
            **kwargs
        )

    def create_by_encoding_id(self, encoding_id, email_notification, **kwargs):
        # type: (string_types, EmailNotification, dict) -> EmailNotification
        """Add Encoding Error Email Notification (Specific Encoding)

        :param encoding_id: Id of the encoding resource
        :type encoding_id: string_types, required
        :param email_notification: The email notifications object
        :type email_notification: EmailNotification, required
        :return: Notification Details
        :rtype: EmailNotification
        """

        return self.api_client.post(
            '/notifications/emails/encoding/encodings/{encoding_id}/error',
            email_notification,
            path_params={'encoding_id': encoding_id},
            type=EmailNotification,
            **kwargs
        )

    def update(self, notification_id, email_notification, **kwargs):
        # type: (string_types, EmailNotification, dict) -> EmailNotification
        """Replace Encoding Error Email Notification

        :param notification_id: Id of the email notification
        :type notification_id: string_types, required
        :param email_notification: The email notification with the updated values
        :type email_notification: EmailNotification, required
        :return: Notification Details
        :rtype: EmailNotification
        """

        return self.api_client.put(
            '/notifications/emails/encoding/encodings/error/{notification_id}',
            email_notification,
            path_params={'notification_id': notification_id},
            type=EmailNotification,
            **kwargs
        )
