# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.statistics_per_label import StatisticsPerLabel
from bitmovin.encoding.statistics.labels.daily.daily_api import DailyApi
from bitmovin.encoding.statistics.labels.statistics_per_label_list_by_date_range_query_params import StatisticsPerLabelListByDateRangeQueryParams
from bitmovin.encoding.statistics.labels.statistics_per_label_list_query_params import StatisticsPerLabelListQueryParams


class LabelsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(LabelsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.daily = DailyApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: StatisticsPerLabelListQueryParams = None, **kwargs):
        """Get Statistics per Label"""

        return self.api_client.get(
            '/encoding/statistics/labels/',
            query_params=query_params,
            pagination_response=True,
            type=StatisticsPerLabel,
            **kwargs
        )

    def listByDateRange(self, _from, to, query_params: StatisticsPerLabelListByDateRangeQueryParams = None, **kwargs):
        """Get statistics per label within specific dates"""

        return self.api_client.get(
            '/encoding/statistics/labels/{from}/{to}',
            path_params={'from': _from, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=StatisticsPerLabel,
            **kwargs
        )
