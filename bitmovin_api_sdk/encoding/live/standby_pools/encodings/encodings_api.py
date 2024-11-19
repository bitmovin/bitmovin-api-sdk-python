# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.live_standby_pool_encoding import LiveStandbyPoolEncoding
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.live.standby_pools.encodings.live_standby_pool_encoding_list_query_params import LiveStandbyPoolEncodingListQueryParams


class EncodingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EncodingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def delete(self, pool_id, id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete encoding from pool by id

        :param pool_id: Id of the standby pool
        :type pool_id: string_types, required
        :param id: Id of the standby pool encoding
        :type id: string_types, required
        :return: Id of the encoding from the pool that was deleted
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/live/standby-pools/{pool_id}/encodings/{id}',
            path_params={'pool_id': pool_id, 'id': id},
            type=BitmovinResponse,
            **kwargs
        )

    def list(self, pool_id, query_params=None, **kwargs):
        # type: (string_types, LiveStandbyPoolEncodingListQueryParams, dict) -> LiveStandbyPoolEncoding
        """List encodings from a standby pool

        :param pool_id: Id of the standby pool
        :type pool_id: string_types, required
        :param query_params: Query parameters
        :type query_params: LiveStandbyPoolEncodingListQueryParams
        :return: Standby pool encodings list response
        :rtype: LiveStandbyPoolEncoding
        """

        return self.api_client.get(
            '/encoding/live/standby-pools/{pool_id}/encodings',
            path_params={'pool_id': pool_id},
            query_params=query_params,
            pagination_response=True,
            type=LiveStandbyPoolEncoding,
            **kwargs
        )
