# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.h264_picture_timing_trimming_input_stream import H264PictureTimingTrimmingInputStream
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.trimming.h264_picture_timing.h264_picture_timing_trimming_input_stream_list_query_params import H264PictureTimingTrimmingInputStreamListQueryParams


class H264PictureTimingApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(H264PictureTimingApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, h264_picture_timing_trimming_input_stream, **kwargs):
        # type: (string_types, H264PictureTimingTrimmingInputStream, dict) -> H264PictureTimingTrimmingInputStream
        """Add H264 Picture Timing Trimming Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param h264_picture_timing_trimming_input_stream: The H264 Picture Timing Trimming Input Stream to be created
        :type h264_picture_timing_trimming_input_stream: H264PictureTimingTrimmingInputStream, required
        :return: H264 Picture Timing Trimming Input Stream
        :rtype: H264PictureTimingTrimmingInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/h264-picture-timing',
            h264_picture_timing_trimming_input_stream,
            path_params={'encoding_id': encoding_id},
            type=H264PictureTimingTrimmingInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete H264 Picture Timing Trimming Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the H264 Picture Timing Trimming Input Stream.
        :type input_stream_id: string_types, required
        :return: Id of the H264 Picture Timing Trimming Input Stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/h264-picture-timing/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> H264PictureTimingTrimmingInputStream
        """H264 Picture Timing Trimming Input Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the H264 Picture Timing Trimming Input Stream.
        :type input_stream_id: string_types, required
        :return: Stream
        :rtype: H264PictureTimingTrimmingInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/h264-picture-timing/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=H264PictureTimingTrimmingInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, H264PictureTimingTrimmingInputStreamListQueryParams, dict) -> H264PictureTimingTrimmingInputStream
        """List H264 Picture Timing Trimming Input Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: H264PictureTimingTrimmingInputStreamListQueryParams
        :return: List of H264 Picture Timing Trimming Input Streams
        :rtype: H264PictureTimingTrimmingInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/h264-picture-timing',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=H264PictureTimingTrimmingInputStream,
            **kwargs
        )
