# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.codec_configuration import CodecConfiguration
from bitmovin_api_sdk.models.passthrough_audio_configuration import PassthroughAudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.passthrough.passthrough_audio_configuration_list_query_params import PassthroughAudioConfigurationListQueryParams


class PassthroughApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PassthroughApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, passthrough_audio_configuration, **kwargs):
        # type: (PassthroughAudioConfiguration, dict) -> PassthroughAudioConfiguration
        """Create Audio Passthrough Configuration

        :param passthrough_audio_configuration: The Audio Passthrough Configuration to be created
        :type passthrough_audio_configuration: PassthroughAudioConfiguration, required
        :return: Passthrough Audio Configuration
        :rtype: PassthroughAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/passthrough',
            passthrough_audio_configuration,
            type=PassthroughAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Audio Passthrough Codec Configuration

        :param configuration_id: Id of the audio configuration
        :type configuration_id: string_types, required
        :return: Id of the audio configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/passthrough/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> PassthroughAudioConfiguration
        """Audio Passthrough Configuration Details

        :param configuration_id: Id of the audio configuration
        :type configuration_id: string_types, required
        :return: Passthrough Audio Configuration
        :rtype: PassthroughAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/passthrough/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=PassthroughAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (PassthroughAudioConfigurationListQueryParams, dict) -> PassthroughAudioConfiguration
        """List Audio Passthrough Configurations

        :param query_params: Query parameters
        :type query_params: PassthroughAudioConfigurationListQueryParams
        :return: List of Audio Passthrough configurations
        :rtype: PassthroughAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/passthrough',
            query_params=query_params,
            pagination_response=True,
            type=PassthroughAudioConfiguration,
            **kwargs
        )
