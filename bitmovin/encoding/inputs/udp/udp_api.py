# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.udp_input import UdpInput
from bitmovin.encoding.inputs.udp.udp_input_list_query_params import UdpInputListQueryParams


class UdpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(UdpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, input_id, **kwargs):
        """UDP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/udp/{input_id}',
            path_params={'input_id': input_id},
            type=UdpInput,
            **kwargs
        )

    def list(self, query_params: UdpInputListQueryParams = None, **kwargs):
        """List UDP inputs"""

        return self.api_client.get(
            '/encoding/inputs/udp',
            query_params=query_params,
            pagination_response=True,
            type=UdpInput,
            **kwargs
        )
