# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_avg_dropped_frames_response import AnalyticsAvgDroppedFramesResponse
from bitmovin_api_sdk.models.analytics_metrics_query_request import AnalyticsMetricsQueryRequest
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class AvgDroppedFramesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AvgDroppedFramesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, analytics_metrics_query_request, **kwargs):
        # type: (AnalyticsMetricsQueryRequest, dict) -> AnalyticsAvgDroppedFramesResponse
        """Get metrics data

        :param analytics_metrics_query_request: Analytics metrics query object
        :type analytics_metrics_query_request: AnalyticsMetricsQueryRequest, required
        :return: Service specific result
        :rtype: AnalyticsAvgDroppedFramesResponse
        """

        return self.api_client.post(
            '/analytics/metrics/avg-dropped-frames',
            analytics_metrics_query_request,
            type=AnalyticsAvgDroppedFramesResponse,
            **kwargs
        )
