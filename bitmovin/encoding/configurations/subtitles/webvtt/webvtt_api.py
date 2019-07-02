# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_resource import BitmovinResource
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.web_vtt_configuration import WebVttConfiguration
from bitmovin.encoding.configurations.subtitles.webvtt.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.configurations.subtitles.webvtt.web_vtt_configuration_list_query_params import WebVttConfigurationListQueryParams


class WebvttApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(WebvttApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, web_vtt_configuration, **kwargs):
        """Create WebVtt Subtitle Configuration"""

        return self.api_client.post(
            '/encoding/configurations/subtitles/webvtt/',
            web_vtt_configuration,
            type=WebVttConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete WebVtt Subtitle Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/subtitles/webvtt/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """WebVtt Subtitle Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/subtitles/webvtt/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=WebVttConfiguration,
            **kwargs
        )

    def list(self, query_params: WebVttConfigurationListQueryParams = None, **kwargs):
        """List WebVtt Configurations"""

        return self.api_client.get(
            '/encoding/configurations/subtitles/webvtt/',
            query_params=query_params,
            pagination_response=True,
            type=WebVttConfiguration,
            **kwargs
        )
