# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.ts_muxing import TsMuxing
from bitmovin_api_sdk.encoding.encodings.muxings.ts.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.ts.drm.drm_api import DrmApi
from bitmovin_api_sdk.encoding.encodings.muxings.ts.ts_muxing_list_query_params import TsMuxingListQueryParams


class TsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TsApi, self).__init__(
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

    def create(self, encoding_id, ts_muxing, **kwargs):
        # type: (string_types, TsMuxing, dict) -> TsMuxing
        """Add TS muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param ts_muxing: The TS muxing to be created
        :type ts_muxing: TsMuxing, required
        :return: TS muxing
        :rtype: TsMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/ts',
            ts_muxing,
            path_params={'encoding_id': encoding_id},
            type=TsMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete TS muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the TS muxing
        :type muxing_id: string_types, required
        :return: Id of the TS muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> TsMuxing
        """TS muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the TS muxing
        :type muxing_id: string_types, required
        :return: TS muxing
        :rtype: TsMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=TsMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, TsMuxingListQueryParams, dict) -> TsMuxing
        """List TS muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: TsMuxingListQueryParams
        :return: List of TS muxings
        :rtype: TsMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=TsMuxing,
            **kwargs
        )
