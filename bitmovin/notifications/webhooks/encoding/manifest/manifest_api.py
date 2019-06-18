# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.notification import Notification
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.notifications.webhooks.encoding.manifest.error.error_api import ErrorApi
from bitmovin.notifications.webhooks.encoding.manifest.finished.finished_api import FinishedApi
from bitmovin.notifications.webhooks.encoding.manifest.notification_list_query_params import NotificationListQueryParams


class ManifestApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ManifestApi, self).__init__(
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

        self.finished = FinishedApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, manifest_id, query_params: NotificationListQueryParams = None, **kwargs):
        """List Webhook Notifications (Specific Manifest)"""

        return self.api_client.get(
            '/notifications/webhooks/encoding/manifest/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=Notification,
            **kwargs
        )
