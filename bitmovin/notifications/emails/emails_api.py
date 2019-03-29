# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.notification import Notification
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.notifications.emails.encoding.encoding_api import EncodingApi
from bitmovin.notifications.emails.notification_list_query_params import NotificationListQueryParams


class EmailsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(EmailsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.encoding = EncodingApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: NotificationListQueryParams = None, **kwargs):
        """List Email Notifications"""

        return self.api_client.get(
            '/notifications/emails',
            query_params=query_params,
            pagination_response=True,
            type=Notification,
            **kwargs
        )
