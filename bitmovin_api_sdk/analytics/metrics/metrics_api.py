# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.analytics.metrics.max_concurrentviewers.max_concurrentviewers_api import MaxConcurrentviewersApi
from bitmovin_api_sdk.analytics.metrics.avg_concurrentviewers.avg_concurrentviewers_api import AvgConcurrentviewersApi
from bitmovin_api_sdk.analytics.metrics.avg_dropped_frames.avg_dropped_frames_api import AvgDroppedFramesApi


class MetricsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(MetricsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.max_concurrentviewers = MaxConcurrentviewersApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.avg_concurrentviewers = AvgConcurrentviewersApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.avg_dropped_frames = AvgDroppedFramesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
