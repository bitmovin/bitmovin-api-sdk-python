# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.encoding_statistics_live import EncodingStatisticsLive
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.statistics.encodings.live.daily.encoding_statistics_live_list_by_date_range_query_params import EncodingStatisticsLiveListByDateRangeQueryParams


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

    def list_by_date_range(self, from_, to, query_params=None, **kwargs):
        # type: (date, date, EncodingStatisticsLiveListByDateRangeQueryParams, dict) -> EncodingStatisticsLive
        """List daily live encoding statistics within specific dates

        :param from_: Start date, format: yyyy-MM-dd
        :type from_: date, required
        :param to: End date, format: yyyy-MM-dd
        :type to: date, required
        :param query_params: Query parameters
        :type query_params: EncodingStatisticsLiveListByDateRangeQueryParams
        :return: List of encoding statistics
        :rtype: EncodingStatisticsLive
        """

        return self.api_client.get(
            '/encoding/statistics/encodings/live/daily/{from}/{to}',
            path_params={'from': from_, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=EncodingStatisticsLive,
            **kwargs
        )
