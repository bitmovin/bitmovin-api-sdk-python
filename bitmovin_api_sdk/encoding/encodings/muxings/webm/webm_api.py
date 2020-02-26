# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.webm_muxing import WebmMuxing
from bitmovin_api_sdk.encoding.encodings.muxings.webm.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.webm.drm.drm_api import DrmApi
from bitmovin_api_sdk.encoding.encodings.muxings.webm.webm_muxing_list_query_params import WebmMuxingListQueryParams


class WebmApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(WebmApi, self).__init__(
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

        self.drm = DrmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, webm_muxing, **kwargs):
        # type: (string_types, WebmMuxing, dict) -> WebmMuxing
        """Add WebM muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param webm_muxing: The WebM muxing to be created
        :type webm_muxing: WebmMuxing, required
        :return: WebM muxing
        :rtype: WebmMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/webm',
            webm_muxing,
            path_params={'encoding_id': encoding_id},
            type=WebmMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete WebM muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the WebM muxing
        :type muxing_id: string_types, required
        :return: Id of the WebM muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/webm/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> WebmMuxing
        """WebM muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the WebM muxing
        :type muxing_id: string_types, required
        :return: WebM muxing
        :rtype: WebmMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/webm/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=WebmMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, WebmMuxingListQueryParams, dict) -> WebmMuxing
        """List WebM muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: WebmMuxingListQueryParams
        :return: List of WebM muxings
        :rtype: WebmMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/webm',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=WebmMuxing,
            **kwargs
        )
