# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.chunked_text_muxing import ChunkedTextMuxing
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.muxings.chunkedText.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.muxings.chunkedText.chunked_text_muxing_list_query_params import ChunkedTextMuxingListQueryParams


class ChunkedTextApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ChunkedTextApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, chunked_text_muxing, **kwargs):
        """Add Chunked Text Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/chunked-text',
            chunked_text_muxing,
            path_params={'encoding_id': encoding_id},
            type=ChunkedTextMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete Chunked Text Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/chunked-text/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """Chunked Text Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/chunked-text/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ChunkedTextMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: ChunkedTextMuxingListQueryParams = None, **kwargs):
        """List Chunked Text Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/chunked-text',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ChunkedTextMuxing,
            **kwargs
        )
