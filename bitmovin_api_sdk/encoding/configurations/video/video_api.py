# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.encoding.configurations.video.h262.h262_api import H262Api
from bitmovin_api_sdk.encoding.configurations.video.h264.h264_api import H264Api
from bitmovin_api_sdk.encoding.configurations.video.h265.h265_api import H265Api
from bitmovin_api_sdk.encoding.configurations.video.vp8.vp8_api import Vp8Api
from bitmovin_api_sdk.encoding.configurations.video.vp9.vp9_api import Vp9Api
from bitmovin_api_sdk.encoding.configurations.video.av1.av1_api import Av1Api
from bitmovin_api_sdk.encoding.configurations.video.mjpeg.mjpeg_api import MjpegApi


class VideoApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(VideoApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.h262 = H262Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.h264 = H264Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.h265 = H265Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.vp8 = Vp8Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.vp9 = Vp9Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.av1 = Av1Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mjpeg = MjpegApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
