# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.dvb_teletext_input_stream import DvbTeletextInputStream
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.inputStreams.subtitles.dvbTeletext.dvb_teletext_input_stream_list_query_params import DvbTeletextInputStreamListQueryParams


class DvbTeletextApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DvbTeletextApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, dvb_teletext_input_stream, **kwargs):
        """Add DVB-Teletext Input Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-teletext',
            dvb_teletext_input_stream,
            path_params={'encoding_id': encoding_id},
            type=DvbTeletextInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        """Delete DVB-Teletext Input Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-teletext/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """DVB-Teletext Input Stream Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-teletext/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=DvbTeletextInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params: DvbTeletextInputStreamListQueryParams = None, **kwargs):
        """List DVB-Teletext Input Streams"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/subtitles/dvb-teletext',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=DvbTeletextInputStream,
            **kwargs
        )
