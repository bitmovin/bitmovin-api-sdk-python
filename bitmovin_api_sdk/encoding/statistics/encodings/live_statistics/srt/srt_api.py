# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.srt_statistics import SrtStatistics
from bitmovin_api_sdk.encoding.statistics.encodings.live_statistics.srt.srt_statistics_list_query_params import SrtStatisticsListQueryParams
from bitmovin_api_sdk.encoding.statistics.encodings.live_statistics.srt.srt_statistics_list_by_srt_input_id_query_params import SrtStatisticsListBySrtInputIdQueryParams


class SrtApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SrtApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, SrtStatisticsListQueryParams, dict) -> SrtStatistics
        """List Stream Infos of Live Statistics from an Encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SrtStatisticsListQueryParams
        :return: List of statistics
        :rtype: SrtStatistics
        """

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}/live-statistics/srt',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=SrtStatistics,
            **kwargs
        )

    def list_by_srt_input_id(self, encoding_id, srt_input_id, query_params=None, **kwargs):
        # type: (string_types, string_types, SrtStatisticsListBySrtInputIdQueryParams, dict) -> SrtStatistics
        """List Statistics For SRT Live Stream Input

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param srt_input_id: Id of the SRT input.
        :type srt_input_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SrtStatisticsListBySrtInputIdQueryParams
        :return: List of statistics
        :rtype: SrtStatistics
        """

        return self.api_client.get(
            '/encoding/statistics/encodings/{encoding_id}/live-statistics/srt/{srt_input_id}',
            path_params={'encoding_id': encoding_id, 'srt_input_id': srt_input_id},
            query_params=query_params,
            pagination_response=True,
            type=SrtStatistics,
            **kwargs
        )
