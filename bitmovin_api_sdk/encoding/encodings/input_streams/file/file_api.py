# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.file_input_stream import FileInputStream
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.file.file_input_stream_list_query_params import FileInputStreamListQueryParams


class FileApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(FileApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, file_input_stream, **kwargs):
        # type: (string_types, FileInputStream, dict) -> FileInputStream
        """Add File input stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param file_input_stream: The File input stream to be created
        :type file_input_stream: FileInputStream, required
        :return: File input stream
        :rtype: FileInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/file',
            file_input_stream,
            path_params={'encoding_id': encoding_id},
            type=FileInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete File stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the File input stream.
        :type input_stream_id: string_types, required
        :return: Id of the File input stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/file/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> FileInputStream
        """File input stream details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the File input stream.
        :type input_stream_id: string_types, required
        :return: Stream
        :rtype: FileInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/file/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=FileInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, FileInputStreamListQueryParams, dict) -> FileInputStream
        """List File input stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: FileInputStreamListQueryParams
        :return: List of File input stream
        :rtype: FileInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/file',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=FileInputStream,
            **kwargs
        )
