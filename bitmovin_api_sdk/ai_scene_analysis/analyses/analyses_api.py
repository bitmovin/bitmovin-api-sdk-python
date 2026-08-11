# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.scene_analysis_list_item import SceneAnalysisListItem
from bitmovin_api_sdk.models.scene_analysis_list_sort import SceneAnalysisListSort
from bitmovin_api_sdk.ai_scene_analysis.analyses.by_encoding_id.by_encoding_id_api import ByEncodingIdApi
from bitmovin_api_sdk.ai_scene_analysis.analyses.scene_analysis_list_item_list_query_params import SceneAnalysisListItemListQueryParams


class AnalysesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AnalysesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.by_encoding_id = ByEncodingIdApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, query_params=None, **kwargs):
        # type: (SceneAnalysisListItemListQueryParams, dict) -> SceneAnalysisListItem
        """List AI Scene Analyses

        :param query_params: Query parameters
        :type query_params: SceneAnalysisListItemListQueryParams
        :return: List of AI scene analyses
        :rtype: SceneAnalysisListItem
        """

        return self.api_client.get(
            '/ai-scene-analysis/analyses',
            query_params=query_params,
            pagination_response=True,
            type=SceneAnalysisListItem,
            **kwargs
        )
