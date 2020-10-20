# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.enhanced_deinterlace_filter import EnhancedDeinterlaceFilter
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.enhanced_deinterlace.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.enhanced_deinterlace.enhanced_deinterlace_filter_list_query_params import EnhancedDeinterlaceFilterListQueryParams


class EnhancedDeinterlaceApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EnhancedDeinterlaceApi, self).__init__(
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

    def create(self, enhanced_deinterlace_filter, **kwargs):
        # type: (EnhancedDeinterlaceFilter, dict) -> EnhancedDeinterlaceFilter
        """Create Enhanced Deinterlace Filter

        :param enhanced_deinterlace_filter: The Enhanced Deinterlace Filter to be created
        :type enhanced_deinterlace_filter: EnhancedDeinterlaceFilter, required
        :return: Enhanced Deinterlace Filter details
        :rtype: EnhancedDeinterlaceFilter
        """

        return self.api_client.post(
            '/encoding/filters/enhanced-deinterlace',
            enhanced_deinterlace_filter,
            type=EnhancedDeinterlaceFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Enhanced Deinterlace Filter

        :param filter_id: Id of the Enhanced Deinterlace Filter
        :type filter_id: string_types, required
        :return: Id of the Enhanced Deinterlace Filter.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/enhanced-deinterlace/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> EnhancedDeinterlaceFilter
        """Enhanced Deinterlace Filter Details

        :param filter_id: Id of the Enhanced Deinterlace Filter
        :type filter_id: string_types, required
        :return: Enhanced Deinterlace Filter details
        :rtype: EnhancedDeinterlaceFilter
        """

        return self.api_client.get(
            '/encoding/filters/enhanced-deinterlace/{filter_id}',
            path_params={'filter_id': filter_id},
            type=EnhancedDeinterlaceFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (EnhancedDeinterlaceFilterListQueryParams, dict) -> EnhancedDeinterlaceFilter
        """List Enhanced Deinterlace Filters

        :param query_params: Query parameters
        :type query_params: EnhancedDeinterlaceFilterListQueryParams
        :return: List of Enhanced Deinterlace Filter ids
        :rtype: EnhancedDeinterlaceFilter
        """

        return self.api_client.get(
            '/encoding/filters/enhanced-deinterlace',
            query_params=query_params,
            pagination_response=True,
            type=EnhancedDeinterlaceFilter,
            **kwargs
        )
