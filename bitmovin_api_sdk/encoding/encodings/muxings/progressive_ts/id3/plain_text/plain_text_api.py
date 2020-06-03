# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.plaintext_id3_tag import PlaintextId3Tag
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.id3.plain_text.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.id3.plain_text.plaintext_id3_tag_list_query_params import PlaintextId3TagListQueryParams


class PlainTextApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (string_types, string_types, PlaintextId3Tag, dict) -> PlaintextId3Tag
        """Add Plain Text ID3 Tag to a Progressive TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :param plaintext_id3_tag: The Plain Text ID3 Tag to be created
        :type plaintext_id3_tag: PlaintextId3Tag, required
        :return: Plain Text ID3 Tag
        :rtype: PlaintextId3Tag
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/plain-text',
            plaintext_id3_tag,
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=PlaintextId3Tag,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, id3_tag_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Plain Text ID3 Tag of a Progressive TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :param id3_tag_id: ID of the Plain Text ID3 Tag
        :type id3_tag_id: string_types, required
        :return: ID of the Plain Text ID3 Tag
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/plain-text/{id3_tag_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'id3_tag_id': id3_tag_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, id3_tag_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> PlaintextId3Tag
        """Plain Text ID3 Tag Details of a Progressive TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :param id3_tag_id: ID of the Plain Text ID3 Tag
        :type id3_tag_id: string_types, required
        :return: Plain Text ID3 Tag
        :rtype: PlaintextId3Tag
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/plain-text/{id3_tag_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id, 'id3_tag_id': id3_tag_id},
            type=PlaintextId3Tag,
            **kwargs
        )

    def list(self, encoding_id, muxing_id, query_params=None, **kwargs):
        # type: (string_types, string_types, PlaintextId3TagListQueryParams, dict) -> PlaintextId3Tag
        """List Plain Text ID3 Tags of a Progressive TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :param query_params: Query parameters
        :type query_params: PlaintextId3TagListQueryParams
        :return: List of Plain Text ID3 Tags
        :rtype: PlaintextId3Tag
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}/id3/plain-text',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            query_params=query_params,
            pagination_response=True,
            type=PlaintextId3Tag,
            **kwargs
        )
