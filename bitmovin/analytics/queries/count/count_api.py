# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.analytics_count_query_request import AnalyticsCountQueryRequest
from bitmovin.models.analytics_query_request import AnalyticsQueryRequest
from bitmovin.models.analytics_response import AnalyticsResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class CountApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CountApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, analytics_count_query_request, **kwargs):
        """Count"""

        return self.api_client.post(
            '/analytics/queries/count',
            analytics_count_query_request,
            type=AnalyticsResponse,
            **kwargs
        )
