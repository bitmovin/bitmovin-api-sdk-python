# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.progressive_webm_muxing import ProgressiveWebmMuxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_webm.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_webm.information.information_api import InformationApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_webm.drm.drm_api import DrmApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_webm.progressive_webm_muxing_list_query_params import ProgressiveWebmMuxingListQueryParams


class ProgressiveWebmApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ProgressiveWebmApi, self).__init__(
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

        self.drm = DrmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, progressive_webm_muxing, **kwargs):
        # type: (string_types, ProgressiveWebmMuxing, dict) -> ProgressiveWebmMuxing
        """Add Progressive WebM muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param progressive_webm_muxing: The Progressive WebM muxing to be created
        :type progressive_webm_muxing: ProgressiveWebmMuxing, required
        :return: Progressive WebM muxing
        :rtype: ProgressiveWebmMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-webm',
            progressive_webm_muxing,
            path_params={'encoding_id': encoding_id},
            type=ProgressiveWebmMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Progressive WebM muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Progressive WebM muxing
        :type muxing_id: string_types, required
        :return: Id of the Progressive WebM muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-webm/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> ProgressiveWebmMuxing
        """Progressive WebM muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Progressive WebM muxing
        :type muxing_id: string_types, required
        :return: Progressive WebM muxing
        :rtype: ProgressiveWebmMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-webm/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ProgressiveWebmMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, ProgressiveWebmMuxingListQueryParams, dict) -> ProgressiveWebmMuxing
        """List Progressive WebM muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ProgressiveWebmMuxingListQueryParams
        :return: List of Progressive WebM muxings
        :rtype: ProgressiveWebmMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-webm',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ProgressiveWebmMuxing,
            **kwargs
        )
