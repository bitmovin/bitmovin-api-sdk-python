# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.h265_v2_video_configuration import H265V2VideoConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.video.h265v2.h265_v2_video_configuration_list_query_params import H265V2VideoConfigurationListQueryParams


class H265v2Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(H265v2Api, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, h265_v2_video_configuration, **kwargs):
        # type: (H265V2VideoConfiguration, dict) -> H265V2VideoConfiguration
        """Create H265 V2 Codec Configuration

        :param h265_v2_video_configuration: The H265 V2 Codec Configuration to be created
        :type h265_v2_video_configuration: H265V2VideoConfiguration, required
        :return: H265 V2 video configuration
        :rtype: H265V2VideoConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/video/h265v2',
            h265_v2_video_configuration,
            type=H265V2VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete H265 V2 Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/video/h265v2/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> H265V2VideoConfiguration
        """H265 V2 Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: H265 V2 video configuration
        :rtype: H265V2VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/h265v2/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=H265V2VideoConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (H265V2VideoConfigurationListQueryParams, dict) -> H265V2VideoConfiguration
        """List H265 V2 Codec Configurations

        :param query_params: Query parameters
        :type query_params: H265V2VideoConfigurationListQueryParams
        :return: List of H265 V2 codec configurations
        :rtype: H265V2VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/h265v2',
            query_params=query_params,
            pagination_response=True,
            type=H265V2VideoConfiguration,
            **kwargs
        )
