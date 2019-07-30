# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dvb_teletext_input_stream import DvbTeletextInputStream
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.subtitles.dvb_teletext.dvb_teletext_input_stream_list_query_params import DvbTeletextInputStreamListQueryParams


class DvbTeletextApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DvbTeletextApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, dvb_teletext_input_stream, **kwargs):
        # type: (string_types, DvbTeletextInputStream, dict) -> DvbTeletextInputStream
        """Add DVB-Teletext Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param dvb_teletext_input_stream: The DVB-Teletext Input Stream to be created
        :type dvb_teletext_input_stream: DvbTeletextInputStream, required
        :return: DVB-Teletext Input Stream
        :rtype: DvbTeletextInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-teletext',
            dvb_teletext_input_stream,
            path_params={'encoding_id': encoding_id},
            type=DvbTeletextInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete DVB-Teletext Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the DVB-Teletext input stream.
        :type input_stream_id: string_types, required
        :return: Id of the DVB-Teletext Input stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-teletext/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> DvbTeletextInputStream
        """DVB-Teletext Input Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the DVB-Teletext input stream.
        :type input_stream_id: string_types, required
        :return: DVB-Teletext Input Stream
        :rtype: DvbTeletextInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-teletext/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=DvbTeletextInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, DvbTeletextInputStreamListQueryParams, dict) -> DvbTeletextInputStream
        """List DVB-Teletext Input Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DvbTeletextInputStreamListQueryParams
        :return: List of DVB-Teletext Input Streams
        :rtype: DvbTeletextInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-teletext',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=DvbTeletextInputStream,
            **kwargs
        )
