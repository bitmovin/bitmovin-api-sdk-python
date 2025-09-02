# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.scene_analysis_ad_placement_metadata_response import SceneAnalysisAdPlacementMetadataResponse


class AdPlacementsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AdPlacementsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> SceneAnalysisAdPlacementMetadataResponse
        """Get AI scene analysis ad placements by encoding ID

        :param encoding_id: The encoding ID
        :type encoding_id: string_types, required
        :return:
        :rtype: SceneAnalysisAdPlacementMetadataResponse
        """

        return self.api_client.get(
            '/ai-scene-analysis/analyses/by-encoding-id/{encoding_id}/ad-placements',
            path_params={'encoding_id': encoding_id},
            type=SceneAnalysisAdPlacementMetadataResponse,
            **kwargs
        )
