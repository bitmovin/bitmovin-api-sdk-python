# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.aac_audio_configuration import AacAudioConfiguration
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.aac.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.aac.aac_audio_configuration_list_query_params import AacAudioConfigurationListQueryParams


class AacApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AacApi, self).__init__(
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

    def create(self, aac_audio_configuration, **kwargs):
        # type: (AacAudioConfiguration, dict) -> AacAudioConfiguration
        """Create AAC Codec Configuration

        :param aac_audio_configuration: The AAC Codec Configuration to be created
        :type aac_audio_configuration: AacAudioConfiguration, required
        :return: AAC Audio Configuration
        :rtype: AacAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/aac',
            aac_audio_configuration,
            type=AacAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete AAC Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/aac/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> AacAudioConfiguration
        """AAC Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: AAC Audio Configuration
        :rtype: AacAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/aac/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=AacAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AacAudioConfigurationListQueryParams, dict) -> AacAudioConfiguration
        """List AAC Configurations

        :param query_params: Query parameters
        :type query_params: AacAudioConfigurationListQueryParams
        :return: List of AAC codec configuration ids
        :rtype: AacAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/aac',
            query_params=query_params,
            pagination_response=True,
            type=AacAudioConfiguration,
            **kwargs
        )
