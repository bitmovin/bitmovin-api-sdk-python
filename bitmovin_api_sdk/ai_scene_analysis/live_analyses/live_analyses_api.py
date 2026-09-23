# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.ai_scene_analysis_live_create_request import AiSceneAnalysisLiveCreateRequest
from bitmovin_api_sdk.models.ai_scene_analysis_live_response import AiSceneAnalysisLiveResponse
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.ai_scene_analysis.live_analyses.results.results_api import ResultsApi
from bitmovin_api_sdk.ai_scene_analysis.live_analyses.ai_scene_analysis_live_response_list_query_params import AiSceneAnalysisLiveResponseListQueryParams


class LiveAnalysesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LiveAnalysesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.results = ResultsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, ai_scene_analysis_live_create_request, **kwargs):
        # type: (AiSceneAnalysisLiveCreateRequest, dict) -> AiSceneAnalysisLiveResponse
        """Create Live Analysis

        :param ai_scene_analysis_live_create_request: Live Analysis configuration
        :type ai_scene_analysis_live_create_request: AiSceneAnalysisLiveCreateRequest, required
        :return: Created Live Analysis
        :rtype: AiSceneAnalysisLiveResponse
        """

        return self.api_client.post(
            '/ai-scene-analysis/live-analyses',
            ai_scene_analysis_live_create_request,
            type=AiSceneAnalysisLiveResponse,
            **kwargs
        )

    def delete(self, analysis_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Live Analysis

        :param analysis_id: ID of the Live Analysis
        :type analysis_id: string_types, required
        :return: ID of the deleted Live Analysis
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/ai-scene-analysis/live-analyses/{analysis_id}',
            path_params={'analysis_id': analysis_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, analysis_id, **kwargs):
        # type: (string_types, dict) -> AiSceneAnalysisLiveResponse
        """Get Live Analysis details

        :param analysis_id: ID of the Live Analysis
        :type analysis_id: string_types, required
        :return: Live Analysis
        :rtype: AiSceneAnalysisLiveResponse
        """

        return self.api_client.get(
            '/ai-scene-analysis/live-analyses/{analysis_id}',
            path_params={'analysis_id': analysis_id},
            type=AiSceneAnalysisLiveResponse,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AiSceneAnalysisLiveResponseListQueryParams, dict) -> AiSceneAnalysisLiveResponse
        """List Live Analyses

        :param query_params: Query parameters
        :type query_params: AiSceneAnalysisLiveResponseListQueryParams
        :return: Live Analyses
        :rtype: AiSceneAnalysisLiveResponse
        """

        return self.api_client.get(
            '/ai-scene-analysis/live-analyses',
            query_params=query_params,
            pagination_response=True,
            type=AiSceneAnalysisLiveResponse,
            **kwargs
        )

    def start(self, analysis_id, **kwargs):
        # type: (string_types, dict) -> AiSceneAnalysisLiveResponse
        """Start Live Analysis

        :param analysis_id: ID of the Live Analysis
        :type analysis_id: string_types, required
        :return:
        :rtype: AiSceneAnalysisLiveResponse
        """

        return self.api_client.post(
            '/ai-scene-analysis/live-analyses/{analysis_id}/start',
            path_params={'analysis_id': analysis_id},
            type=AiSceneAnalysisLiveResponse,
            **kwargs
        )

    def stop(self, analysis_id, **kwargs):
        # type: (string_types, dict) -> AiSceneAnalysisLiveResponse
        """Stop Live Analysis

        :param analysis_id: ID of the Live Analysis
        :type analysis_id: string_types, required
        :return:
        :rtype: AiSceneAnalysisLiveResponse
        """

        return self.api_client.post(
            '/ai-scene-analysis/live-analyses/{analysis_id}/stop',
            path_params={'analysis_id': analysis_id},
            type=AiSceneAnalysisLiveResponse,
            **kwargs
        )
