# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dash_imsc_representation import DashImscRepresentation
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.imsc.dash_imsc_representation_list_query_params import DashImscRepresentationListQueryParams


class ImscApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ImscApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, adaptationset_id, dash_imsc_representation, **kwargs):
        # type: (string_types, string_types, string_types, DashImscRepresentation, dict) -> DashImscRepresentation
        """Add IMSC Representation

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the subtitle adaptation set
        :type adaptationset_id: string_types, required
        :param dash_imsc_representation: The IMSC representation to be added to the adaptation set. Note that the adaptation set has to be a subtitle adaptation set. 
        :type dash_imsc_representation: DashImscRepresentation, required
        :return: Imsc representation
        :rtype: DashImscRepresentation
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/imsc',
            dash_imsc_representation,
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=DashImscRepresentation,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        # type: (string_types, string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete IMSC Representation

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param representation_id: Id of the IMSC representation to be deleted
        :type representation_id: string_types, required
        :return: Id of the IMSC Representation
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/imsc/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        # type: (string_types, string_types, string_types, string_types, dict) -> DashImscRepresentation
        """IMSC Representation Details

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param representation_id: Id of the IMSC representation
        :type representation_id: string_types, required
        :return: IMSC Representation details
        :rtype: DashImscRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/imsc/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=DashImscRepresentation,
            **kwargs
        )

    def list(self, manifest_id, period_id, adaptationset_id, query_params=None, **kwargs):
        # type: (string_types, string_types, string_types, DashImscRepresentationListQueryParams, dict) -> DashImscRepresentation
        """List all IMSC Representations

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DashImscRepresentationListQueryParams
        :return: List of IMSC Representations
        :rtype: DashImscRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/imsc',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            query_params=query_params,
            pagination_response=True,
            type=DashImscRepresentation,
            **kwargs
        )
