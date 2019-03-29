# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.hls_manifest_default import HlsManifestDefault
from bitmovin.models.response_envelope import ResponseEnvelope


class DefaultApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DefaultApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, hls_manifest_default, **kwargs):
        """Create HLS Manifest Default"""

        return self.api_client.post(
            '/encoding/manifests/hls/default',
            hls_manifest_default,
            type=HlsManifestDefault,
            **kwargs
        )
