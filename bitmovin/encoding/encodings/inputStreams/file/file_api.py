# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.file_input_stream import FileInputStream
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.inputStreams.file.file_input_stream_list_query_params import FileInputStreamListQueryParams


class FileApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(FileApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, file_input_stream, **kwargs):
        """Add File input stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/file',
            file_input_stream,
            path_params={'encoding_id': encoding_id},
            type=FileInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        """Delete File stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/file/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """File input stream details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/file/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=FileInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params: FileInputStreamListQueryParams = None, **kwargs):
        """List File input stream"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/file',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=FileInputStream,
            **kwargs
        )
