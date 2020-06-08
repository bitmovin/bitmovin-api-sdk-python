# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.raw_id3_tag import RawId3Tag
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.id3.raw.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.id3.raw.raw_id3_tag_list_query_params import RawId3TagListQueryParams


class RawApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(RawApi, self).__init__(
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

    def create(self, encoding_id, muxing_id, raw_id3_tag, **kwargs):
        # type: (string_types, string_types, RawId3Tag, dict) -> RawId3Tag
        """Add Raw ID3 Tag to a Progressive TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :param raw_id3_tag: The Raw ID3 Tag to be created
        :type raw_id3_tag: RawId3Tag, required
        :return: Raw ID3 Tag
        :rtype: RawId3Tag
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/raw',
            raw_id3_tag,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=RawId3Tag,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, id3_tag_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Raw ID3 Tag of a Progressive TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :param id3_tag_id: ID of the RAW ID3 Tag
        :type id3_tag_id: string_types, required
        :return: ID of the Raw ID3 Tag
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/raw/{id3_tag_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'id3_tag_id': id3_tag_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, id3_tag_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> RawId3Tag
        """Raw ID3 Tag Details of a Progressive TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :param id3_tag_id: ID of the Raw ID3 Tag
        :type id3_tag_id: string_types, required
        :return: Raw ID3 Tag
        :rtype: RawId3Tag
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/raw/{id3_tag_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'id3_tag_id': id3_tag_id},
            type=RawId3Tag,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params=None, **kwargs):
        # type: (string_types, string_types, RawId3TagListQueryParams, dict) -> RawId3Tag
        """List Raw ID3 Tags of a Progressive TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :param query_params: Query parameters
        :type query_params: RawId3TagListQueryParams
        :return: List of Raw ID3 Tags
        :rtype: RawId3Tag
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/raw',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=RawId3Tag,
            **kwargs
        )
