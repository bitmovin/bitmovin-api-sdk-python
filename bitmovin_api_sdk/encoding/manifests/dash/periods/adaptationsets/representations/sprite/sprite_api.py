# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.sprite_representation import SpriteRepresentation
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.sprite.sprite_representation_list_query_params import SpriteRepresentationListQueryParams


class SpriteApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SpriteApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, adaptationset_id, sprite_representation, **kwargs):
        # type: (string_types, string_types, string_types, SpriteRepresentation, dict) -> SpriteRepresentation
        """Add Sprite Representation

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param sprite_representation: The Sprite representation to be added to the adaptation set. Note that the adaptation set has to be an image adaptation set.  Only supported for sprites generated with encoder version &#x60;2.76.0&#x60; or above. 
        :type sprite_representation: SpriteRepresentation, required
        :return: Id of the Sprite representation
        :rtype: SpriteRepresentation
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/sprite',
            sprite_representation,
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=SpriteRepresentation,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        # type: (string_types, string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Sprite Representation

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param representation_id: Id of the Sprite representation to be deleted
        :type representation_id: string_types, required
        :return: Id of the Sprite Representation
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/sprite/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        # type: (string_types, string_types, string_types, string_types, dict) -> SpriteRepresentation
        """Sprite Representation Details

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param representation_id: Id of the Sprite representation
        :type representation_id: string_types, required
        :return: Sprite Representation details
        :rtype: SpriteRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/sprite/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=SpriteRepresentation,
            **kwargs
        )

    def list(self, manifest_id, period_id, adaptationset_id, query_params=None, **kwargs):
        # type: (string_types, string_types, string_types, SpriteRepresentationListQueryParams, dict) -> SpriteRepresentation
        """List all Sprite Representations

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param query_params: Query parameters
        :type query_params: SpriteRepresentationListQueryParams
        :return: List of Sprite Representations
        :rtype: SpriteRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/sprite',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            query_params=query_params,
            pagination_response=True,
            type=SpriteRepresentation,
            **kwargs
        )
