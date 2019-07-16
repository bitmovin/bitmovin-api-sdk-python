# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.watermark_filter import WatermarkFilter
from bitmovin_api_sdk.encoding.filters.watermark.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.watermark.watermark_filter_list_query_params import WatermarkFilterListQueryParams


class WatermarkApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(WatermarkApi, self).__init__(
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

    def create(self, watermark_filter, **kwargs):
        # type: (WatermarkFilter, dict) -> WatermarkFilter
        """Create Watermark Filter

        :param watermark_filter: The Watermark Filter to be created. Only one horizontal and one vertical distance parameter is allowed, either top or bottom, and either left or right. See example body.
        :type watermark_filter: WatermarkFilter, required
        :return: Watermark details
        :rtype: WatermarkFilter
        """

        return self.api_client.post(
            '/encoding/filters/watermark',
            watermark_filter,
            type=WatermarkFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Watermark Filter

        :param filter_id: Id of the watermark configuration.
        :type filter_id: string_types, required
        :return: Id of the watermark.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/watermark/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> WatermarkFilter
        """Watermark Filter Details

        :param filter_id: Id of the watermark configuration.
        :type filter_id: string_types, required
        :return: Watermark details
        :rtype: WatermarkFilter
        """

        return self.api_client.get(
            '/encoding/filters/watermark/{filter_id}',
            path_params={'filter_id': filter_id},
            type=WatermarkFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (WatermarkFilterListQueryParams, dict) -> WatermarkFilter
        """List Watermark Filters

        :param query_params: Query parameters
        :type query_params: WatermarkFilterListQueryParams
        :return: List of watermark ids
        :rtype: WatermarkFilter
        """

        return self.api_client.get(
            '/encoding/filters/watermark',
            query_params=query_params,
            pagination_response=True,
            type=WatermarkFilter,
            **kwargs
        )
