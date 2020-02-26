# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.progressive_mov_muxing import ProgressiveMovMuxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_mov.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_mov.information.information_api import InformationApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_mov.progressive_mov_muxing_list_query_params import ProgressiveMovMuxingListQueryParams


class ProgressiveMovApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ProgressiveMovApi, self).__init__(
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

        self.information = InformationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, progressive_mov_muxing, **kwargs):
        # type: (string_types, ProgressiveMovMuxing, dict) -> ProgressiveMovMuxing
        """Add Progressive MOV muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param progressive_mov_muxing: The Progressive MOV muxing to be created
        :type progressive_mov_muxing: ProgressiveMovMuxing, required
        :return: Progressive MOV muxing
        :rtype: ProgressiveMovMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-mov',
            progressive_mov_muxing,
            path_params={'encoding_id': encoding_id},
            type=ProgressiveMovMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Progressive MOV muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Progressive MOV muxing
        :type muxing_id: string_types, required
        :return: Id of the Progressive MOV muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-mov/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> ProgressiveMovMuxing
        """Progressive MOV muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Progressive MOV muxing
        :type muxing_id: string_types, required
        :return: Progressive MOV muxing details
        :rtype: ProgressiveMovMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-mov/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ProgressiveMovMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, ProgressiveMovMuxingListQueryParams, dict) -> ProgressiveMovMuxing
        """List Progressive MOV muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ProgressiveMovMuxingListQueryParams
        :return: List of Progressive MOV muxings
        :rtype: ProgressiveMovMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-mov',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ProgressiveMovMuxing,
            **kwargs
        )
