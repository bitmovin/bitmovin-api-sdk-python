# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.concatenation_input_stream import ConcatenationInputStream
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.concatenation.concatenation_input_stream_list_query_params import ConcatenationInputStreamListQueryParams


class ConcatenationApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ConcatenationApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, concatenation_input_stream, **kwargs):
        # type: (string_types, ConcatenationInputStream, dict) -> ConcatenationInputStream
        """Add Concatenation Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param concatenation_input_stream: The Concatenation Input Stream to be created
        :type concatenation_input_stream: ConcatenationInputStream, required
        :return: Concatenation Input Stream
        :rtype: ConcatenationInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/concatenation',
            concatenation_input_stream,
            path_params={'encoding_id': encoding_id},
            type=ConcatenationInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Concatenation Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the Concatenation input stream.
        :type input_stream_id: string_types, required
        :return: Id of the Concatenation input stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/concatenation/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> ConcatenationInputStream
        """Concatenation Input Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the concatenation input stream.
        :type input_stream_id: string_types, required
        :return: Stream
        :rtype: ConcatenationInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/concatenation/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=ConcatenationInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, ConcatenationInputStreamListQueryParams, dict) -> ConcatenationInputStream
        """List Concatenation Input Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ConcatenationInputStreamListQueryParams
        :return: List of Concatenation Input Streams
        :rtype: ConcatenationInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/concatenation',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ConcatenationInputStream,
            **kwargs
        )
