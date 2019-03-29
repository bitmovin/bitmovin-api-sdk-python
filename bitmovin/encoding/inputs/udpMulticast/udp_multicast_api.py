# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.udp_multicast_input import UdpMulticastInput
from bitmovin.encoding.inputs.udpMulticast.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.inputs.udpMulticast.udp_multicast_input_list_query_params import UdpMulticastInputListQueryParams


class UdpMulticastApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
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
        """Create UDP multicast input"""

        return self.api_client.post(
            '/encoding/inputs/udp-multicast',
            udp_multicast_input,
            type=UdpMulticastInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete UDP multicast input"""

        return self.api_client.delete(
            '/encoding/inputs/udp-multicast/{input_id}',
            path_params={'input_id': input_id},
            type=UdpMulticastInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """UDP multicast Input Details"""

        return self.api_client.get(
            '/encoding/inputs/udp-multicast/{input_id}',
            path_params={'input_id': input_id},
            type=UdpMulticastInput,
            **kwargs
        )

    def list(self, query_params: UdpMulticastInputListQueryParams = None, **kwargs):
        """List UDP multicast inputs"""

        return self.api_client.get(
            '/encoding/inputs/udp-multicast',
            query_params=query_params,
            pagination_response=True,
            type=UdpMulticastInput,
            **kwargs
        )
