# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dvb_subtitle_input_stream import DvbSubtitleInputStream
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.subtitles.dvb_subtitle.dvb_subtitle_input_stream_list_query_params import DvbSubtitleInputStreamListQueryParams


class DvbSubtitleApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DvbSubtitleApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, dvb_subtitle_input_stream, **kwargs):
        # type: (string_types, DvbSubtitleInputStream, dict) -> DvbSubtitleInputStream
        """Add DVB Subtitle Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param dvb_subtitle_input_stream: The DVB Subtitle Input Stream to be created
        :type dvb_subtitle_input_stream: DvbSubtitleInputStream, required
        :return: DVB Subtitle Input Stream
        :rtype: DvbSubtitleInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-subtitle',
            dvb_subtitle_input_stream,
            path_params={'encoding_id': encoding_id},
            type=DvbSubtitleInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete DVB Subtitle Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the DVB Subtitle Input Stream.
        :type input_stream_id: string_types, required
        :return: Id of the DVB Subtitle Input Stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-subtitle/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> DvbSubtitleInputStream
        """DVB Subtitle Input Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the DVB Subtitle Input Stream.
        :type input_stream_id: string_types, required
        :return: DVB Subtitle Input Stream
        :rtype: DvbSubtitleInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-subtitle/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=DvbSubtitleInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, DvbSubtitleInputStreamListQueryParams, dict) -> DvbSubtitleInputStream
        """List DVB Subtitle Input Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DvbSubtitleInputStreamListQueryParams
        :return: List of DVB Subtitle Input Streams
        :rtype: DvbSubtitleInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-subtitle',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=DvbSubtitleInputStream,
            **kwargs
        )
