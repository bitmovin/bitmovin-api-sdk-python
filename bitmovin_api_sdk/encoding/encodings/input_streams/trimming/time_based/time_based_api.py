# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.time_based_trimming_input_stream import TimeBasedTrimmingInputStream
from bitmovin_api_sdk.encoding.encodings.input_streams.trimming.time_based.time_based_trimming_input_stream_list_query_params import TimeBasedTrimmingInputStreamListQueryParams


class TimeBasedApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TimeBasedApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, time_based_trimming_input_stream, **kwargs):
        # type: (string_types, TimeBasedTrimmingInputStream, dict) -> TimeBasedTrimmingInputStream
        """Add Time-Based Trimming Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param time_based_trimming_input_stream: The Time-Based Trimming Input Stream to be created
        :type time_based_trimming_input_stream: TimeBasedTrimmingInputStream, required
        :return: Time-Based Trimming Input Stream
        :rtype: TimeBasedTrimmingInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/time-based',
            time_based_trimming_input_stream,
            path_params={'encoding_id': encoding_id},
            type=TimeBasedTrimmingInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Time-Based Trimming Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the Time-Based Trimming Input Stream.
        :type input_stream_id: string_types, required
        :return: Id of the Time-Based Trimming Input Stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/time-based/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> TimeBasedTrimmingInputStream
        """Time-Based Trimming Input Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the Time-Based Trimming Input Stream.
        :type input_stream_id: string_types, required
        :return: Stream
        :rtype: TimeBasedTrimmingInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/time-based/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=TimeBasedTrimmingInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, TimeBasedTrimmingInputStreamListQueryParams, dict) -> TimeBasedTrimmingInputStream
        """List Time-Based Trimming Input Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: TimeBasedTrimmingInputStreamListQueryParams
        :return: List of Time-Based Trimming Input Streams
        :rtype: TimeBasedTrimmingInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/time-based',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=TimeBasedTrimmingInputStream,
            **kwargs
        )
