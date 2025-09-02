# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.ai_scene_analysis.analyses.by_encoding_id.details.details_api import DetailsApi
from bitmovin_api_sdk.ai_scene_analysis.analyses.by_encoding_id.languages.languages_api import LanguagesApi
from bitmovin_api_sdk.ai_scene_analysis.analyses.by_encoding_id.ad_placements.ad_placements_api import AdPlacementsApi


class ByEncodingIdApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ByEncodingIdApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.details = DetailsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.languages = LanguagesApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.ad_placements = AdPlacementsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
