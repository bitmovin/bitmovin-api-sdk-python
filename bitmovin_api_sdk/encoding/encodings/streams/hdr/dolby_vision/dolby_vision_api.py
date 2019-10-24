# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dolby_vision_metadata import DolbyVisionMetadata
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.streams.hdr.dolby_vision.dolby_vision_metadata_list_query_params import DolbyVisionMetadataListQueryParams


class DolbyVisionApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DolbyVisionApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream_id, dolby_vision_metadata, **kwargs):
        # type: (string_types, string_types, DolbyVisionMetadata, dict) -> DolbyVisionMetadata
        """Add Dolby Vision Metadata

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param dolby_vision_metadata: The Dolby Vision Metadata to be added
        :type dolby_vision_metadata: DolbyVisionMetadata, required
        :return: Dolby Vision Metadata details
        :rtype: DolbyVisionMetadata
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/hdr/dolby-vision',
            dolby_vision_metadata,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=DolbyVisionMetadata,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, hdr_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Dolby Vision Metadata

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param hdr_id: Id of the Dolby Vision Metadata.
        :type hdr_id: string_types, required
        :return: Id of the Dolby Vision Metadata
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/hdr/dolby-vision/{hdr_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'hdr_id': hdr_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, hdr_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> DolbyVisionMetadata
        """Dolby Vision Metadata Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param hdr_id: Id of the Dolby Vision Metadata.
        :type hdr_id: string_types, required
        :return: Dolby Vision Metadata details
        :rtype: DolbyVisionMetadata
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/hdr/dolby-vision/{hdr_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'hdr_id': hdr_id},
            type=DolbyVisionMetadata,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params=None, **kwargs):
        # type: (string_types, string_types, DolbyVisionMetadataListQueryParams, dict) -> DolbyVisionMetadata
        """List Dolby Vision Metadata

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DolbyVisionMetadataListQueryParams
        :return: List of Dolby Vision Metadata
        :rtype: DolbyVisionMetadata
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/hdr/dolby-vision',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=DolbyVisionMetadata,
            **kwargs
        )
