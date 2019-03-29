# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.smooth_manifest_default import SmoothManifestDefault


class DefaultApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DefaultApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, smooth_manifest_default, **kwargs):
        """Create Smooth Streaming Manifest Default"""

        return self.api_client.post(
            '/encoding/manifests/smooth/default',
            smooth_manifest_default,
            type=SmoothManifestDefault,
            **kwargs
        )
