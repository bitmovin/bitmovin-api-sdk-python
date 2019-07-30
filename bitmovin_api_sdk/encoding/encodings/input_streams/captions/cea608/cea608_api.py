# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.cea608_caption_input_stream import Cea608CaptionInputStream
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.captions.cea608.cea608_caption_input_stream_list_query_params import Cea608CaptionInputStreamListQueryParams


class Cea608Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Cea608Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, cea608_caption_input_stream, **kwargs):
        # type: (string_types, Cea608CaptionInputStream, dict) -> Cea608CaptionInputStream
        """Add CEA 608 Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param cea608_caption_input_stream: The CEA 608 Input Stream to be created
        :type cea608_caption_input_stream: Cea608CaptionInputStream, required
        :return: CEA 608 Input Stream
        :rtype: Cea608CaptionInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea608',
            cea608_caption_input_stream,
            path_params={'encoding_id': encoding_id},
            type=Cea608CaptionInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete CEA 608 Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the CEA 608 input stream.
        :type input_stream_id: string_types, required
        :return: Id of the CEA 608 Input stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea608/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> Cea608CaptionInputStream
        """CEA 608 Input Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the CEA 608 input stream.
        :type input_stream_id: string_types, required
        :return: CEA 608 Input Stream
        :rtype: Cea608CaptionInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea608/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=Cea608CaptionInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, Cea608CaptionInputStreamListQueryParams, dict) -> Cea608CaptionInputStream
        """List CEA 608 Input Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: Cea608CaptionInputStreamListQueryParams
        :return: CEA 608 Input Streams
        :rtype: Cea608CaptionInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea608',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Cea608CaptionInputStream,
            **kwargs
        )
