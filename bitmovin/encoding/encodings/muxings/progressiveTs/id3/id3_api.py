# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.id3_tag import Id3Tag
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.muxings.progressiveTs.id3.raw.raw_api import RawApi
from bitmovin.encoding.encodings.muxings.progressiveTs.id3.frameId.frame_id_api import FrameIdApi
from bitmovin.encoding.encodings.muxings.progressiveTs.id3.plainText.plain_text_api import PlainTextApi
from bitmovin.encoding.encodings.muxings.progressiveTs.id3.id3_tag_list_query_params import Id3TagListQueryParams


class Id3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Id3Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.raw = RawApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.frameId = FrameIdApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.plainText = PlainTextApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, muxing_id, query_params: Id3TagListQueryParams = None, **kwargs):
        """List all ID3 Tags of Progressive TS Muxing"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=Id3Tag,
            **kwargs
        )
