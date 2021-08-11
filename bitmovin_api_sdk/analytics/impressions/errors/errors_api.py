# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_error_details_response import AnalyticsErrorDetailsResponse
from bitmovin_api_sdk.models.analytics_license_key import AnalyticsLicenseKey
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class ErrorsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ErrorsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, impression_id, analytics_license_key, **kwargs):
        # type: (string_types, AnalyticsLicenseKey, dict) -> AnalyticsErrorDetailsResponse
        """Impression Error Details

        :param impression_id: Impression id
        :type impression_id: string_types, required
        :param analytics_license_key: Analytics license
        :type analytics_license_key: AnalyticsLicenseKey, required
        :return: List of error details for impression
        :rtype: AnalyticsErrorDetailsResponse
        """

        return self.api_client.post(
            '/analytics/impressions/{impression_id}/errors',
            analytics_license_key,
            path_params={'impression_id': impression_id},
            type=AnalyticsErrorDetailsResponse,
            **kwargs
        )
