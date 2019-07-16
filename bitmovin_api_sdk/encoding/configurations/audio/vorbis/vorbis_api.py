# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.vorbis_audio_configuration import VorbisAudioConfiguration
from bitmovin_api_sdk.encoding.configurations.audio.vorbis.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.vorbis.vorbis_audio_configuration_list_query_params import VorbisAudioConfigurationListQueryParams


class VorbisApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(VorbisApi, self).__init__(
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

    def create(self, vorbis_audio_configuration, **kwargs):
        # type: (VorbisAudioConfiguration, dict) -> VorbisAudioConfiguration
        """Create Vorbis Codec Configuration

        :param vorbis_audio_configuration: The Vorbis Codec Configuration to be created
        :type vorbis_audio_configuration: VorbisAudioConfiguration, required
        :return: Vorbis Audio Configuration
        :rtype: VorbisAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/vorbis',
            vorbis_audio_configuration,
            type=VorbisAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Vorbis Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/vorbis/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> VorbisAudioConfiguration
        """Vorbis Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Vorbis Audio Configuration
        :rtype: VorbisAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/vorbis/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=VorbisAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (VorbisAudioConfigurationListQueryParams, dict) -> VorbisAudioConfiguration
        """List Vorbis Configurations

        :param query_params: Query parameters
        :type query_params: VorbisAudioConfigurationListQueryParams
        :return: List of Vorbis codec configuration ids
        :rtype: VorbisAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/vorbis',
            query_params=query_params,
            pagination_response=True,
            type=VorbisAudioConfiguration,
            **kwargs
        )
