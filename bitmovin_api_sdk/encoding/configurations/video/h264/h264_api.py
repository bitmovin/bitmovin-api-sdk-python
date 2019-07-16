# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.h264_video_configuration import H264VideoConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.video.h264.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.video.h264.h264_video_configuration_list_query_params import H264VideoConfigurationListQueryParams


class H264Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(H264Api, self).__init__(
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

    def create(self, h264_video_configuration, **kwargs):
        # type: (H264VideoConfiguration, dict) -> H264VideoConfiguration
        """Create H264/AVC Codec Configuration

        :param h264_video_configuration: The H264/AVC Codec Configuration to be created
        :type h264_video_configuration: H264VideoConfiguration, required
        :return: H264/AVC video configuration
        :rtype: H264VideoConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/video/h264',
            h264_video_configuration,
            type=H264VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete H264/AVC Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/video/h264/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> H264VideoConfiguration
        """H264/AVC Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: H264/AVC video configuration
        :rtype: H264VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/h264/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=H264VideoConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (H264VideoConfigurationListQueryParams, dict) -> H264VideoConfiguration
        """List H264/AVC Codec Configurations

        :param query_params: Query parameters
        :type query_params: H264VideoConfigurationListQueryParams
        :return: List of H264/AVC codec configurations
        :rtype: H264VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/h264',
            query_params=query_params,
            pagination_response=True,
            type=H264VideoConfiguration,
            **kwargs
        )
