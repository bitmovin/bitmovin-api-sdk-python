# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dolby_digital_audio_configuration import DolbyDigitalAudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.dolby_digital.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.dolby_digital.dolby_digital_audio_configuration_list_query_params import DolbyDigitalAudioConfigurationListQueryParams


class DolbyDigitalApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DolbyDigitalApi, self).__init__(
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

    def create(self, dolby_digital_audio_configuration, **kwargs):
        # type: (DolbyDigitalAudioConfiguration, dict) -> DolbyDigitalAudioConfiguration
        """Create Dolby Digital Codec Configuration

        :param dolby_digital_audio_configuration: The Dolby Digital Codec Configuration to be created (Dolby Encoder v3.17)
        :type dolby_digital_audio_configuration: DolbyDigitalAudioConfiguration, required
        :return: Dolby Digital Audio Configuration
        :rtype: DolbyDigitalAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/dolby-digital',
            dolby_digital_audio_configuration,
            type=DolbyDigitalAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Dolby Digital Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/dolby-digital/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> DolbyDigitalAudioConfiguration
        """Dolby Digital Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Dolby Digital Audio Configuration
        :rtype: DolbyDigitalAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dolby-digital/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=DolbyDigitalAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DolbyDigitalAudioConfigurationListQueryParams, dict) -> DolbyDigitalAudioConfiguration
        """List Dolby Digital Codec Configurations

        :param query_params: Query parameters
        :type query_params: DolbyDigitalAudioConfigurationListQueryParams
        :return: List of Dolby Digital codec configurations
        :rtype: DolbyDigitalAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dolby-digital',
            query_params=query_params,
            pagination_response=True,
            type=DolbyDigitalAudioConfiguration,
            **kwargs
        )
