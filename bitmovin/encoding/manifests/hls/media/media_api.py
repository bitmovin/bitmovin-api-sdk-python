# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except
from bitmovin.encoding.manifests.hls.media.customTags.custom_tags_api import CustomTagsApi
from bitmovin.encoding.manifests.hls.media.type.type_api import TypeApi
from bitmovin.encoding.manifests.hls.media.video.video_api import VideoApi
from bitmovin.encoding.manifests.hls.media.audio.audio_api import AudioApi
from bitmovin.encoding.manifests.hls.media.subtitles.subtitles_api import SubtitlesApi
from bitmovin.encoding.manifests.hls.media.vtt.vtt_api import VttApi
from bitmovin.encoding.manifests.hls.media.closedCaptions.closed_captions_api import ClosedCaptionsApi


class MediaApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(MediaApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customTags = CustomTagsApi(
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

        self.closedCaptions = ClosedCaptionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
