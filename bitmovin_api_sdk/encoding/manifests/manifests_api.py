# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.manifest import Manifest
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.type.type_api import TypeApi
from bitmovin_api_sdk.encoding.manifests.dash.dash_api import DashApi
from bitmovin_api_sdk.encoding.manifests.hls.hls_api import HlsApi
from bitmovin_api_sdk.encoding.manifests.smooth.smooth_api import SmoothApi
from bitmovin_api_sdk.encoding.manifests.manifest_list_query_params import ManifestListQueryParams


class ManifestsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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

    def list(self, query_params=None, **kwargs):
        # type: (ManifestListQueryParams, dict) -> Manifest
        """List all Manifests

        :param query_params: Query parameters
        :type query_params: ManifestListQueryParams
        :return: All manifests with type information
        :rtype: Manifest
        """

        return self.api_client.get(
            '/encoding/manifests',
            query_params=query_params,
            pagination_response=True,
            type=Manifest,
            **kwargs
        )
