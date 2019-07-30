# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.audio_mix_input_stream import AudioMixInputStream
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.audio_mix.audio_mix_input_stream_list_query_params import AudioMixInputStreamListQueryParams


class AudioMixApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AudioMixApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, audio_mix_input_stream, **kwargs):
        # type: (string_types, AudioMixInputStream, dict) -> AudioMixInputStream
        """Add audio mix input stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param audio_mix_input_stream: The audio mix input stream to be created
        :type audio_mix_input_stream: AudioMixInputStream, required
        :return: Audio mix input stream
        :rtype: AudioMixInputStream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/audio-mix',
            audio_mix_input_stream,
            path_params={'encoding_id': encoding_id},
            type=AudioMixInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete audio mix input stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the audio mix input stream.
        :type input_stream_id: string_types, required
        :return: Id of the audio mix input stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/audio-mix/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> AudioMixInputStream
        """Audio mix input stream details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the audio mix input stream.
        :type input_stream_id: string_types, required
        :return: Stream
        :rtype: AudioMixInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/audio-mix/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=AudioMixInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, AudioMixInputStreamListQueryParams, dict) -> AudioMixInputStream
        """List audio mix input stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: AudioMixInputStreamListQueryParams
        :return: List of audio mix input stream
        :rtype: AudioMixInputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/audio-mix',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=AudioMixInputStream,
            **kwargs
        )
