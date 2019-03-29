# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.tcp_input import TcpInput
from bitmovin.encoding.inputs.tcp.tcp_input_list_query_params import TcpInputListQueryParams


class TcpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TcpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, input_id, **kwargs):
        """TCP Input Details"""

        return self.api_client.get(
            '/encoding/inputs/tcp/{input_id}',
            path_params={'input_id': input_id},
            type=TcpInput,
            **kwargs
        )

    def list(self, query_params: TcpInputListQueryParams = None, **kwargs):
        """List TCP inputs"""

        return self.api_client.get(
            '/encoding/inputs/tcp',
            query_params=query_params,
            pagination_response=True,
            type=TcpInput,
            **kwargs
        )
