# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.cea708_caption_input_stream import Cea708CaptionInputStream
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.captions.cea708.cea708_caption_input_stream_list_query_params import Cea708CaptionInputStreamListQueryParams


class Cea708Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Cea708Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, cea708_caption_input_stream, **kwargs):
        # type: (string_types, Cea708CaptionInputStream, dict) -> Cea708CaptionInputStream
        """Add CEA 708 Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param cea708_caption_input_stream: The CEA 708 Input Stream to be created
        :type cea708_caption_input_stream: Cea708CaptionInputStream, required
        :return: CEA 708 Input Stream
        :rtype: Cea708CaptionInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea708',
            cea708_caption_input_stream,
            path_params={'encoding_id': encoding_id},
            type=Cea708CaptionInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete CEA 708 Input Stream

        :param encoding_id: Id of the Encoding
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the CEA 708 input stream.
        :type input_stream_id: string_types, required
        :return: Id of the CEA 708 Input stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea708/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> Cea708CaptionInputStream
        """CEA 708 Input Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the CEA 708 input stream.
        :type input_stream_id: string_types, required
        :return: CEA 708 Input Stream
        :rtype: Cea708CaptionInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea708/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=Cea708CaptionInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, Cea708CaptionInputStreamListQueryParams, dict) -> Cea708CaptionInputStream
        """List CEA 708 Input Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: Cea708CaptionInputStreamListQueryParams
        :return: CEA 708 Input Streams
        :rtype: Cea708CaptionInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea708',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Cea708CaptionInputStream,
            **kwargs
        )
