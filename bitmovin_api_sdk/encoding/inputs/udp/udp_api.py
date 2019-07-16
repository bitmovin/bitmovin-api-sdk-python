# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.udp_input import UdpInput
from bitmovin_api_sdk.encoding.inputs.udp.udp_input_list_query_params import UdpInputListQueryParams


class UdpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(UdpApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> UdpInput
        """UDP Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: UDP input
        :rtype: UdpInput
        """

        return self.api_client.get(
            '/encoding/inputs/udp/{input_id}',
            path_params={'input_id': input_id},
            type=UdpInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (UdpInputListQueryParams, dict) -> UdpInput
        """List UDP inputs

        :param query_params: Query parameters
        :type query_params: UdpInputListQueryParams
        :return: List of UDP inputs
        :rtype: UdpInput
        """

        return self.api_client.get(
            '/encoding/inputs/udp',
            query_params=query_params,
            pagination_response=True,
            type=UdpInput,
            **kwargs
        )
