# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.streams_live_create_request import StreamsLiveCreateRequest
from bitmovin_api_sdk.models.streams_live_response import StreamsLiveResponse
from bitmovin_api_sdk.models.streams_live_update_request import StreamsLiveUpdateRequest
from bitmovin_api_sdk.streams.live.stop.stop_api import StopApi
from bitmovin_api_sdk.streams.live.start.start_api import StartApi
from bitmovin_api_sdk.streams.live.streams_live_response_list_query_params import StreamsLiveResponseListQueryParams


class LiveApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LiveApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.stop = StopApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.start = StartApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, streams_live_create_request, **kwargs):
        # type: (StreamsLiveCreateRequest, dict) -> StreamsLiveResponse
        """Create new live stream

        :param streams_live_create_request: Create a new stream.
        :type streams_live_create_request: StreamsLiveCreateRequest, required
        :return: Created stream
        :rtype: StreamsLiveResponse
        """

        return self.api_client.post(
            '/streams/live',
            streams_live_create_request,
            type=StreamsLiveResponse,
            **kwargs
        )

    def delete(self, stream_id, **kwargs):
        # type: (string_types, dict) -> None
        """Delete Stream

        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        """

        self.api_client.delete(
            '/streams/live/{stream_id}',
            path_params={'stream_id': stream_id},
            **kwargs
        )

    def get(self, stream_id, **kwargs):
        # type: (string_types, dict) -> StreamsLiveResponse
        """Get live stream by id

        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :return:
        :rtype: StreamsLiveResponse
        """

        return self.api_client.get(
            '/streams/live/{stream_id}',
            path_params={'stream_id': stream_id},
            type=StreamsLiveResponse,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (StreamsLiveResponseListQueryParams, dict) -> StreamsLiveResponse
        """Get paginated list of live streams

        :param query_params: Query parameters
        :type query_params: StreamsLiveResponseListQueryParams
        :return: List of all streams
        :rtype: StreamsLiveResponse
        """

        return self.api_client.get(
            '/streams/live',
            query_params=query_params,
            pagination_response=True,
            type=StreamsLiveResponse,
            **kwargs
        )

    def patch_streams_live(self, stream_id, streams_live_update_request, **kwargs):
        # type: (string_types, StreamsLiveUpdateRequest, dict) -> StreamsLiveResponse
        """Partially update live stream by id

        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param streams_live_update_request: Stream fields to update.
        :type streams_live_update_request: StreamsLiveUpdateRequest, required
        :return:
        :rtype: StreamsLiveResponse
        """

        return self.api_client.patch(
            '/streams/live/{stream_id}',
            streams_live_update_request,
            path_params={'stream_id': stream_id},
            type=StreamsLiveResponse,
            **kwargs
        )
