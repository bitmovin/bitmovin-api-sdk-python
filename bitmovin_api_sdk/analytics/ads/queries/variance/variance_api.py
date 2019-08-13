# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.ad_analytics_query_request import AdAnalyticsQueryRequest
from bitmovin_api_sdk.models.ad_analytics_variance_query_request import AdAnalyticsVarianceQueryRequest
from bitmovin_api_sdk.models.analytics_response import AnalyticsResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class VarianceApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(VarianceApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, ad_analytics_variance_query_request, **kwargs):
        # type: (AdAnalyticsVarianceQueryRequest, dict) -> AnalyticsResponse
        """Variance

        :param ad_analytics_variance_query_request: Analytics Query Object
        :type ad_analytics_variance_query_request: AdAnalyticsVarianceQueryRequest, required
        :return: Service specific result
        :rtype: AnalyticsResponse
        """

        return self.api_client.post(
            '/analytics/ads/queries/variance',
            ad_analytics_variance_query_request,
            type=AnalyticsResponse,
            **kwargs
        )
