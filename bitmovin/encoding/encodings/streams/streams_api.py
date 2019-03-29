# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.stream import Stream
from bitmovin.encoding.encodings.streams.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.streams.input.input_api import InputApi
from bitmovin.encoding.encodings.streams.inputs.inputs_api import InputsApi
from bitmovin.encoding.encodings.streams.filters.filters_api import FiltersApi
from bitmovin.encoding.encodings.streams.subtitles.subtitles_api import SubtitlesApi
from bitmovin.encoding.encodings.streams.burnInSubtitles.burn_in_subtitles_api import BurnInSubtitlesApi
from bitmovin.encoding.encodings.streams.captions.captions_api import CaptionsApi
from bitmovin.encoding.encodings.streams.thumbnails.thumbnails_api import ThumbnailsApi
from bitmovin.encoding.encodings.streams.sprites.sprites_api import SpritesApi
from bitmovin.encoding.encodings.streams.stream_list_query_params import StreamListQueryParams


class StreamsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(StreamsApi, self).__init__(
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

        self.input = InputApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.inputs = InputsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.filters = FiltersApi(
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

        self.burnInSubtitles = BurnInSubtitlesApi(
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

        self.thumbnails = ThumbnailsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.sprites = SpritesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream, **kwargs):
        """Add Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams',
            stream,
            path_params={'encoding_id': encoding_id},
            type=Stream,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, **kwargs):
        """Delete Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, **kwargs):
        """Stream Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=Stream,
            **kwargs
        )

    def list(self, encoding_id, query_params: StreamListQueryParams = None, **kwargs):
        """List Streams"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Stream,
            **kwargs
        )
