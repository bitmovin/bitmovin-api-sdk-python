# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.prewarmed_encoder_pool import PrewarmedEncoderPool
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.prewarmed_encoder_pools.schedules.schedules_api import SchedulesApi
from bitmovin_api_sdk.encoding.infrastructure.prewarmed_encoder_pools.prewarmed_encoder_pool_list_query_params import PrewarmedEncoderPoolListQueryParams


class PrewarmedEncoderPoolsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PrewarmedEncoderPoolsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.schedules = SchedulesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, prewarmed_encoder_pool, **kwargs):
        # type: (PrewarmedEncoderPool, dict) -> PrewarmedEncoderPool
        """Create prewarmed encoder pool

        :param prewarmed_encoder_pool: The prewarmed encoder pool to be created
        :type prewarmed_encoder_pool: PrewarmedEncoderPool, required
        :return: Prewarmed encoder pool
        :rtype: PrewarmedEncoderPool
        """

        return self.api_client.post(
            '/encoding/infrastructure/prewarmed-encoder-pools',
            prewarmed_encoder_pool,
            type=PrewarmedEncoderPool,
            **kwargs
        )

    def delete(self, pool_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete prewarmed encoder pool

        :param pool_id: Id of the prewarmed encoder pool
        :type pool_id: string_types, required
        :return: Id of the prewarmed encoder pool that was deleted
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/infrastructure/prewarmed-encoder-pools/{pool_id}',
            path_params={'pool_id': pool_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, pool_id, **kwargs):
        # type: (string_types, dict) -> PrewarmedEncoderPool
        """Prewarmed encoder pool details

        :param pool_id: Id of the prewarmed encoder pool
        :type pool_id: string_types, required
        :return: Prewarmed encoder pool
        :rtype: PrewarmedEncoderPool
        """

        return self.api_client.get(
            '/encoding/infrastructure/prewarmed-encoder-pools/{pool_id}',
            path_params={'pool_id': pool_id},
            type=PrewarmedEncoderPool,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (PrewarmedEncoderPoolListQueryParams, dict) -> PrewarmedEncoderPool
        """List prewarmed encoder pools

        :param query_params: Query parameters
        :type query_params: PrewarmedEncoderPoolListQueryParams
        :return: List of prewarmed encoder pools
        :rtype: PrewarmedEncoderPool
        """

        return self.api_client.get(
            '/encoding/infrastructure/prewarmed-encoder-pools',
            query_params=query_params,
            pagination_response=True,
            type=PrewarmedEncoderPool,
            **kwargs
        )

    def start(self, pool_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Start prewarmed encoder pool

        :param pool_id: Id of the prewarmed encoder pool to be started
        :type pool_id: string_types, required
        :return: Id of the prewarmed encoder pool
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/infrastructure/prewarmed-encoder-pools/{pool_id}/start',
            path_params={'pool_id': pool_id},
            type=BitmovinResponse,
            **kwargs
        )

    def stop(self, pool_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Stop prewarmed encoder pool

        :param pool_id: Id of the prewarmed encoder pool to be stopped
        :type pool_id: string_types, required
        :return: Id of the prewarmed encoder pool
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/infrastructure/prewarmed-encoder-pools/{pool_id}/stop',
            path_params={'pool_id': pool_id},
            type=BitmovinResponse,
            **kwargs
        )
