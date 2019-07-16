# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.notification import Notification
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.notifications.webhooks.encoding.manifest.error.error_api import ErrorApi
from bitmovin_api_sdk.notifications.webhooks.encoding.manifest.finished.finished_api import FinishedApi
from bitmovin_api_sdk.notifications.webhooks.encoding.manifest.notification_list_query_params import NotificationListQueryParams


class ManifestApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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

    def list(self, manifest_id, query_params=None, **kwargs):
        # type: (string_types, NotificationListQueryParams, dict) -> Notification
        """List Webhook Notifications (Specific Manifest)

        :param manifest_id: Id of the manifest resource
        :type manifest_id: string_types, required
        :param query_params: Query parameters
        :type query_params: NotificationListQueryParams
        :return: List of Webhook Notifications
        :rtype: Notification
        """

        return self.api_client.get(
            '/notifications/webhooks/encoding/manifest/{manifest_id}',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=Notification,
            **kwargs
        )
