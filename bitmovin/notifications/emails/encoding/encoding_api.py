# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.email_notification import EmailNotification
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.notifications.emails.encoding.encodings.encodings_api import EncodingsApi
from bitmovin.notifications.emails.encoding.email_notification_list_query_params import EmailNotificationListQueryParams


class EncodingApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
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

    def list(self, query_params: EmailNotificationListQueryParams = None, **kwargs):
        """List Email Notifications (All Encodings)"""

        return self.api_client.get(
            '/notifications/emails/encoding',
            query_params=query_params,
            pagination_response=True,
            type=EmailNotification,
            **kwargs
        )
