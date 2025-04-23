# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.encoding.encodings.streams.burn_in_subtitles.dvbsub.dvbsub_api import DvbsubApi
from bitmovin_api_sdk.encoding.encodings.streams.burn_in_subtitles.srt.srt_api import SrtApi
from bitmovin_api_sdk.encoding.encodings.streams.burn_in_subtitles.assa.assa_api import AssaApi


class BurnInSubtitlesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(BurnInSubtitlesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.dvbsub = DvbsubApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.srt = SrtApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.assa = AssaApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
