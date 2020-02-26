# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.progressive_ts_muxing import ProgressiveTsMuxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.information.information_api import InformationApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.id3.id3_api import Id3Api
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.drm.drm_api import DrmApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.progressive_ts_muxing_list_query_params import ProgressiveTsMuxingListQueryParams


class ProgressiveTsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ProgressiveTsApi, self).__init__(
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

        self.id3 = Id3Api(
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

    def create(self, encoding_id, progressive_ts_muxing, **kwargs):
        # type: (string_types, ProgressiveTsMuxing, dict) -> ProgressiveTsMuxing
        """Add Progressive TS muxing

        :param encoding_id: ID of the encoding.
        :type encoding_id: string_types, required
        :param progressive_ts_muxing: The Progressive TS muxing to be created
        :type progressive_ts_muxing: ProgressiveTsMuxing, required
        :return: Progressive TS muxing
        :rtype: ProgressiveTsMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts',
            progressive_ts_muxing,
            path_params={'encoding_id': encoding_id},
            type=ProgressiveTsMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Progressive TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :return: ID of the Progressive TS muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> ProgressiveTsMuxing
        """Progressive TS muxing details

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Progressive TS muxing
        :type muxing_id: string_types, required
        :return: Progressive TS muxing
        :rtype: ProgressiveTsMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ProgressiveTsMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, ProgressiveTsMuxingListQueryParams, dict) -> ProgressiveTsMuxing
        """List Progressive TS muxings

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ProgressiveTsMuxingListQueryParams
        :return: List of Progressive TS muxings
        :rtype: ProgressiveTsMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-ts',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ProgressiveTsMuxing,
            **kwargs
        )
