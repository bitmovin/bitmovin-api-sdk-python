# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.dash_representation_type_response import DashRepresentationTypeResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.type.dash_representation_type_response_get_query_params import DashRepresentationTypeResponseGetQueryParams


class TypeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TypeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, manifest_id, period_id, adaptationset_id, representation_id, query_params=None, **kwargs):
        # type: (string_types, string_types, string_types, string_types, DashRepresentationTypeResponseGetQueryParams, dict) -> DashRepresentationTypeResponse
        """Get DASH representation type

        :param manifest_id: Id of the manifest
        :type manifest_id: string_types, required
        :param period_id: Id of the period
        :type period_id: string_types, required
        :param adaptationset_id: Id of the adaptation set
        :type adaptationset_id: string_types, required
        :param representation_id: Id of the representation
        :type representation_id: string_types, required
        :param query_params: Query parameters
        :type query_params: DashRepresentationTypeResponseGetQueryParams
        :return: DASH representation type response
        :rtype: DashRepresentationTypeResponse
        """

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/{representation_id}/type',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            query_params=query_params,
            type=DashRepresentationTypeResponse,
            **kwargs
        )
