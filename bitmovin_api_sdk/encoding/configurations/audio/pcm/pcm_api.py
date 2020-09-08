# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.pcm_audio_configuration import PcmAudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.pcm.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.pcm.pcm_audio_configuration_list_query_params import PcmAudioConfigurationListQueryParams


class PcmApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PcmApi, self).__init__(
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

    def create(self, pcm_audio_configuration, **kwargs):
        # type: (PcmAudioConfiguration, dict) -> PcmAudioConfiguration
        """Create PCM Codec Configuration

        :param pcm_audio_configuration: The PCM Codec Configuration to be created
        :type pcm_audio_configuration: PcmAudioConfiguration, required
        :return: PCM Audio Configuration
        :rtype: PcmAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/pcm',
            pcm_audio_configuration,
            type=PcmAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete PCM Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/pcm/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> PcmAudioConfiguration
        """PCM Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: PCM Audio Configuration
        :rtype: PcmAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/pcm/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=PcmAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (PcmAudioConfigurationListQueryParams, dict) -> PcmAudioConfiguration
        """List PCM Configurations

        :param query_params: Query parameters
        :type query_params: PcmAudioConfigurationListQueryParams
        :return: List of PCM codec configuration ids
        :rtype: PcmAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/pcm',
            query_params=query_params,
            pagination_response=True,
            type=PcmAudioConfiguration,
            **kwargs
        )
