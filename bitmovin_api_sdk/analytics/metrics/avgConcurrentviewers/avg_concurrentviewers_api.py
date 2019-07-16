# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_avg_concurrent_viewers_response import AnalyticsAvgConcurrentViewersResponse
from bitmovin_api_sdk.models.analytics_metrics_query_request import AnalyticsMetricsQueryRequest
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class AvgConcurrentviewersApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AvgConcurrentviewersApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, analytics_metrics_query_request, **kwargs):
        # type: (AnalyticsMetricsQueryRequest, dict) -> AnalyticsAvgConcurrentViewersResponse
        """Get metrics data

        :param analytics_metrics_query_request: Analytics metrics query object
        :type analytics_metrics_query_request: AnalyticsMetricsQueryRequest, required
        :return: Service specific result
        :rtype: AnalyticsAvgConcurrentViewersResponse
        """

        return self.api_client.post(
            '/analytics/metrics/avg-concurrentviewers',
            analytics_metrics_query_request,
            type=AnalyticsAvgConcurrentViewersResponse,
            **kwargs
        )
