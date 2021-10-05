# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.input_stream import InputStream
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.input_streams.type.type_api import TypeApi
from bitmovin_api_sdk.encoding.encodings.input_streams.audio_mix.audio_mix_api import AudioMixApi
from bitmovin_api_sdk.encoding.encodings.input_streams.ingest.ingest_api import IngestApi
from bitmovin_api_sdk.encoding.encodings.input_streams.sidecar.sidecar_api import SidecarApi
from bitmovin_api_sdk.encoding.encodings.input_streams.concatenation.concatenation_api import ConcatenationApi
from bitmovin_api_sdk.encoding.encodings.input_streams.file.file_api import FileApi
from bitmovin_api_sdk.encoding.encodings.input_streams.trimming.trimming_api import TrimmingApi
from bitmovin_api_sdk.encoding.encodings.input_streams.subtitles.subtitles_api import SubtitlesApi
from bitmovin_api_sdk.encoding.encodings.input_streams.captions.captions_api import CaptionsApi
from bitmovin_api_sdk.encoding.encodings.input_streams.dolby_atmos.dolby_atmos_api import DolbyAtmosApi
from bitmovin_api_sdk.encoding.encodings.input_streams.dolby_vision.dolby_vision_api import DolbyVisionApi
from bitmovin_api_sdk.encoding.encodings.input_streams.input_stream_list_query_params import InputStreamListQueryParams


class InputStreamsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(InputStreamsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.type = TypeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.audio_mix = AudioMixApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.ingest = IngestApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.sidecar = SidecarApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.concatenation = ConcatenationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.file = FileApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.trimming = TrimmingApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.subtitles = SubtitlesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.captions = CaptionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.dolby_atmos = DolbyAtmosApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.dolby_vision = DolbyVisionApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> InputStream
        """Input Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param input_stream_id: Id of the input stream.
        :type input_stream_id: string_types, required
        :return: Input stream
        :rtype: InputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=InputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, InputStreamListQueryParams, dict) -> InputStream
        """List All Input Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: InputStreamListQueryParams
        :return: List of all input streams
        :rtype: InputStream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=InputStream,
            **kwargs
        )
