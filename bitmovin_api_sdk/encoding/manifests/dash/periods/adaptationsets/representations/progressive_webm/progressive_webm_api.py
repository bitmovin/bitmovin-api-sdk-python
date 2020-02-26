# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dash_progressive_webm_representation import DashProgressiveWebmRepresentation
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.progressive_webm.dash_progressive_webm_representation_list_query_params import DashProgressiveWebmRepresentationListQueryParams


class ProgressiveWebmApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ProgressiveWebmApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, adaptationset_id, dash_progressive_webm_representation, **kwargs):
        # type: (string_types, string_types, string_types, DashProgressiveWebmRepresentation, dict) -> DashProgressiveWebmRepresentation
        """Add Progressive WebM Representation

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param dash_progressive_webm_representation: The Progressive WebM representation to be added to the adaptation set
        :type dash_progressive_webm_representation: DashProgressiveWebmRepresentation, required
        :return: Id of the Progressive WebM representation
        :rtype: DashProgressiveWebmRepresentation
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/progressive-webm',
            dash_progressive_webm_representation,
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=DashProgressiveWebmRepresentation,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        # type: (string_types, string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete Progressive WebM Representation

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param representation_id: Id of the Progressive WebM representation to be deleted
        :type representation_id: string_types, required
        :return: Id of the Progressive WebM Representation
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/progressive-webm/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        # type: (string_types, string_types, string_types, string_types, dict) -> DashProgressiveWebmRepresentation
        """Progressive WebM Representation Details

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param representation_id: Id of the representation
        :type representation_id: string_types, required
        :return: Progressive WebM Representation details
        :rtype: DashProgressiveWebmRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/progressive-webm/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=DashProgressiveWebmRepresentation,
            **kwargs
        )

    def list(self, manifest_id, period_id, adaptationset_id, query_params=None, **kwargs):
        # type: (string_types, string_types, string_types, DashProgressiveWebmRepresentationListQueryParams, dict) -> DashProgressiveWebmRepresentation
        """List all Progressive WebM Representations

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DashProgressiveWebmRepresentationListQueryParams
        :return: List of Progressive WebM Representations
        :rtype: DashProgressiveWebmRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/progressive-webm',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            query_params=query_params,
            pagination_response=True,
            type=DashProgressiveWebmRepresentation,
            **kwargs
        )
