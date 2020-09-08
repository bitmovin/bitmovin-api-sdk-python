# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.h262_video_configuration import H262VideoConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.video.h262.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.video.h262.h262_video_configuration_list_query_params import H262VideoConfigurationListQueryParams


class H262Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(H262Api, self).__init__(
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

    def create(self, h262_video_configuration, **kwargs):
        # type: (H262VideoConfiguration, dict) -> H262VideoConfiguration
        """Create H262 Codec Configuration

        :param h262_video_configuration: The H262 Codec Configuration to be created
        :type h262_video_configuration: H262VideoConfiguration, required
        :return: H262 video configuration
        :rtype: H262VideoConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/video/h262',
            h262_video_configuration,
            type=H262VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete H262 Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/video/h262/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> H262VideoConfiguration
        """H262 Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: H262 video configuration
        :rtype: H262VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/h262/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=H262VideoConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (H262VideoConfigurationListQueryParams, dict) -> H262VideoConfiguration
        """List H262 Codec Configurations

        :param query_params: Query parameters
        :type query_params: H262VideoConfigurationListQueryParams
        :return: List of H262 codec configurations
        :rtype: H262VideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/h262',
            query_params=query_params,
            pagination_response=True,
            type=H262VideoConfiguration,
            **kwargs
        )
