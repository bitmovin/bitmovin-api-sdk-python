# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.srt_statistics import SrtStatistics
from bitmovin.encoding.statistics.encodings.liveStatistics.srt.srt_statistics_list_by_srt_input_id_query_params import SrtStatisticsListBySrtInputIdQueryParams
from bitmovin.encoding.statistics.encodings.liveStatistics.srt.srt_statistics_list_query_params import SrtStatisticsListQueryParams


class SrtApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(SrtApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, query_params: SrtStatisticsListQueryParams = None, **kwargs):
        """List Stream Infos of Live Statistics from an Encoding"""

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}/live-statistics/srt',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=SrtStatistics,
            **kwargs
        )

    def listBySrtInputId(self, encoding_id, srt_input_id, query_params: SrtStatisticsListBySrtInputIdQueryParams = None, **kwargs):
        """List Statistics For SRT Live Stream Input"""

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}/live-statistics/srt/{srt_input_id}',
            path_params={'encoding_id': encoding_id, 'srt_input_id': srt_input_id},
            query_params=query_params,
            pagination_response=True,
            type=SrtStatistics,
            **kwargs
        )
