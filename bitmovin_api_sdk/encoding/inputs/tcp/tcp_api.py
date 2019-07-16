# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.tcp_input import TcpInput
from bitmovin_api_sdk.encoding.inputs.tcp.tcp_input_list_query_params import TcpInputListQueryParams


class TcpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TcpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> TcpInput
        """TCP Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: TCP input
        :rtype: TcpInput
        """

        return self.api_client.get(
            '/encoding/inputs/tcp/{input_id}',
            path_params={'input_id': input_id},
            type=TcpInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (TcpInputListQueryParams, dict) -> TcpInput
        """List TCP inputs

        :param query_params: Query parameters
        :type query_params: TcpInputListQueryParams
        :return: List of TCP inputs
        :rtype: TcpInput
        """

        return self.api_client.get(
            '/encoding/inputs/tcp',
            query_params=query_params,
            pagination_response=True,
            type=TcpInput,
            **kwargs
        )
