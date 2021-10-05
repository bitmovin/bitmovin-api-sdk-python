# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dolby_vision_input_stream import DolbyVisionInputStream
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.dolby_vision.dolby_vision_input_stream_list_query_params import DolbyVisionInputStreamListQueryParams


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

    def create(self, encoding_id, dolby_vision_input_stream, **kwargs):
        # type: (string_types, DolbyVisionInputStream, dict) -> DolbyVisionInputStream
        """Add Dolby Vision input stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param dolby_vision_input_stream: The Dolby Vision input stream to be created
        :type dolby_vision_input_stream: DolbyVisionInputStream, required
        :return: Dolby Vision input stream
        :rtype: DolbyVisionInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/dolby-vision',
            dolby_vision_input_stream,
            path_params={'encoding_id': encoding_id},
            type=DolbyVisionInputStream,
            **kwargs
        )

    def delete(self, encoding_id, dolby_vision_input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Dolby Vision input stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param dolby_vision_input_stream_id: Id of the Dolby Vision input stream.
        :type dolby_vision_input_stream_id: string_types, required
        :return: Id of the Dolby Vision input stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/dolby-vision/{dolby_vision_input_stream_id}',
            path_params={'encoding_id': encoding_id, 'dolby_vision_input_stream_id': dolby_vision_input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, dolby_vision_input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> DolbyVisionInputStream
        """Dolby Vision input stream details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param dolby_vision_input_stream_id: Id of the Dolby Vision input stream.
        :type dolby_vision_input_stream_id: string_types, required
        :return: Dolby Vision input stream
        :rtype: DolbyVisionInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/dolby-vision/{dolby_vision_input_stream_id}',
            path_params={'encoding_id': encoding_id, 'dolby_vision_input_stream_id': dolby_vision_input_stream_id},
            type=DolbyVisionInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, DolbyVisionInputStreamListQueryParams, dict) -> DolbyVisionInputStream
        """List Dolby Vision input stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DolbyVisionInputStreamListQueryParams
        :return: List of Dolby Vision input stream
        :rtype: DolbyVisionInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/dolby-vision',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=DolbyVisionInputStream,
            **kwargs
        )
