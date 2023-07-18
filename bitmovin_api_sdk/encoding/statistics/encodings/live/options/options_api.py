# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.live_encoding_options_statistics import LiveEncodingOptionsStatistics
from bitmovin_api_sdk.models.live_options_statistics import LiveOptionsStatistics
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.statistics.encodings.live.options.live_options_statistics_list_by_date_range_query_params import LiveOptionsStatisticsListByDateRangeQueryParams


class OptionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(OptionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> LiveEncodingOptionsStatistics
        """List live options encoding statistics for a given encoding

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :return:
        :rtype: LiveEncodingOptionsStatistics
        """

        return self.api_client.get(
            '/encoding/statistics/encodings/live/{encoding_id}/options',
            path_params={'encoding_id': encoding_id},
            type=LiveEncodingOptionsStatistics,
            **kwargs
        )

    def list_by_date_range(self, query_params=None, **kwargs):
        # type: (LiveOptionsStatisticsListByDateRangeQueryParams, dict) -> LiveOptionsStatistics
        """List live options encoding statistics within specific dates

        :param query_params: Query parameters
        :type query_params: LiveOptionsStatisticsListByDateRangeQueryParams
        :return:
        :rtype: LiveOptionsStatistics
        """

        return self.api_client.get(
            '/encoding/statistics/encodings/live/options',
            query_params=query_params,
            type=LiveOptionsStatistics,
            **kwargs
        )
