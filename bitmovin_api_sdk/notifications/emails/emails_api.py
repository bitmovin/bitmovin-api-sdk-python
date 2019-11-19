# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.notification import Notification
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.notifications.emails.usage_reports.usage_reports_api import UsageReportsApi
from bitmovin_api_sdk.notifications.emails.encoding.encoding_api import EncodingApi
from bitmovin_api_sdk.notifications.emails.notification_list_query_params import NotificationListQueryParams


class EmailsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EmailsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.usage_reports = UsageReportsApi(
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

    def list(self, query_params=None, **kwargs):
        # type: (NotificationListQueryParams, dict) -> Notification
        """List Email Notifications

        :param query_params: Query parameters
        :type query_params: NotificationListQueryParams
        :return: List of Notifications
        :rtype: Notification
        """

        return self.api_client.get(
            '/notifications/emails',
            query_params=query_params,
            pagination_response=True,
            type=Notification,
            **kwargs
        )
