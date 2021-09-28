# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.prewarmed_encoder_pool_schedule import PrewarmedEncoderPoolSchedule
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.prewarmed_encoder_pools.schedules.prewarmed_encoder_pool_schedule_list_query_params import PrewarmedEncoderPoolScheduleListQueryParams


class SchedulesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SchedulesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, pool_id, prewarmed_encoder_pool_schedule, **kwargs):
        # type: (string_types, PrewarmedEncoderPoolSchedule, dict) -> PrewarmedEncoderPoolSchedule
        """Create prewarmed encoder pool schedule

        :param pool_id: Id of the scheduled encoder pool
        :type pool_id: string_types, required
        :param prewarmed_encoder_pool_schedule: The prewarmed encoder pool schedule to be created
        :type prewarmed_encoder_pool_schedule: PrewarmedEncoderPoolSchedule, required
        :return: Prewarmed encoder pool schedule
        :rtype: PrewarmedEncoderPoolSchedule
        """

        return self.api_client.post(
            '/encoding/infrastructure/prewarmed-encoder-pools/{pool_id}/schedules',
            prewarmed_encoder_pool_schedule,
            path_params={'pool_id': pool_id},
            type=PrewarmedEncoderPoolSchedule,
            **kwargs
        )

    def delete(self, pool_id, schedule_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete prewarmed encoder pool schedule

        :param pool_id: Id of the scheduled encoder pool
        :type pool_id: string_types, required
        :param schedule_id: Id of the prewarmed encoder pool schedule
        :type schedule_id: string_types, required
        :return: Id of the prewarmed encoder pool schedule that was deleted
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/infrastructure/prewarmed-encoder-pools/{pool_id}/schedules/{schedule_id}',
            path_params={'pool_id': pool_id, 'schedule_id': schedule_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, pool_id, schedule_id, **kwargs):
        # type: (string_types, string_types, dict) -> PrewarmedEncoderPoolSchedule
        """Prewarmed encoder pool schedule details

        :param pool_id: Id of the scheduled encoder pool
        :type pool_id: string_types, required
        :param schedule_id: Id of the prewarmed encoder pool schedule
        :type schedule_id: string_types, required
        :return: Prewarmed encoder pool schedule
        :rtype: PrewarmedEncoderPoolSchedule
        """

        return self.api_client.get(
            '/encoding/infrastructure/prewarmed-encoder-pools/{pool_id}/schedules/{schedule_id}',
            path_params={'pool_id': pool_id, 'schedule_id': schedule_id},
            type=PrewarmedEncoderPoolSchedule,
            **kwargs
        )

    def list(self, pool_id, query_params=None, **kwargs):
        # type: (string_types, PrewarmedEncoderPoolScheduleListQueryParams, dict) -> PrewarmedEncoderPoolSchedule
        """List prewarmed encoder pool schedules

        :param pool_id: Id of the scheduled encoder pool
        :type pool_id: string_types, required
        :param query_params: Query parameters
        :type query_params: PrewarmedEncoderPoolScheduleListQueryParams
        :return: List of prewarmed encoder pool schedules
        :rtype: PrewarmedEncoderPoolSchedule
        """

        return self.api_client.get(
            '/encoding/infrastructure/prewarmed-encoder-pools/{pool_id}/schedules',
            path_params={'pool_id': pool_id},
            query_params=query_params,
            pagination_response=True,
            type=PrewarmedEncoderPoolSchedule,
            **kwargs
        )
