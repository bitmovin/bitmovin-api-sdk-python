# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.streams_video_create_request import StreamsVideoCreateRequest
from bitmovin_api_sdk.models.streams_video_response import StreamsVideoResponse
from bitmovin_api_sdk.models.streams_video_update_request import StreamsVideoUpdateRequest
from bitmovin_api_sdk.streams.video.streams_video_response_list_query_params import StreamsVideoResponseListQueryParams


class VideoApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(VideoApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, streams_video_create_request, **kwargs):
        # type: (StreamsVideoCreateRequest, dict) -> StreamsVideoResponse
        """Create new Streams video

        :param streams_video_create_request: Create a new stream.
        :type streams_video_create_request: StreamsVideoCreateRequest, required
        :return: Created vod stream
        :rtype: StreamsVideoResponse
        """

        return self.api_client.post(
            '/streams/video',
            streams_video_create_request,
            type=StreamsVideoResponse,
            **kwargs
        )

    def get(self, stream_id, **kwargs):
        # type: (string_types, dict) -> StreamsVideoResponse
        """Get Streams video by id

        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :return: stream
        :rtype: StreamsVideoResponse
        """

        return self.api_client.get(
            '/streams/video/{stream_id}',
            path_params={'stream_id': stream_id},
            type=StreamsVideoResponse,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (StreamsVideoResponseListQueryParams, dict) -> StreamsVideoResponse
        """Get paginated list of Streams videos

        :param query_params: Query parameters
        :type query_params: StreamsVideoResponseListQueryParams
        :return: List of all streams
        :rtype: StreamsVideoResponse
        """

        return self.api_client.get(
            '/streams/video',
            query_params=query_params,
            pagination_response=True,
            type=StreamsVideoResponse,
            **kwargs
        )

    def patch_streams_video(self, stream_id, streams_video_update_request, **kwargs):
        # type: (string_types, StreamsVideoUpdateRequest, dict) -> StreamsVideoResponse
        """Update Streams video by id

        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param streams_video_update_request: Stream fields to update.
        :type streams_video_update_request: StreamsVideoUpdateRequest, required
        :return:
        :rtype: StreamsVideoResponse
        """

        return self.api_client.patch(
            '/streams/video/{stream_id}',
            streams_video_update_request,
            path_params={'stream_id': stream_id},
            type=StreamsVideoResponse,
            **kwargs
        )
