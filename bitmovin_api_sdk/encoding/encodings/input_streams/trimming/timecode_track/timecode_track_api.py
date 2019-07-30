# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.timecode_track_trimming_input_stream import TimecodeTrackTrimmingInputStream
from bitmovin_api_sdk.encoding.encodings.input_streams.trimming.timecode_track.timecode_track_trimming_input_stream_list_query_params import TimecodeTrackTrimmingInputStreamListQueryParams


class TimecodeTrackApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TimecodeTrackApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, timecode_track_trimming_input_stream, **kwargs):
        # type: (string_types, TimecodeTrackTrimmingInputStream, dict) -> TimecodeTrackTrimmingInputStream
        """Add Timecode Track Trimming Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param timecode_track_trimming_input_stream: The Timecode Track Trimming Input Stream to be created
        :type timecode_track_trimming_input_stream: TimecodeTrackTrimmingInputStream, required
        :return: Timecode Track Trimming Input Stream
        :rtype: TimecodeTrackTrimmingInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/timecode-track',
            timecode_track_trimming_input_stream,
            path_params={'encoding_id': encoding_id},
            type=TimecodeTrackTrimmingInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Timecode Track Trimming Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the Timecode Track Trimming Input Stream.
        :type input_stream_id: string_types, required
        :return: Id of the Timecode Track Trimming Input Stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/timecode-track/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> TimecodeTrackTrimmingInputStream
        """Timecode Track Trimming Input Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the Timecode Track Trimming Input Stream.
        :type input_stream_id: string_types, required
        :return: Stream
        :rtype: TimecodeTrackTrimmingInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/timecode-track/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=TimecodeTrackTrimmingInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, TimecodeTrackTrimmingInputStreamListQueryParams, dict) -> TimecodeTrackTrimmingInputStream
        """List Timecode Track Trimming Input Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: TimecodeTrackTrimmingInputStreamListQueryParams
        :return: List of Timecode Track Trimming Input Streams
        :rtype: TimecodeTrackTrimmingInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/timecode-track',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=TimecodeTrackTrimmingInputStream,
            **kwargs
        )
