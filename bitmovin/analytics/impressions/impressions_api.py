# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.analytics_impression_details import AnalyticsImpressionDetails
from bitmovin.models.analytics_license import AnalyticsLicense
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError


class ImpressionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ImpressionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, impression_id, analytics_license, **kwargs):
        """Impression Details"""

        return self.api_client.post(
            '/analytics/impressions/{impression_id}',
            analytics_license,
            path_params={'impression_id': impression_id},
            type=AnalyticsImpressionDetails,
            **kwargs
        )
