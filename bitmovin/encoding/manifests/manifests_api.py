# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.manifest import Manifest
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.manifests.type.type_api import TypeApi
from bitmovin.encoding.manifests.dash.dash_api import DashApi
from bitmovin.encoding.manifests.hls.hls_api import HlsApi
from bitmovin.encoding.manifests.smooth.smooth_api import SmoothApi
from bitmovin.encoding.manifests.manifest_list_query_params import ManifestListQueryParams


class ManifestsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ManifestsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.type = TypeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.dash = DashApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.hls = HlsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.smooth = SmoothApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: ManifestListQueryParams = None, **kwargs):
        """List all Manifests"""

        return self.api_client.get(
            '/encoding/manifests',
            query_params=query_params,
            pagination_response=True,
            type=Manifest,
            **kwargs
        )
