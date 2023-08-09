# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.streams_search_response import StreamsSearchResponse
from bitmovin_api_sdk.streams.search.streams_search_response_list_query_params import StreamsSearchResponseListQueryParams


class SearchApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SearchApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params=None, **kwargs):
        # type: (StreamsSearchResponseListQueryParams, dict) -> StreamsSearchResponse
        """Get paginated search results of VOD and Live streams

        :param query_params: Query parameters
        :type query_params: StreamsSearchResponseListQueryParams
        :return: List of all search results
        :rtype: StreamsSearchResponse
        """

        return self.api_client.get(
            '/streams/search',
            query_params=query_params,
            pagination_response=True,
            type=StreamsSearchResponse,
            **kwargs
        )
