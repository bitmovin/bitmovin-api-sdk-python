# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.encoding.configurations.audio.aac.aac_api import AacApi
from bitmovin_api_sdk.encoding.configurations.audio.dts_passthrough.dts_passthrough_api import DtsPassthroughApi
from bitmovin_api_sdk.encoding.configurations.audio.dolby_atmos.dolby_atmos_api import DolbyAtmosApi
from bitmovin_api_sdk.encoding.configurations.audio.he_aac_v1.he_aac_v1_api import HeAacV1Api
from bitmovin_api_sdk.encoding.configurations.audio.he_aac_v2.he_aac_v2_api import HeAacV2Api
from bitmovin_api_sdk.encoding.configurations.audio.vorbis.vorbis_api import VorbisApi
from bitmovin_api_sdk.encoding.configurations.audio.opus.opus_api import OpusApi
from bitmovin_api_sdk.encoding.configurations.audio.pcm.pcm_api import PcmApi
from bitmovin_api_sdk.encoding.configurations.audio.ac3.ac3_api import Ac3Api
from bitmovin_api_sdk.encoding.configurations.audio.eac3.eac3_api import Eac3Api
from bitmovin_api_sdk.encoding.configurations.audio.mp2.mp2_api import Mp2Api
from bitmovin_api_sdk.encoding.configurations.audio.mp3.mp3_api import Mp3Api


class AudioApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AudioApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.aac = AacApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.dts_passthrough = DtsPassthroughApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.dolby_atmos = DolbyAtmosApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.he_aac_v1 = HeAacV1Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.he_aac_v2 = HeAacV2Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.vorbis = VorbisApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.opus = OpusApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.pcm = PcmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.ac3 = Ac3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.eac3 = Eac3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mp2 = Mp2Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mp3 = Mp3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
