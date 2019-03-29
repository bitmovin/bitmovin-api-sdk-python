# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.daily_statistics import DailyStatistics
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.statistics.daily.daily_statistics_list_query_params import DailyStatisticsListQueryParams
from bitmovin.encoding.statistics.daily.daily_statistics_list_by_date_range_query_params import DailyStatisticsListByDateRangeQueryParams


class DailyApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DailyApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: DailyStatisticsListQueryParams = None, **kwargs):
        """List Daily Statistics"""

        return self.api_client.get(
            '/encoding/statistics/daily',
            query_params=query_params,
            pagination_response=True,
            type=DailyStatistics,
            **kwargs
        )

    def listByDateRange(self, _from, to, query_params: DailyStatisticsListByDateRangeQueryParams = None, **kwargs):
        """List daily statistics within specific dates"""

        return self.api_client.get(
            '/encoding/statistics/daily/{from}/{to}',
            path_params={'from': _from, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=DailyStatistics,
            **kwargs
        )
