# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.vp8_video_configuration import Vp8VideoConfiguration
from bitmovin_api_sdk.encoding.configurations.video.vp8.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.video.vp8.vp8_video_configuration_list_query_params import Vp8VideoConfigurationListQueryParams


class Vp8Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Vp8Api, self).__init__(
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

    def create(self, vp8_video_configuration, **kwargs):
        # type: (Vp8VideoConfiguration, dict) -> Vp8VideoConfiguration
        """Create VP8 Codec Configuration

        :param vp8_video_configuration: The VP8 Codec Configuration to be created
        :type vp8_video_configuration: Vp8VideoConfiguration, required
        :return: VP8 video configuration
        :rtype: Vp8VideoConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/video/vp8',
            vp8_video_configuration,
            type=Vp8VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete VP8 Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/video/vp8/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> Vp8VideoConfiguration
        """VP8 Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: VP8 video configuration
        :rtype: Vp8VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/vp8/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Vp8VideoConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (Vp8VideoConfigurationListQueryParams, dict) -> Vp8VideoConfiguration
        """get_encoding_configurations_video_vp8

        :param query_params: Query parameters
        :type query_params: Vp8VideoConfigurationListQueryParams
        :return: List of VP8 codec configurations
        :rtype: Vp8VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/vp8',
            query_params=query_params,
            pagination_response=True,
            type=Vp8VideoConfiguration,
            **kwargs
        )
