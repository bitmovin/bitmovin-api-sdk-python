# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.interlace_filter import InterlaceFilter
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.filters.interlace.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.filters.interlace.interlace_filter_list_query_params import InterlaceFilterListQueryParams


class InterlaceApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(InterlaceApi, self).__init__(
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

    def create(self, interlace_filter, **kwargs):
        # type: (InterlaceFilter, dict) -> InterlaceFilter
        """Create Interlace Filter

        :param interlace_filter: The Interlace Filter to be created
        :type interlace_filter: InterlaceFilter, required
        :return: Watermark details
        :rtype: InterlaceFilter
        """

        return self.api_client.post(
            '/encoding/filters/interlace',
            interlace_filter,
            type=InterlaceFilter,
            **kwargs
        )

    def delete(self, filter_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Interlace Filter

        :param filter_id: Id of the Interlace Filter
        :type filter_id: string_types, required
        :return: Id of the watermark.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/filters/interlace/{filter_id}',
            path_params={'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, filter_id, **kwargs):
        # type: (string_types, dict) -> InterlaceFilter
        """Interlace Filter Details

        :param filter_id: Id of the Interlace Filter
        :type filter_id: string_types, required
        :return: Watermark details
        :rtype: InterlaceFilter
        """

        return self.api_client.get(
            '/encoding/filters/interlace/{filter_id}',
            path_params={'filter_id': filter_id},
            type=InterlaceFilter,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (InterlaceFilterListQueryParams, dict) -> InterlaceFilter
        """List Interlace Filters

        :param query_params: Query parameters
        :type query_params: InterlaceFilterListQueryParams
        :return: List of interlace ids
        :rtype: InterlaceFilter
        """

        return self.api_client.get(
            '/encoding/filters/interlace',
            query_params=query_params,
            pagination_response=True,
            type=InterlaceFilter,
            **kwargs
        )
