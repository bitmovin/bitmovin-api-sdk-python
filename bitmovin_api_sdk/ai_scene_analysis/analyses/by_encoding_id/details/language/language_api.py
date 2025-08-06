# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.scene_analysis_details_response import SceneAnalysisDetailsResponse


class LanguageApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LanguageApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, language_code, **kwargs):
        # type: (string_types, string_types, dict) -> SceneAnalysisDetailsResponse
        """Get translated AI scene analysis details by encoding ID and language code

        :param encoding_id: The encoding ID
        :type encoding_id: string_types, required
        :param language_code: The language code
        :type language_code: string_types, required
        :return:
        :rtype: SceneAnalysisDetailsResponse
        """

        return self.api_client.get(
            '/ai-scene-analysis/analyses/by-encoding-id/{encoding_id}/details/language/{language_code}',
            path_params={'encoding_id': encoding_id, 'language_code': language_code},
            type=SceneAnalysisDetailsResponse,
            **kwargs
        )
