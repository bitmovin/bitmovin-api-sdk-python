# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.encoding.encodings.inputStreams.trimming.timeBased.time_based_api import TimeBasedApi
from bitmovin_api_sdk.encoding.encodings.inputStreams.trimming.timecodeTrack.timecode_track_api import TimecodeTrackApi
from bitmovin_api_sdk.encoding.encodings.inputStreams.trimming.h264PictureTiming.h264_picture_timing_api import H264PictureTimingApi


class TrimmingApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TrimmingApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.timeBased = TimeBasedApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.timecodeTrack = TimecodeTrackApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.h264PictureTiming = H264PictureTimingApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
