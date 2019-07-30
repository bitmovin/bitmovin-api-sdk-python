# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.encoding.manifests.hls.media.custom_tags.custom_tags_api import CustomTagsApi
from bitmovin_api_sdk.encoding.manifests.hls.media.type.type_api import TypeApi
from bitmovin_api_sdk.encoding.manifests.hls.media.video.video_api import VideoApi
from bitmovin_api_sdk.encoding.manifests.hls.media.audio.audio_api import AudioApi
from bitmovin_api_sdk.encoding.manifests.hls.media.subtitles.subtitles_api import SubtitlesApi
from bitmovin_api_sdk.encoding.manifests.hls.media.vtt.vtt_api import VttApi
from bitmovin_api_sdk.encoding.manifests.hls.media.closed_captions.closed_captions_api import ClosedCaptionsApi


class MediaApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(MediaApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.custom_tags = CustomTagsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.type = TypeApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.video = VideoApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.audio = AudioApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.subtitles = SubtitlesApi(
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

        self.closed_captions = ClosedCaptionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
