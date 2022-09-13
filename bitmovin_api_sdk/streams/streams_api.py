# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_stream_response import BitmovinStreamResponse
from bitmovin_api_sdk.models.create_bitmovin_stream_request import CreateBitmovinStreamRequest
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.update_bitmovin_stream_request import UpdateBitmovinStreamRequest
from bitmovin_api_sdk.streams.bitmovin_stream_response_list_query_params import BitmovinStreamResponseListQueryParams


class StreamsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(StreamsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, create_bitmovin_stream_request, **kwargs):
        # type: (CreateBitmovinStreamRequest, dict) -> BitmovinStreamResponse
        """Create new Stream

        :param create_bitmovin_stream_request: Create a new Stream.
        :type create_bitmovin_stream_request: CreateBitmovinStreamRequest, required
        :return: Created Stream
        :rtype: BitmovinStreamResponse
        """

        return self.api_client.post(
            '/streams',
            create_bitmovin_stream_request,
            type=BitmovinStreamResponse,
            **kwargs
        )

    def get(self, stream_id, **kwargs):
        # type: (string_types, dict) -> BitmovinStreamResponse
        """Get Stream by id

        :param stream_id: Id of the Stream.
        :type stream_id: string_types, required
        :return: Stream
        :rtype: BitmovinStreamResponse
        """

        return self.api_client.get(
            '/streams/{stream_id}',
            path_params={'stream_id': stream_id},
            type=BitmovinStreamResponse,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (BitmovinStreamResponseListQueryParams, dict) -> BitmovinStreamResponse
        """Get paginated list of Streams

        :param query_params: Query parameters
        :type query_params: BitmovinStreamResponseListQueryParams
        :return: List of all streams
        :rtype: BitmovinStreamResponse
        """

        return self.api_client.get(
            '/streams',
            query_params=query_params,
            pagination_response=True,
            type=BitmovinStreamResponse,
            **kwargs
        )

    def patch_bitmovin_streams_streams_by_stream_id(self, stream_id, update_bitmovin_stream_request, **kwargs):
        # type: (string_types, UpdateBitmovinStreamRequest, dict) -> BitmovinStreamResponse
        """Update Stream by id

        :param stream_id: Id of the Stream.
        :type stream_id: string_types, required
        :param update_bitmovin_stream_request: Stream fields to update.
        :type update_bitmovin_stream_request: UpdateBitmovinStreamRequest, required
        :return:
        :rtype: BitmovinStreamResponse
        """

        return self.api_client.patch(
            '/streams/{stream_id}',
            update_bitmovin_stream_request,
            path_params={'stream_id': stream_id},
            type=BitmovinStreamResponse,
            **kwargs
        )
