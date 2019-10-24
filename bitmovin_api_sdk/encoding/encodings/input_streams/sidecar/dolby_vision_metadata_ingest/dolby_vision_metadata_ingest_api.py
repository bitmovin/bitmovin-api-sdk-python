# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dolby_vision_metadata_ingest_input_stream import DolbyVisionMetadataIngestInputStream
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.sidecar.dolby_vision_metadata_ingest.dolby_vision_metadata_ingest_input_stream_list_query_params import DolbyVisionMetadataIngestInputStreamListQueryParams


class DolbyVisionMetadataIngestApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DolbyVisionMetadataIngestApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, dolby_vision_metadata_ingest_input_stream, **kwargs):
        # type: (string_types, DolbyVisionMetadataIngestInputStream, dict) -> DolbyVisionMetadataIngestInputStream
        """Add Dolby Vision Metadata Ingest Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param dolby_vision_metadata_ingest_input_stream: The Dolby Vision Metadata Ingest Input Stream to be created
        :type dolby_vision_metadata_ingest_input_stream: DolbyVisionMetadataIngestInputStream, required
        :return: Dolby Vision Metadata Ingest Input Stream
        :rtype: DolbyVisionMetadataIngestInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/sidecar/dolby-vision-metadata-ingest',
            dolby_vision_metadata_ingest_input_stream,
            path_params={'encoding_id': encoding_id},
            type=DolbyVisionMetadataIngestInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Dolby Vision Metadata Ingest Input Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the Dolby Vision Metadata Ingest input stream.
        :type input_stream_id: string_types, required
        :return: Id of the Dolby Vision Metadata Ingest input stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/sidecar/dolby-vision-metadata-ingest/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> DolbyVisionMetadataIngestInputStream
        """Dolby Vision Metadata Ingest Input Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the Dolby Vision Metadata Ingest input stream.
        :type input_stream_id: string_types, required
        :return: Dolby Vision Metadata Ingest Input Stream
        :rtype: DolbyVisionMetadataIngestInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/sidecar/dolby-vision-metadata-ingest/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=DolbyVisionMetadataIngestInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, DolbyVisionMetadataIngestInputStreamListQueryParams, dict) -> DolbyVisionMetadataIngestInputStream
        """List Dolby Vision Metadata Ingest Input Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DolbyVisionMetadataIngestInputStreamListQueryParams
        :return: List of Dolby Vision Ingest Metadata input streams
        :rtype: DolbyVisionMetadataIngestInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/sidecar/dolby-vision-metadata-ingest',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=DolbyVisionMetadataIngestInputStream,
            **kwargs
        )
