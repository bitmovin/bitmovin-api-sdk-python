# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.codec_configuration import CodecConfiguration
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.configurations.type.type_api import TypeApi
from bitmovin.encoding.configurations.video.video_api import VideoApi
from bitmovin.encoding.configurations.audio.audio_api import AudioApi
from bitmovin.encoding.configurations.subtitles.subtitles_api import SubtitlesApi
from bitmovin.encoding.configurations.codec_configuration_list_query_params import CodecConfigurationListQueryParams


class ConfigurationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(ConfigurationsApi, self).__init__(
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

    def list(self, query_params: CodecConfigurationListQueryParams = None, **kwargs):
        """List all Codec Configurations"""

        return self.api_client.get(
            '/encoding/configurations',
            query_params=query_params,
            pagination_response=True,
            type=CodecConfiguration,
            **kwargs
        )
