# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.webhook import Webhook


class ErrorApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ErrorApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, webhook, **kwargs):
        """Add Manifest Error Webhook (All Manifests)"""

        return self.api_client.post(
            '/notifications/webhooks/encoding/manifest/error',
            webhook,
            pagination_response=True,
            type=Webhook,
            **kwargs
        )

    def createByManifestId(self, manifest_id, webhook, **kwargs):
        """Add Manifest Error Webhook Notification (Specific Manifest)"""

        return self.api_client.post(
            '/notifications/webhooks/encoding/manifest/{manifest_id}/error',
            webhook,
            path_params={'manifest_id': manifest_id},
            type=Webhook,
            **kwargs
        )

    def update(self, notification_id, webhook, **kwargs):
        """Replace Manifest Error Webhook Notification"""

        return self.api_client.put(
            '/notifications/webhooks/encoding/manifest/error/{notification_id}',
            webhook,
            path_params={'notification_id': notification_id},
            type=Webhook,
            **kwargs
        )
