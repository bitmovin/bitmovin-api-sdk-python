# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.sprite import Sprite
from bitmovin_api_sdk.encoding.encodings.streams.sprites.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.streams.sprites.sprite_list_query_params import SpriteListQueryParams


class SpritesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SpritesApi, self).__init__(
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

    def create(self, encoding_id, stream_id, sprite, **kwargs):
        # type: (string_types, string_types, Sprite, dict) -> Sprite
        """Add Sprite

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param sprite: The Sprite to be added
        :type sprite: Sprite, required
        :return: Sprite details
        :rtype: Sprite
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/sprites',
            sprite,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=Sprite,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, sprite_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Sprite

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param sprite_id: Id of the sprite.
        :type sprite_id: string_types, required
        :return: Id of the sprite
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/sprites/{sprite_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'sprite_id': sprite_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, sprite_id, **kwargs):
        # type: (string_types, string_types, string_types, dict) -> Sprite
        """Sprite Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param sprite_id: Id of the sprite configuration.
        :type sprite_id: string_types, required
        :return: Sprite details
        :rtype: Sprite
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/sprites/{sprite_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'sprite_id': sprite_id},
            type=Sprite,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params=None, **kwargs):
        # type: (string_types, string_types, SpriteListQueryParams, dict) -> Sprite
        """List Sprites

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SpriteListQueryParams
        :return: List of sprites
        :rtype: Sprite
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/sprites',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=Sprite,
            **kwargs
        )
