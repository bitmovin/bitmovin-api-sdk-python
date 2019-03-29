# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.audio_mix_input_stream import AudioMixInputStream
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.inputStreams.audioMix.audio_mix_input_stream_list_query_params import AudioMixInputStreamListQueryParams


class AudioMixApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AudioMixApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, audio_mix_input_stream, **kwargs):
        """Add audio mix input stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/audio-mix',
            audio_mix_input_stream,
            path_params={'encoding_id': encoding_id},
            type=AudioMixInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        """Delete audio mix input stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/audio-mix/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """Audio mix input stream details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/audio-mix/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=AudioMixInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params: AudioMixInputStreamListQueryParams = None, **kwargs):
        """List audio mix input stream"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/audio-mix',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=AudioMixInputStream,
            **kwargs
        )
