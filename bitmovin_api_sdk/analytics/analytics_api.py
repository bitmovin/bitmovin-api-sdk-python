# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.analytics.exports.exports_api import ExportsApi
from bitmovin_api_sdk.analytics.impressions.impressions_api import ImpressionsApi
from bitmovin_api_sdk.analytics.insights.insights_api import InsightsApi
from bitmovin_api_sdk.analytics.metrics.metrics_api import MetricsApi
from bitmovin_api_sdk.analytics.ads.ads_api import AdsApi
from bitmovin_api_sdk.analytics.queries.queries_api import QueriesApi
from bitmovin_api_sdk.analytics.licenses.licenses_api import LicensesApi
from bitmovin_api_sdk.analytics.outputs.outputs_api import OutputsApi
from bitmovin_api_sdk.analytics.alerting.alerting_api import AlertingApi


class AnalyticsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AnalyticsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.exports = ExportsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.impressions = ImpressionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.insights = InsightsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.metrics = MetricsApi(
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

        self.queries = QueriesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.licenses = LicensesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.outputs = OutputsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.alerting = AlertingApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
