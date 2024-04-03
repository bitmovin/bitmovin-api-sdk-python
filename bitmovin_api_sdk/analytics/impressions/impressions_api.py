# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_impressions_query import AnalyticsImpressionsQuery
from bitmovin_api_sdk.models.analytics_impressions_response import AnalyticsImpressionsResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.analytics.impressions.ads.ads_api import AdsApi
from bitmovin_api_sdk.analytics.impressions.errors.errors_api import ErrorsApi


class ImpressionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ImpressionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.ads = AdsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.errors = ErrorsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get_impressions(self, analytics_impressions_query, **kwargs):
        # type: (AnalyticsImpressionsQuery, dict) -> AnalyticsImpressionsResponse
        """List impressions

        :param analytics_impressions_query: Analytics impressions query object
        :type analytics_impressions_query: AnalyticsImpressionsQuery, required
        :return: List of Impressions
        :rtype: AnalyticsImpressionsResponse
        """

        return self.api_client.post(
            '/analytics/impressions',
            analytics_impressions_query,
            type=AnalyticsImpressionsResponse,
            **kwargs
        )
