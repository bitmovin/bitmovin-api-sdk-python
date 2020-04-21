# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.fmp4_muxing import Fmp4Muxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.fmp4.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.fmp4.information.information_api import InformationApi
from bitmovin_api_sdk.encoding.encodings.muxings.fmp4.drm.drm_api import DrmApi
from bitmovin_api_sdk.encoding.encodings.muxings.fmp4.fmp4_muxing_list_query_params import Fmp4MuxingListQueryParams


class Fmp4Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Fmp4Api, self).__init__(
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

    def create(self, encoding_id, fmp4_muxing, **kwargs):
        # type: (string_types, Fmp4Muxing, dict) -> Fmp4Muxing
        """Add fMP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param fmp4_muxing: The fMP4 muxing to be created
        :type fmp4_muxing: Fmp4Muxing, required
        :return: fMP4 muxing
        :rtype: Fmp4Muxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/fmp4',
            fmp4_muxing,
            path_params={'encoding_id': encoding_id},
            type=Fmp4Muxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete fMP4 muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the fMP4 muxing
        :type muxing_id: string_types, required
        :return: Id of the fMP4 muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> Fmp4Muxing
        """fMP4 muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the fMP4 muxing
        :type muxing_id: string_types, required
        :return: fMP4 muxing
        :rtype: Fmp4Muxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=Fmp4Muxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, Fmp4MuxingListQueryParams, dict) -> Fmp4Muxing
        """List fMP4 muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: Fmp4MuxingListQueryParams
        :return: List of fMP4 muxings
        :rtype: Fmp4Muxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/fmp4',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Fmp4Muxing,
            **kwargs
        )
