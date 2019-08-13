# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.analytics.ads.queries.count.count_api import CountApi
from bitmovin_api_sdk.analytics.ads.queries.sum.sum_api import SumApi
from bitmovin_api_sdk.analytics.ads.queries.avg.avg_api import AvgApi
from bitmovin_api_sdk.analytics.ads.queries.min.min_api import MinApi
from bitmovin_api_sdk.analytics.ads.queries.max.max_api import MaxApi
from bitmovin_api_sdk.analytics.ads.queries.stddev.stddev_api import StddevApi
from bitmovin_api_sdk.analytics.ads.queries.percentile.percentile_api import PercentileApi
from bitmovin_api_sdk.analytics.ads.queries.variance.variance_api import VarianceApi
from bitmovin_api_sdk.analytics.ads.queries.median.median_api import MedianApi


class QueriesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(QueriesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.count = CountApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.sum = SumApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.avg = AvgApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.min = MinApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.max = MaxApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.stddev = StddevApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.percentile = PercentileApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.variance = VarianceApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.median = MedianApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
