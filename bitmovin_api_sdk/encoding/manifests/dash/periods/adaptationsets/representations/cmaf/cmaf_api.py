# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dash_cmaf_representation import DashCmafRepresentation
from bitmovin_api_sdk.models.dash_segmented_representation import DashSegmentedRepresentation
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.cmaf.contentprotection.contentprotection_api import ContentprotectionApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.cmaf.dash_cmaf_representation_list_query_params import DashCmafRepresentationListQueryParams


class CmafApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(CmafApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.contentprotection = ContentprotectionApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, manifest_id, period_id, adaptationset_id, dash_cmaf_representation, **kwargs):
        # type: (string_types, string_types, string_types, DashCmafRepresentation, dict) -> DashCmafRepresentation
        """Add CMAF Representation

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param dash_cmaf_representation: The CMAF representation to be added to the adaptation set
        :type dash_cmaf_representation: DashCmafRepresentation, required
        :return: Id of the CMAF representation
        :rtype: DashCmafRepresentation
        """

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf',
            dash_cmaf_representation,
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=DashCmafRepresentation,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        # type: (string_types, string_types, string_types, string_types, dict) -> BitmovinResponse
        """Delete CMAF Representation

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param representation_id: Id of the CMAF representation to be deleted
        :type representation_id: string_types, required
        :return: Id of the CMAF Representation
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        # type: (string_types, string_types, string_types, string_types, dict) -> DashCmafRepresentation
        """CMAF Representation Details

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param representation_id: Id of the representation
        :type representation_id: string_types, required
        :return: CMAF Representation details
        :rtype: DashCmafRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=DashCmafRepresentation,
            **kwargs
        )

    def list(self, manifest_id, period_id, adaptationset_id, query_params=None, **kwargs):
        # type: (string_types, string_types, string_types, DashCmafRepresentationListQueryParams, dict) -> DashCmafRepresentation
        """List all CMAF Representations

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DashCmafRepresentationListQueryParams
        :return: List of CMAF Representations
        :rtype: DashCmafRepresentation
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            query_params=query_params,
            pagination_response=True,
            type=DashCmafRepresentation,
            **kwargs
        )
