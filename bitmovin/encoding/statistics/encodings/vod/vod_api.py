# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.encoding_statistics_vod import EncodingStatisticsVod
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.statistics.encodings.vod.encoding_statistics_vod_list_query_params import EncodingStatisticsVodListQueryParams
from bitmovin.encoding.statistics.encodings.vod.encoding_statistics_vod_list_by_date_range_query_params import EncodingStatisticsVodListByDateRangeQueryParams


class VodApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(VodApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params: EncodingStatisticsVodListQueryParams = None, **kwargs):
        """List VOD Encoding Statistics"""

        return self.api_client.get(
            '/encoding/statistics/encodings/vod',
            query_params=query_params,
            pagination_response=True,
            type=EncodingStatisticsVod,
            **kwargs
        )

    def listByDateRange(self, _from, to, query_params: EncodingStatisticsVodListByDateRangeQueryParams = None, **kwargs):
        """List VOD Encoding Statistics Within Specific Dates"""

        return self.api_client.get(
            '/encoding/statistics/encodings/vod/{from}/{to}',
            path_params={'from': _from, 'to': to},
            query_params=query_params,
            pagination_response=True,
            type=EncodingStatisticsVod,
            **kwargs
        )
