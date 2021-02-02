# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.nex_guard_file_marker import NexGuardFileMarker
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.streams.watermarking.nexguard_file_marker.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.streams.watermarking.nexguard_file_marker.nex_guard_file_marker_list_query_params import NexGuardFileMarkerListQueryParams


class NexguardFileMarkerApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(NexguardFileMarkerApi, self).__init__(
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

    def create(self, encoding_id, stream_id, nex_guard_file_marker, **kwargs):
        # type: (string_types, string_types, NexGuardFileMarker, dict) -> NexGuardFileMarker
        """Add a nexguard file marker watermarking configurations

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param nex_guard_file_marker: The nexguard file marker configurations
        :type nex_guard_file_marker: NexGuardFileMarker, required
        :return: Nexguard file marker configurations details
        :rtype: NexGuardFileMarker
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/watermarking/nexguard-file-marker',
            nex_guard_file_marker,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=NexGuardFileMarker,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, nexguard_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete nexguard file marker watermarking configurations

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param nexguard_id: Id of the nexguard file marker watermarking configurations
        :type nexguard_id: string_types, required
        :return: Id of the nexguard file marker watermarking configurations.
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/watermarking/nexguard-file-marker/{nexguard_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'nexguard_id': nexguard_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, nexguard_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> NexGuardFileMarker
        """Nexguard file marker watermarking configurations details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param nexguard_id: Id of the nexguard file marker watermarking configurations.
        :type nexguard_id: string_types, required
        :return: Nexguard file marker watermarking configurations details
        :rtype: NexGuardFileMarker
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/watermarking/nexguard-file-marker/{nexguard_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'nexguard_id': nexguard_id},
            type=NexGuardFileMarker,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params=None, **kwargs):
        # type: (string_types, string_types, NexGuardFileMarkerListQueryParams, dict) -> NexGuardFileMarker
        """List nexguard file marker watermarking configurations

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param query_params: Query parameters
        :type query_params: NexGuardFileMarkerListQueryParams
        :return: List of nexguard file marker watermarking configurations
        :rtype: NexGuardFileMarker
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/watermarking/nexguard-file-marker',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=NexGuardFileMarker,
            **kwargs
        )
