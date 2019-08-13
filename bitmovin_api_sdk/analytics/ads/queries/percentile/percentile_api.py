# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.ad_analytics_percentile_query_request import AdAnalyticsPercentileQueryRequest
from bitmovin_api_sdk.models.analytics_response import AnalyticsResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class PercentileApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PercentileApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, ad_analytics_percentile_query_request, **kwargs):
        # type: (AdAnalyticsPercentileQueryRequest, dict) -> AnalyticsResponse
        """Percentile

        :param ad_analytics_percentile_query_request: Analytics Query Object
        :type ad_analytics_percentile_query_request: AdAnalyticsPercentileQueryRequest, required
        :return: Service specific result
        :rtype: AnalyticsResponse
        """

        return self.api_client.post(
            '/analytics/ads/queries/percentile',
            ad_analytics_percentile_query_request,
            type=AnalyticsResponse,
            **kwargs
        )
