# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.unsharp_filter import UnsharpFilter
from bitmovin.encoding.filters.unsharp.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.filters.unsharp.unsharp_filter_list_query_params import UnsharpFilterListQueryParams


class UnsharpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(UnsharpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, unsharp_filter, **kwargs):
        """Create Unsharp Filter"""

        return self.api_client.post(
            '/encoding/filters/unsharp',
            unsharp_filter,
            type=UnsharpFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Unsharp Filter"""

        return self.api_client.delete(
            '/encoding/filters/unsharp/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Unsharp Filter Details"""

        return self.api_client.get(
            '/encoding/filters/unsharp/{filter_id}',
            path_params={'filter_id': filter_id},
            type=UnsharpFilter,
            **kwargs
        )

    def list(self, query_params: UnsharpFilterListQueryParams = None, **kwargs):
        """List Unsharp Filters"""

        return self.api_client.get(
            '/encoding/filters/unsharp',
            query_params=query_params,
            pagination_response=True,
            type=UnsharpFilter,
            **kwargs
        )
