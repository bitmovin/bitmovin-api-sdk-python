# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.plaintext_id3_tag import PlaintextId3Tag
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.muxings.progressiveTs.id3.plainText.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.muxings.progressiveTs.id3.plainText.plaintext_id3_tag_list_query_params import PlaintextId3TagListQueryParams


class PlainTextApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(PlainTextApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, plaintext_id3_tag, **kwargs):
        """Add Plain Text ID3 Tag to Progressive TS Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/plain-text',
            plaintext_id3_tag,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=PlaintextId3Tag,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, id3_tag_id, **kwargs):
        """Delete Plain Text ID3 Tag of Progressive TS Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/plain-text/{id3_tag_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'id3_tag_id': id3_tag_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, id3_tag_id, **kwargs):
        """Plain Text ID3 Tag Details of Progressive TS Muxing"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/plain-text/{id3_tag_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'id3_tag_id': id3_tag_id},
            type=PlaintextId3Tag,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params: PlaintextId3TagListQueryParams = None, **kwargs):
        """List Plain Text ID3 Tags of Progressive TS Muxing"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/plain-text',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=PlaintextId3Tag,
            **kwargs
        )
