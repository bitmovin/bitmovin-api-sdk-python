# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.ai_scene_analysis_live_result import AiSceneAnalysisLiveResult
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class LatestApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LatestApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, analysis_id, **kwargs):
        # type: (string_types, dict) -> AiSceneAnalysisLiveResult
        """Get Live Analysis Latest Result

        :param analysis_id: ID of the Live Analysis
        :type analysis_id: string_types, required
        :return:
        :rtype: AiSceneAnalysisLiveResult
        """

        return self.api_client.get(
            '/ai-scene-analysis/live-analyses/{analysis_id}/results/latest',
            path_params={'analysis_id': analysis_id},
            type=AiSceneAnalysisLiveResult,
            **kwargs
        )
