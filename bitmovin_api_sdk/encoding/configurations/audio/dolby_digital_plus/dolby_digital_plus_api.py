# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dolby_digital_plus_audio_configuration import DolbyDigitalPlusAudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.dolby_digital_plus.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.dolby_digital_plus.dolby_digital_plus_audio_configuration_list_query_params import DolbyDigitalPlusAudioConfigurationListQueryParams


class DolbyDigitalPlusApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DolbyDigitalPlusApi, self).__init__(
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

    def create(self, dolby_digital_plus_audio_configuration, **kwargs):
        # type: (DolbyDigitalPlusAudioConfiguration, dict) -> DolbyDigitalPlusAudioConfiguration
        """Create Dolby Digital Plus Codec Configuration

        :param dolby_digital_plus_audio_configuration: The Dolby Digital Plus Codec Configuration to be created (Dolby Encoder v3.17).  Dolby Digital Plus enables high-resolution multichannel audio at lower bit rates than with Dolby Digital. 
        :type dolby_digital_plus_audio_configuration: DolbyDigitalPlusAudioConfiguration, required
        :return: Dolby Digital Plus Audio Configuration
        :rtype: DolbyDigitalPlusAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/dolby-digital-plus',
            dolby_digital_plus_audio_configuration,
            type=DolbyDigitalPlusAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Dolby Digital Plus Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/dolby-digital-plus/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> DolbyDigitalPlusAudioConfiguration
        """Dolby Digital Plus Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Dolby Digital Plus Audio Configuration
        :rtype: DolbyDigitalPlusAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dolby-digital-plus/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=DolbyDigitalPlusAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DolbyDigitalPlusAudioConfigurationListQueryParams, dict) -> DolbyDigitalPlusAudioConfiguration
        """List Dolby Digital Plus Codec Configurations

        :param query_params: Query parameters
        :type query_params: DolbyDigitalPlusAudioConfigurationListQueryParams
        :return: List of Dolby Digital Plus codec configurations
        :rtype: DolbyDigitalPlusAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dolby-digital-plus',
            query_params=query_params,
            pagination_response=True,
            type=DolbyDigitalPlusAudioConfiguration,
            **kwargs
        )
