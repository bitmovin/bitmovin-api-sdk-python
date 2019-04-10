# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.dash_cmaf_drm_representation import DashCmafDrmRepresentation
from bitmovin.models.dash_fmp4_drm_representation import DashFmp4DrmRepresentation
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.manifests.dash.periods.adaptationsets.representations.cmaf.drm.contentprotection.contentprotection_api import ContentprotectionApi
from bitmovin.encoding.manifests.dash.periods.adaptationsets.representations.cmaf.drm.dash_cmaf_drm_representation_list_query_params import DashCmafDrmRepresentationListQueryParams


class DrmApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(DrmApi, self).__init__(
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

    def create(self, manifest_id, period_id, adaptationset_id, dash_cmaf_drm_representation, **kwargs):
        """Add DRM CMAF Representation"""

        return self.api_client.post(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf/drm',
            dash_cmaf_drm_representation,
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            type=DashCmafDrmRepresentation,
            **kwargs
        )

    def delete(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        """Delete DRM CMAF Representation"""

        return self.api_client.delete(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf/drm/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, manifest_id, period_id, adaptationset_id, representation_id, **kwargs):
        """DRM CMAF Representation Details"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf/drm/{representation_id}',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id, 'representation_id': representation_id},
            type=DashCmafDrmRepresentation,
            **kwargs
        )

    def list(self, manifest_id, period_id, adaptationset_id, query_params: DashCmafDrmRepresentationListQueryParams = None, **kwargs):
        """List all DRM CMAF Representations"""

        return self.api_client.get(
            '/encoding/manifests/dash/{manifest_id}/periods/{period_id}/adaptationsets/{adaptationset_id}/representations/cmaf/drm',
            path_params={'manifest_id': manifest_id, 'period_id': period_id, 'adaptationset_id': adaptationset_id},
            query_params=query_params,
            pagination_response=True,
            type=DashCmafDrmRepresentation,
            **kwargs
        )
