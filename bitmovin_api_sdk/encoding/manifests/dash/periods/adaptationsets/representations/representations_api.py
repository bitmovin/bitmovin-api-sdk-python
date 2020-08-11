# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.vtt.vtt_api import VttApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.fmp4.fmp4_api import Fmp4Api
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.chunked_text.chunked_text_api import ChunkedTextApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.cmaf.cmaf_api import CmafApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.mp4.mp4_api import Mp4Api
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.webm.webm_api import WebmApi
from bitmovin_api_sdk.encoding.manifests.dash.periods.adaptationsets.representations.progressive_webm.progressive_webm_api import ProgressiveWebmApi


class RepresentationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(RepresentationsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.vtt = VttApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.fmp4 = Fmp4Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.chunked_text = ChunkedTextApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.cmaf = CmafApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mp4 = Mp4Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.webm = WebmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.progressive_webm = ProgressiveWebmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
