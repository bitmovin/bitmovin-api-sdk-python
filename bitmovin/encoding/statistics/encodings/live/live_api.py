# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.encoding_statistics_live import EncodingStatisticsLive
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.statistics.encodings.live.encoding_statistics_live_list_query_params import EncodingStatisticsLiveListQueryParams
from bitmovin.encoding.statistics.encodings.live.encoding_statistics_live_list_by_date_range_query_params import EncodingStatisticsLiveListByDateRangeQueryParams


class LiveApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(LiveApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: EncodingStatisticsLiveListQueryParams = None, **kwargs):
        """List Live Encoding Statistics"""

        return self.api_client.get(
            '/encoding/statistics/encodings/live',
            query_params=query_params,
            pagination_response=True,
            type=EncodingStatisticsLive,
            **kwargs
        )

    def listByDateRange(self, _from, to, query_params: EncodingStatisticsLiveListByDateRangeQueryParams = None, **kwargs):
        """List live encoding statistics within specific dates"""

        return self.api_client.get(
            '/encoding/statistics/encodings/live/{from}/{to}',
            path_params={'from': _from, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=EncodingStatisticsLive,
            **kwargs
        )
