# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.opus_audio_configuration import OpusAudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.opus.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.opus.opus_audio_configuration_list_query_params import OpusAudioConfigurationListQueryParams


class OpusApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(OpusApi, self).__init__(
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

    def create(self, opus_audio_configuration, **kwargs):
        # type: (OpusAudioConfiguration, dict) -> OpusAudioConfiguration
        """Create Opus Codec Configuration

        :param opus_audio_configuration: The Opus Codec Configuration to be created
        :type opus_audio_configuration: OpusAudioConfiguration, required
        :return: Opus Audio Configuration
        :rtype: OpusAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/opus',
            opus_audio_configuration,
            type=OpusAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Opus Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/opus/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> OpusAudioConfiguration
        """Opus Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Opus Audio Configuration
        :rtype: OpusAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/opus/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=OpusAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (OpusAudioConfigurationListQueryParams, dict) -> OpusAudioConfiguration
        """List Opus Configurations

        :param query_params: Query parameters
        :type query_params: OpusAudioConfigurationListQueryParams
        :return: List of Opus codec configurations
        :rtype: OpusAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/opus',
            query_params=query_params,
            pagination_response=True,
            type=OpusAudioConfiguration,
            **kwargs
        )
