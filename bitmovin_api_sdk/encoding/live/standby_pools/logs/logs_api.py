# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.live_standby_pool_event_log import LiveStandbyPoolEventLog
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.encoding.live.standby_pools.logs.live_standby_pool_event_log_list_query_params import LiveStandbyPoolEventLogListQueryParams


class LogsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LogsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, pool_id, query_params=None, **kwargs):
        # type: (string_types, LiveStandbyPoolEventLogListQueryParams, dict) -> LiveStandbyPoolEventLog
        """List event logs for a standby pool

        :param pool_id: Id of the standby pool
        :type pool_id: string_types, required
        :param query_params: Query parameters
        :type query_params: LiveStandbyPoolEventLogListQueryParams
        :return: Standby pool event logs list response
        :rtype: LiveStandbyPoolEventLog
        """

        return self.api_client.get(
            '/encoding/live/standby-pools/{pool_id}/logs',
            path_params={'pool_id': pool_id},
            query_params=query_params,
            pagination_response=True,
            type=LiveStandbyPoolEventLog,
            **kwargs
        )
