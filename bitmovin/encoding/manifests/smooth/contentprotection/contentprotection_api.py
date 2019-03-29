# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.smooth_manifest_content_protection import SmoothManifestContentProtection
from bitmovin.encoding.manifests.smooth.contentprotection.smooth_manifest_content_protection_list_query_params import SmoothManifestContentProtectionListQueryParams


class ContentprotectionApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ContentprotectionApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, smooth_manifest_content_protection, **kwargs):
        """Add Content Protection to Smooth Streaming"""

        return self.api_client.post(
            '/encoding/manifests/smooth/{manifest_id}/contentprotection',
            smooth_manifest_content_protection,
            path_params={'manifest_id': manifest_id},
            type=SmoothManifestContentProtection,
            **kwargs
        )

    def delete(self, manifest_id, protection_id, **kwargs):
        """Delete Content Protection of Smooth Streaming"""

        return self.api_client.delete(
            '/encoding/manifests/smooth/{manifest_id}/contentprotection/{protection_id}',
            path_params={'manifest_id': manifest_id, 'protection_id': protection_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, protection_id, **kwargs):
        """Content Protection of Smooth Streaming Representation Details"""

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/contentprotection/{protection_id}',
            path_params={'manifest_id': manifest_id, 'protection_id': protection_id},
            type=SmoothManifestContentProtection,
            **kwargs
        )

    def list(self, manifest_id, query_params: SmoothManifestContentProtectionListQueryParams = None, **kwargs):
        """List Content Protection of Smooth Streaming"""

        return self.api_client.get(
            '/encoding/manifests/smooth/{manifest_id}/contentprotection',
            path_params={'manifest_id': manifest_id},
            query_params=query_params,
            pagination_response=True,
            type=SmoothManifestContentProtection,
            **kwargs
        )
