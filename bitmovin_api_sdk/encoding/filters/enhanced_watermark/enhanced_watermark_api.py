# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.enhanced_watermark_filter import EnhancedWatermarkFilter
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.enhanced_watermark.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.enhanced_watermark.enhanced_watermark_filter_list_query_params import EnhancedWatermarkFilterListQueryParams


class EnhancedWatermarkApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (EnhancedWatermarkFilter, dict) -> EnhancedWatermarkFilter
        """Create Enhanced Watermark Filter

        :param enhanced_watermark_filter: The Enhanced Watermark Filter to be created. Only one horizontal and one vertical distance parameter is allowed, either top or bottom, and either left or right. See example body.
        :type enhanced_watermark_filter: EnhancedWatermarkFilter, required
        :return: Enhanced Watermark details
        :rtype: EnhancedWatermarkFilter
        """

        return self.api_client.post(
            '/encoding/filters/enhanced-watermark',
            enhanced_watermark_filter,
            type=EnhancedWatermarkFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Enhanced Watermark Filter

        :param filter_id: Id of the enhanced watermark configuration.
        :type filter_id: string_types, required
        :return: Id of the enhanced watermark.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/enhanced-watermark/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> EnhancedWatermarkFilter
        """Enhanced Watermark Filter Details

        :param filter_id: Id of the enhanced watermark configuration.
        :type filter_id: string_types, required
        :return: Enhanced Watermark details
        :rtype: EnhancedWatermarkFilter
        """

        return self.api_client.get(
            '/encoding/filters/enhanced-watermark/{filter_id}',
            path_params={'filter_id': filter_id},
            type=EnhancedWatermarkFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (EnhancedWatermarkFilterListQueryParams, dict) -> EnhancedWatermarkFilter
        """List Enhanced Watermark Filters

        :param query_params: Query parameters
        :type query_params: EnhancedWatermarkFilterListQueryParams
        :return: List of watermark ids
        :rtype: EnhancedWatermarkFilter
        """

        return self.api_client.get(
            '/encoding/filters/enhanced-watermark',
            query_params=query_params,
            pagination_response=True,
            type=EnhancedWatermarkFilter,
            **kwargs
        )
