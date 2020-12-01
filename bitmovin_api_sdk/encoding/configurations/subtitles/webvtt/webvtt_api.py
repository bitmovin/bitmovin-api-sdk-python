# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.web_vtt_configuration import WebVttConfiguration
from bitmovin_api_sdk.encoding.configurations.subtitles.webvtt.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.subtitles.webvtt.web_vtt_configuration_list_query_params import WebVttConfigurationListQueryParams


class WebvttApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (WebVttConfiguration, dict) -> WebVttConfiguration
        """Create WebVtt subtitle configuration

        :param web_vtt_configuration: The WebVtt subtitle configuration to be created
        :type web_vtt_configuration: WebVttConfiguration, required
        :return: The created WebVtt subtitle configuration
        :rtype: WebVttConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/subtitles/webvtt',
            web_vtt_configuration,
            type=WebVttConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete WebVtt subtitle configuration

        :param configuration_id: Id of the subtitle configuration
        :type configuration_id: string_types, required
        :return: Id of the deleted configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/subtitles/webvtt/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> WebVttConfiguration
        """WebVtt subtitle configuration details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: WebVtt subtitle configuration
        :rtype: WebVttConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/subtitles/webvtt/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=WebVttConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (WebVttConfigurationListQueryParams, dict) -> WebVttConfiguration
        """List WebVtt subtitle configurations

        :param query_params: Query parameters
        :type query_params: WebVttConfigurationListQueryParams
        :return: List of WebVtt subtitle configurations
        :rtype: WebVttConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/subtitles/webvtt',
            query_params=query_params,
            pagination_response=True,
            type=WebVttConfiguration,
            **kwargs
        )
