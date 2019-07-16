# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.bitmovin_response_list import BitmovinResponseList
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.stream_filter import StreamFilter
from bitmovin_api_sdk.models.stream_filter_list import StreamFilterList
from bitmovin_api_sdk.encoding.encodings.streams.filters.stream_filter_list_list_query_params import StreamFilterListListQueryParams


class FiltersApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(FiltersApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream_id, stream_filter, **kwargs):
        # type: (string_types, string_types, list, dict) -> StreamFilterList
        """Add Filters to Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param stream_filter: The Filters to be added
        :type stream_filter: list[StreamFilter], required
        :return: List of created stream filters
        :rtype: StreamFilterList
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/filters',
            stream_filter,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=StreamFilterList,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, filter_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Specific Filter from Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param filter_id: Id of the filter
        :type filter_id: string_types, required
        :return: Id of the filter
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/filters/{filter_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'filter_id': filter_id},
            type=BitmovinResponse,
            **kwargs
        )

    def delete_all(self, encoding_id, stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponseList
        """Delete All Filters from Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :return: List of ids of deleted stream filters
        :rtype: BitmovinResponseList
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/filters',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=BitmovinResponseList,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params=None, **kwargs):
        # type: (string_types, string_types, StreamFilterListListQueryParams, dict) -> StreamFilterList
        """List the filters of a stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param query_params: Query parameters
        :type query_params: StreamFilterListListQueryParams
        :return: List of stream filters
        :rtype: StreamFilterList
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/filters',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            type=StreamFilterList,
            **kwargs
        )
