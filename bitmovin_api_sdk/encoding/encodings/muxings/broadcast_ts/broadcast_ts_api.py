# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.broadcast_ts_muxing import BroadcastTsMuxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.broadcast_ts.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.broadcast_ts.information.information_api import InformationApi
from bitmovin_api_sdk.encoding.encodings.muxings.broadcast_ts.broadcast_ts_muxing_list_query_params import BroadcastTsMuxingListQueryParams


class BroadcastTsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(BroadcastTsApi, self).__init__(
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

    def create(self, encoding_id, broadcast_ts_muxing, **kwargs):
        # type: (string_types, BroadcastTsMuxing, dict) -> BroadcastTsMuxing
        """Add Broadcast TS muxing

        :param encoding_id: ID of the encoding.
        :type encoding_id: string_types, required
        :param broadcast_ts_muxing: The Broadcast TS muxing to be created
        :type broadcast_ts_muxing: BroadcastTsMuxing, required
        :return: Broadcast TS muxing
        :rtype: BroadcastTsMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/broadcast-ts',
            broadcast_ts_muxing,
            path_params={'encoding_id': encoding_id},
            type=BroadcastTsMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Broadcast TS muxing

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Broadcast TS muxing
        :type muxing_id: string_types, required
        :return: ID of the Broadcast TS muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/broadcast-ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BroadcastTsMuxing
        """Broadcast TS muxing details

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Broadcast TS muxing
        :type muxing_id: string_types, required
        :return: Broadcast TS muxing
        :rtype: BroadcastTsMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/broadcast-ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BroadcastTsMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, BroadcastTsMuxingListQueryParams, dict) -> BroadcastTsMuxing
        """List Broadcast TS muxings

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: BroadcastTsMuxingListQueryParams
        :return: List of Broadcast TS muxings
        :rtype: BroadcastTsMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/broadcast-ts',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=BroadcastTsMuxing,
            **kwargs
        )
