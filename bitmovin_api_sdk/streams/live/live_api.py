# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.streams_live_update_request import StreamsLiveUpdateRequest


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

    def patch_streams_live(self, stream_id, streams_live_update_request, **kwargs):
        # type: (string_types, StreamsLiveUpdateRequest, dict) -> StreamsLiveUpdateRequest
        """Update live stream by id

        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param streams_live_update_request: Stream fields to update.
        :type streams_live_update_request: StreamsLiveUpdateRequest, required
        :return:
        :rtype: StreamsLiveUpdateRequest
        """

        return self.api_client.patch(
            '/streams/live/{stream_id}',
            streams_live_update_request,
            path_params={'stream_id': stream_id},
            type=StreamsLiveUpdateRequest,
            **kwargs
        )
