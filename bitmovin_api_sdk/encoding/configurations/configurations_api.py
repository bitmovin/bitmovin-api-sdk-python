# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.codec_configuration import CodecConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.type.type_api import TypeApi
from bitmovin_api_sdk.encoding.configurations.video.video_api import VideoApi
from bitmovin_api_sdk.encoding.configurations.audio.audio_api import AudioApi
from bitmovin_api_sdk.encoding.configurations.subtitles.subtitles_api import SubtitlesApi
from bitmovin_api_sdk.encoding.configurations.codec_configuration_list_query_params import CodecConfigurationListQueryParams


class ConfigurationsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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

    def list(self, query_params=None, **kwargs):
        # type: (CodecConfigurationListQueryParams, dict) -> CodecConfiguration
        """List all Codec Configurations

        :param query_params: Query parameters
        :type query_params: CodecConfigurationListQueryParams
        :return: List of codec configurations with type information
        :rtype: CodecConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations',
            query_params=query_params,
            pagination_response=True,
            type=CodecConfiguration,
            **kwargs
        )
