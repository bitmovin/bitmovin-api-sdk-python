# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.stream import Stream
from bitmovin_api_sdk.encoding.encodings.streams.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.streams.input.input_api import InputApi
from bitmovin_api_sdk.encoding.encodings.streams.inputs.inputs_api import InputsApi
from bitmovin_api_sdk.encoding.encodings.streams.filters.filters_api import FiltersApi
from bitmovin_api_sdk.encoding.encodings.streams.burn_in_subtitles.burn_in_subtitles_api import BurnInSubtitlesApi
from bitmovin_api_sdk.encoding.encodings.streams.captions.captions_api import CaptionsApi
from bitmovin_api_sdk.encoding.encodings.streams.bifs.bifs_api import BifsApi
from bitmovin_api_sdk.encoding.encodings.streams.hdr.hdr_api import HdrApi
from bitmovin_api_sdk.encoding.encodings.streams.thumbnails.thumbnails_api import ThumbnailsApi
from bitmovin_api_sdk.encoding.encodings.streams.sprites.sprites_api import SpritesApi
from bitmovin_api_sdk.encoding.encodings.streams.qc.qc_api import QcApi
from bitmovin_api_sdk.encoding.encodings.streams.stream_list_query_params import StreamListQueryParams


class StreamsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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

        self.burn_in_subtitles = BurnInSubtitlesApi(
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

        self.bifs = BifsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.hdr = HdrApi(
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

        self.qc = QcApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream, **kwargs):
        # type: (string_types, Stream, dict) -> Stream
        """Add Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream: The Stream to be created
        :type stream: Stream, required
        :return: Stream
        :rtype: Stream
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams',
            stream,
            path_params={'encoding_id': encoding_id},
            type=Stream,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :return: Id of the stream
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> Stream
        """Stream Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :return: Stream
        :rtype: Stream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=Stream,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, StreamListQueryParams, dict) -> Stream
        """List Streams

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: StreamListQueryParams
        :return: List of streams
        :rtype: Stream
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Stream,
            **kwargs
        )
