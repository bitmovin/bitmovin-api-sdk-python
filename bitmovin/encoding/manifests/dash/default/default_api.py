# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.dash_manifest_default import DashManifestDefault
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class DefaultApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DefaultApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, dash_manifest_default, **kwargs):
        """Create DASH Manifest Default"""

        return self.api_client.post(
            '/encoding/manifests/dash/default',
            dash_manifest_default,
            type=DashManifestDefault,
            **kwargs
        )
