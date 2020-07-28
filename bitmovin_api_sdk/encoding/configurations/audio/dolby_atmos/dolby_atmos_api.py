# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dolby_atmos_audio_configuration import DolbyAtmosAudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.dolby_atmos.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.dolby_atmos.dolby_atmos_audio_configuration_list_query_params import DolbyAtmosAudioConfigurationListQueryParams


class DolbyAtmosApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DolbyAtmosApi, self).__init__(
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

    def create(self, dolby_atmos_audio_configuration, **kwargs):
        # type: (DolbyAtmosAudioConfiguration, dict) -> DolbyAtmosAudioConfiguration
        """Create Dolby Atmos Configuration

        :param dolby_atmos_audio_configuration: The Dolby Atmos Codec Configuration to be created
        :type dolby_atmos_audio_configuration: DolbyAtmosAudioConfiguration, required
        :return: Dolby Atmos Audio Configuration
        :rtype: DolbyAtmosAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/dolby-atmos',
            dolby_atmos_audio_configuration,
            type=DolbyAtmosAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Dolby Atmos Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/dolby-atmos/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> DolbyAtmosAudioConfiguration
        """Dolby Atmos Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Dolby Atmos Audio Configuration
        :rtype: DolbyAtmosAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dolby-atmos/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=DolbyAtmosAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DolbyAtmosAudioConfigurationListQueryParams, dict) -> DolbyAtmosAudioConfiguration
        """List Dolby Atmos Configurations

        :param query_params: Query parameters
        :type query_params: DolbyAtmosAudioConfigurationListQueryParams
        :return: List of Dolby Atmos codec configuration ids
        :rtype: DolbyAtmosAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dolby-atmos',
            query_params=query_params,
            pagination_response=True,
            type=DolbyAtmosAudioConfiguration,
            **kwargs
        )
