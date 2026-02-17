# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.bitmovin_response_list import BitmovinResponseList
from bitmovin_api_sdk.models.dns_mapping_request import DnsMappingRequest
from bitmovin_api_sdk.models.dns_mapping_response import DnsMappingResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.live.encodings.dns_mappings.dns_mapping_response_list_query_params import DnsMappingResponseListQueryParams


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

    def create(self, encoding_id, dns_mapping_request, **kwargs):
        # type: (string_types, DnsMappingRequest, dict) -> DnsMappingResponse
        """Create new DNS mapping for encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param dns_mapping_request: The DNS mapping to be created
        :type dns_mapping_request: DnsMappingRequest, required
        :return:
        :rtype: DnsMappingResponse
        """

        return self.api_client.post(
            '/encoding/live/encodings/{encoding_id}/dns-mappings',
            dns_mapping_request,
            path_params={'encoding_id': encoding_id},
            type=DnsMappingResponse,
            **kwargs
        )

    def delete(self, encoding_id, id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete DNS mapping

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param id: Id of the DNS mapping
        :type id: string_types, required
        :return: Id of the DNS mapping that was deleted
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/live/encodings/{encoding_id}/dns-mappings/{id}',
            path_params={'encoding_id': encoding_id, 'id': id},
            type=BitmovinResponse,
            **kwargs
        )

    def delete_all(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponseList
        """Delete all DNS mappings for encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :return: List of ids of deleted DNS mappings
        :rtype: BitmovinResponseList
        """

        return self.api_client.delete(
            '/encoding/live/encodings/{encoding_id}/dns-mappings',
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponseList,
            **kwargs
        )

    def get(self, encoding_id, id, **kwargs):
        # type: (string_types, string_types, dict) -> DnsMappingResponse
        """DNS mapping details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param id: Id of the DNS mapping
        :type id: string_types, required
        :return: DNS mapping
        :rtype: DnsMappingResponse
        """

        return self.api_client.get(
            '/encoding/live/encodings/{encoding_id}/dns-mappings/{id}',
            path_params={'encoding_id': encoding_id, 'id': id},
            type=DnsMappingResponse,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, DnsMappingResponseListQueryParams, dict) -> DnsMappingResponse
        """List DNS mappings for encoding

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DnsMappingResponseListQueryParams
        :return: List of DNS mappings
        :rtype: DnsMappingResponse
        """

        return self.api_client.get(
            '/encoding/live/encodings/{encoding_id}/dns-mappings',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=DnsMappingResponse,
            **kwargs
        )
