# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.daily_statistics_per_label import DailyStatisticsPerLabel
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.statistics.labels.daily.daily_statistics_per_label_list_query_params import DailyStatisticsPerLabelListQueryParams
from bitmovin_api_sdk.encoding.statistics.labels.daily.daily_statistics_per_label_list_by_date_range_query_params import DailyStatisticsPerLabelListByDateRangeQueryParams


class DailyApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DailyApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params=None, **kwargs):
        # type: (DailyStatisticsPerLabelListQueryParams, dict) -> DailyStatisticsPerLabel
        """Get Daily Statistics per Label

        :param query_params: Query parameters
        :type query_params: DailyStatisticsPerLabelListQueryParams
        :return: List of statistics per label and day
        :rtype: DailyStatisticsPerLabel
        """

        return self.api_client.get(
            '/encoding/statistics/labels/daily',
            query_params=query_params,
            pagination_response=True,
            type=DailyStatisticsPerLabel,
            **kwargs
        )

    def list_by_date_range(self, from_, to, query_params=None, **kwargs):
        # type: (date, date, DailyStatisticsPerLabelListByDateRangeQueryParams, dict) -> DailyStatisticsPerLabel
        """Get daily statistics per label within specific dates

        :param from_: Start date. Format: yyyy-MM-dd
        :type from_: date, required
        :param to: End date. Format: yyyy-MM-dd
        :type to: date, required
        :param query_params: Query parameters
        :type query_params: DailyStatisticsPerLabelListByDateRangeQueryParams
        :return: List of statistics per label and day
        :rtype: DailyStatisticsPerLabel
        """

        return self.api_client.get(
            '/encoding/statistics/labels/daily/{from}/{to}',
            path_params={'from': from_, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=DailyStatisticsPerLabel,
            **kwargs
        )
