# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.id3_tag import Id3Tag
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.id3.raw.raw_api import RawApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.id3.frame_id.frame_id_api import FrameIdApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.id3.plain_text.plain_text_api import PlainTextApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.id3.id3_tag_list_query_params import Id3TagListQueryParams


class Id3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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

        self.frame_id = FrameIdApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.plain_text = PlainTextApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, muxing_id, query_params=None, **kwargs):
        # type: (string_types, string_types, Id3TagListQueryParams, dict) -> Id3Tag
        """List all ID3 Tags of a Progressive TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :param query_params: Query parameters
        :type query_params: Id3TagListQueryParams
        :return: List of ID3 Tags including type attribute
        :rtype: Id3Tag
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=Id3Tag,
            **kwargs
        )
