# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.resource_limit_container import ResourceLimitContainer
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class LimitsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LimitsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, **kwargs):
        # type: (dict) -> ResourceLimitContainer
        """Organization Limits

        :return: Limits grouped by affected resources
        :rtype: ResourceLimitContainer
        """

        return self.api_client.get(
            '/account/limits',
            pagination_response=True,
            type=ResourceLimitContainer,
            **kwargs
        )
