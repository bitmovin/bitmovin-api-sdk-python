# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.enhanced_watermark_filter import EnhancedWatermarkFilter
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.filters.enhancedWatermark.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.filters.enhancedWatermark.enhanced_watermark_filter_list_query_params import EnhancedWatermarkFilterListQueryParams


class EnhancedWatermarkApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(EnhancedWatermarkApi, self).__init__(
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

    def create(self, enhanced_watermark_filter, **kwargs):
        """Create Enhanced Watermark Filter"""

        return self.api_client.post(
            '/encoding/filters/enhanced-watermark',
            enhanced_watermark_filter,
            type=EnhancedWatermarkFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        """Delete Enhanced Watermark Filter"""

        return self.api_client.delete(
            '/encoding/filters/enhanced-watermark/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        """Enhanced Watermark Filter Details"""

        return self.api_client.get(
            '/encoding/filters/enhanced-watermark/{filter_id}',
            path_params={'filter_id': filter_id},
            type=EnhancedWatermarkFilter,
            **kwargs
        )

    def list(self, query_params: EnhancedWatermarkFilterListQueryParams = None, **kwargs):
        """List Enhanced Watermark Filters"""

        return self.api_client.get(
            '/encoding/filters/enhanced-watermark',
            query_params=query_params,
            pagination_response=True,
            type=EnhancedWatermarkFilter,
            **kwargs
        )
