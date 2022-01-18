# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.static_ip import StaticIp
from bitmovin_api_sdk.encoding.infrastructure.static_ips.static_ip_list_query_params import StaticIpListQueryParams


class StaticIpsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(StaticIpsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, static_ip, **kwargs):
        # type: (StaticIp, dict) -> StaticIp
        """Add Static IP Address

        :param static_ip: The static ip to be created
        :type static_ip: StaticIp, required
        :return: Static IP Address
        :rtype: StaticIp
        """

        return self.api_client.post(
            '/encoding/infrastructure/static-ips',
            static_ip,
            type=StaticIp,
            **kwargs
        )

    def delete(self, id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Static IP Address

        :param id: Id of the Static IP Address
        :type id: string_types, required
        :return: Id of the Static IP Address
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/infrastructure/static-ips/{id}',
            path_params={'id': id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, id, **kwargs):
        # type: (string_types, dict) -> StaticIp
        """Static IP Address Details

        :param id: Id of the Static IP Address
        :type id: string_types, required
        :return: Static IP Address
        :rtype: StaticIp
        """

        return self.api_client.get(
            '/encoding/infrastructure/static-ips/{id}',
            path_params={'id': id},
            type=StaticIp,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (StaticIpListQueryParams, dict) -> StaticIp
        """List all Static IP Addresses

        :param query_params: Query parameters
        :type query_params: StaticIpListQueryParams
        :return: All Static IP Addresses.
        :rtype: StaticIp
        """

        return self.api_client.get(
            '/encoding/infrastructure/static-ips',
            query_params=query_params,
            pagination_response=True,
            type=StaticIp,
            **kwargs
        )
