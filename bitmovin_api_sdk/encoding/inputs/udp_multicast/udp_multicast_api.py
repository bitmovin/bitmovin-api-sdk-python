# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.udp_multicast_input import UdpMulticastInput
from bitmovin_api_sdk.encoding.inputs.udp_multicast.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.udp_multicast.udp_multicast_input_list_query_params import UdpMulticastInputListQueryParams


class UdpMulticastApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(UdpMulticastApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, udp_multicast_input, **kwargs):
        # type: (UdpMulticastInput, dict) -> UdpMulticastInput
        """Create UDP multicast input

        :param udp_multicast_input: The UdpMulticastInput to be created
        :type udp_multicast_input: UdpMulticastInput, required
        :return: UDP multicast input
        :rtype: UdpMulticastInput
        """

        return self.api_client.post(
            '/encoding/inputs/udp-multicast',
            udp_multicast_input,
            type=UdpMulticastInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> UdpMulticastInput
        """Delete UDP multicast input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: UdpMulticastInput
        """

        return self.api_client.delete(
            '/encoding/inputs/udp-multicast/{input_id}',
            path_params={'input_id': input_id},
            type=UdpMulticastInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> UdpMulticastInput
        """UDP multicast Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: UDP multicast input
        :rtype: UdpMulticastInput
        """

        return self.api_client.get(
            '/encoding/inputs/udp-multicast/{input_id}',
            path_params={'input_id': input_id},
            type=UdpMulticastInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (UdpMulticastInputListQueryParams, dict) -> UdpMulticastInput
        """List UDP multicast inputs

        :param query_params: Query parameters
        :type query_params: UdpMulticastInputListQueryParams
        :return: List of UDP multicast inputs
        :rtype: UdpMulticastInput
        """

        return self.api_client.get(
            '/encoding/inputs/udp-multicast',
            query_params=query_params,
            pagination_response=True,
            type=UdpMulticastInput,
            **kwargs
        )
