# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.av1_video_configuration import Av1VideoConfiguration
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.video.av1.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.video.av1.av1_video_configuration_list_query_params import Av1VideoConfigurationListQueryParams


class Av1Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Av1Api, self).__init__(
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

    def create(self, av1_video_configuration, **kwargs):
        # type: (Av1VideoConfiguration, dict) -> Av1VideoConfiguration
        """Create AV1 Codec Configuration

        :param av1_video_configuration: The AV1 Codec Configuration to be created
        :type av1_video_configuration: Av1VideoConfiguration, required
        :return: AV1 video configuration
        :rtype: Av1VideoConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/video/av1',
            av1_video_configuration,
            type=Av1VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete AV1 Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/video/av1/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> Av1VideoConfiguration
        """AV1 Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: AV1 video configuration
        :rtype: Av1VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/av1/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Av1VideoConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (Av1VideoConfigurationListQueryParams, dict) -> Av1VideoConfiguration
        """List AV1 Codec Configurations

        :param query_params: Query parameters
        :type query_params: Av1VideoConfigurationListQueryParams
        :return: List of AV1 codec configurations
        :rtype: Av1VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/av1',
            query_params=query_params,
            pagination_response=True,
            type=Av1VideoConfiguration,
            **kwargs
        )
