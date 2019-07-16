# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.vp9_video_configuration import Vp9VideoConfiguration
from bitmovin_api_sdk.encoding.configurations.video.vp9.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.video.vp9.vp9_video_configuration_list_query_params import Vp9VideoConfigurationListQueryParams


class Vp9Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Vp9Api, self).__init__(
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

    def create(self, vp9_video_configuration, **kwargs):
        # type: (Vp9VideoConfiguration, dict) -> Vp9VideoConfiguration
        """Create VP9 Codec Configuration

        :param vp9_video_configuration: The VP9 Codec Configuration to be created
        :type vp9_video_configuration: Vp9VideoConfiguration, required
        :return: VP9 video configuration
        :rtype: Vp9VideoConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/video/vp9',
            vp9_video_configuration,
            type=Vp9VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete VP9 Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/video/vp9/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> Vp9VideoConfiguration
        """VP9 Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: VP9 video configuration
        :rtype: Vp9VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/vp9/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Vp9VideoConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (Vp9VideoConfigurationListQueryParams, dict) -> Vp9VideoConfiguration
        """List VP9 Codec Configurations

        :param query_params: Query parameters
        :type query_params: Vp9VideoConfigurationListQueryParams
        :return: List of VP9 codec configurations
        :rtype: Vp9VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/vp9',
            query_params=query_params,
            pagination_response=True,
            type=Vp9VideoConfiguration,
            **kwargs
        )
