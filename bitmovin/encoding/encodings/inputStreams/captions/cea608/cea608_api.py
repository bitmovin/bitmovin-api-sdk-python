# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.cea608_caption_input_stream import Cea608CaptionInputStream
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.inputStreams.captions.cea608.cea608_caption_input_stream_list_query_params import Cea608CaptionInputStreamListQueryParams


class Cea608Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Cea608Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, cea608_caption_input_stream, **kwargs):
        """Add CEA 608 Input Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea608',
            cea608_caption_input_stream,
            path_params={'encoding_id': encoding_id},
            type=Cea608CaptionInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        """Delete CEA 608 Input Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea608/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """CEA 608 Input Stream Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea608/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=Cea608CaptionInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params: Cea608CaptionInputStreamListQueryParams = None, **kwargs):
        """List CEA 608 Input Streams"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/captions/cea608',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Cea608CaptionInputStream,
            **kwargs
        )
