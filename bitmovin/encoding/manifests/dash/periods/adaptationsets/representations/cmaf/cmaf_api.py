# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.dash_cmaf_representation import DashCmafRepresentation
from bitmovin.models.dash_fmp4_representation import DashFmp4Representation
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.manifests.dash.periods.adaptationsets.representations.cmaf.drm.drm_api import DrmApi
from bitmovin.encoding.manifests.dash.periods.adaptationsets.representations.cmaf.contentprotection.contentprotection_api import ContentprotectionApi
from bitmovin.encoding.manifests.dash.periods.adaptationsets.representations.cmaf.dash_cmaf_representation_list_query_params import DashCmafRepresentationListQueryParams


class CmafApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(CmafApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.drm = DrmApi(
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
        """Add CMAF Representation"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf',
            dash_cmaf_representation,
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=DashCmafRepresentation,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        """Delete CMAF Representation"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        """CMAF Representation Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=DashCmafRepresentation,
            **kwargs
        )

    def list(self, manifest_id, period_id, adaptationset_id, query_params: DashCmafRepresentationListQueryParams = None, **kwargs):
        """List all CMAF Representations"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            query_params=query_params,
            pagination_response=True,
            type=DashCmafRepresentation,
            **kwargs
        )
