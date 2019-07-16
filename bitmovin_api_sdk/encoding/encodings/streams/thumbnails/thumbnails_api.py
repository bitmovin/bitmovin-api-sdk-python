# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.thumbnail import Thumbnail
from bitmovin_api_sdk.encoding.encodings.streams.thumbnails.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.streams.thumbnails.thumbnail_list_query_params import ThumbnailListQueryParams


class ThumbnailsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ThumbnailsApi, self).__init__(
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

    def create(self, encoding_id, stream_id, thumbnail, **kwargs):
        # type: (string_types, string_types, Thumbnail, dict) -> Thumbnail
        """Add Thumbnail

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param thumbnail: The Thumbnail to be added
        :type thumbnail: Thumbnail, required
        :return: Thumbnail details
        :rtype: Thumbnail
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/thumbnails',
            thumbnail,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=Thumbnail,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, thumbnail_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Thumbnail

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param thumbnail_id: Id of the thumbnail.
        :type thumbnail_id: string_types, required
        :return: Id of the thumbnail
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/thumbnails/{thumbnail_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'thumbnail_id': thumbnail_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, thumbnail_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> Thumbnail
        """Thumbnail Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param thumbnail_id: Id of the thumbnail.
        :type thumbnail_id: string_types, required
        :return: Thumbnail details
        :rtype: Thumbnail
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/thumbnails/{thumbnail_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'thumbnail_id': thumbnail_id},
            type=Thumbnail,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params=None, **kwargs):
        # type: (string_types, string_types, ThumbnailListQueryParams, dict) -> Thumbnail
        """List Thumbnails

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ThumbnailListQueryParams
        :return: List of thumbnails
        :rtype: Thumbnail
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/thumbnails',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=Thumbnail,
            **kwargs
        )
