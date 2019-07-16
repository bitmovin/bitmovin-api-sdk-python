# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.email_notification import EmailNotification
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.notifications.emails.encoding.encodings.encodings_api import EncodingsApi
from bitmovin_api_sdk.notifications.emails.encoding.email_notification_list_query_params import EmailNotificationListQueryParams


class EncodingApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EncodingApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.encodings = EncodingsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params=None, **kwargs):
        # type: (EmailNotificationListQueryParams, dict) -> EmailNotification
        """List Email Notifications (All Encodings)

        :param query_params: Query parameters
        :type query_params: EmailNotificationListQueryParams
        :return: List of Notifications
        :rtype: EmailNotification
        """

        return self.api_client.get(
            '/notifications/emails/encoding',
            query_params=query_params,
            pagination_response=True,
            type=EmailNotification,
            **kwargs
        )
