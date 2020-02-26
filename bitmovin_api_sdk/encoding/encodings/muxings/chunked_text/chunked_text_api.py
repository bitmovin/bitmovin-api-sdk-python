# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.chunked_text_muxing import ChunkedTextMuxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.chunked_text.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.chunked_text.chunked_text_muxing_list_query_params import ChunkedTextMuxingListQueryParams


class ChunkedTextApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (string_types, ChunkedTextMuxing, dict) -> ChunkedTextMuxing
        """Add Chunked Text muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param chunked_text_muxing: The Chunked Text muxing to be created
        :type chunked_text_muxing: ChunkedTextMuxing, required
        :return: Chunked Text muxing
        :rtype: ChunkedTextMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/chunked-text',
            chunked_text_muxing,
            path_params={'encoding_id': encoding_id},
            type=ChunkedTextMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Chunked Text muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Chunked Text muxing
        :type muxing_id: string_types, required
        :return: Id of the Chunked Text muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/chunked-text/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> ChunkedTextMuxing
        """Chunked Text muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Chunked Text muxing
        :type muxing_id: string_types, required
        :return: Chunked Text muxing
        :rtype: ChunkedTextMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/chunked-text/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ChunkedTextMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, ChunkedTextMuxingListQueryParams, dict) -> ChunkedTextMuxing
        """List Chunked Text muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ChunkedTextMuxingListQueryParams
        :return: List of Chunked Text muxings
        :rtype: ChunkedTextMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/chunked-text',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ChunkedTextMuxing,
            **kwargs
        )
