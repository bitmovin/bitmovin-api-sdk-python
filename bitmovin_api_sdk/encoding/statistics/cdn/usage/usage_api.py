# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.cdn_usage_statistics import CdnUsageStatistics
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.statistics.cdn.usage.cdn_usage_statistics_get_query_params import CdnUsageStatisticsGetQueryParams


class UsageApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(UsageApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, query_params=None, **kwargs):
        # type: (CdnUsageStatisticsGetQueryParams, dict) -> CdnUsageStatistics
        """List CDN usage statistics within specific dates.

        :param query_params: Query parameters
        :type query_params: CdnUsageStatisticsGetQueryParams
        :return: CDN usage statistics.
        :rtype: CdnUsageStatistics
        """

        return self.api_client.get(
            '/encoding/statistics/cdn/usage',
            query_params=query_params,
            type=CdnUsageStatistics,
            **kwargs
        )
