# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.dns_mapping_response import DnsMappingResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.live.dns_mappings.dns_mapping_response_list_query_params import DnsMappingResponseListQueryParams


class DnsMappingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DnsMappingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params=None, **kwargs):
        # type: (DnsMappingResponseListQueryParams, dict) -> DnsMappingResponse
        """List DNS Mappings

        :param query_params: Query parameters
        :type query_params: DnsMappingResponseListQueryParams
        :return: List of DNS mappings
        :rtype: DnsMappingResponse
        """

        return self.api_client.get(
            '/encoding/live/dns-mappings',
            query_params=query_params,
            pagination_response=True,
            type=DnsMappingResponse,
            **kwargs
        )
