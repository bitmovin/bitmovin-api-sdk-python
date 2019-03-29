# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except
from bitmovin.encoding.configurations.video.h264.h264_api import H264Api
from bitmovin.encoding.configurations.video.h265.h265_api import H265Api
from bitmovin.encoding.configurations.video.vp8.vp8_api import Vp8Api
from bitmovin.encoding.configurations.video.vp9.vp9_api import Vp9Api
from bitmovin.encoding.configurations.video.av1.av1_api import Av1Api
from bitmovin.encoding.configurations.video.mjpeg.mjpeg_api import MjpegApi


class VideoApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(VideoApi, self).__init__(
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
