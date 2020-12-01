# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.mp3_audio_configuration import Mp3AudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.mp3.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.mp3.mp3_audio_configuration_list_query_params import Mp3AudioConfigurationListQueryParams


class Mp3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Mp3Api, self).__init__(
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

    def create(self, mp3_audio_configuration, **kwargs):
        # type: (Mp3AudioConfiguration, dict) -> Mp3AudioConfiguration
        """Create MP3 Codec Configuration

        :param mp3_audio_configuration: The MP3 Codec Configuration to be created
        :type mp3_audio_configuration: Mp3AudioConfiguration, required
        :return: MP3 Audio Configuration
        :rtype: Mp3AudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/mp3',
            mp3_audio_configuration,
            type=Mp3AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete MP3 Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/mp3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> Mp3AudioConfiguration
        """MP3 Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: MP3 Audio Configuration
        :rtype: Mp3AudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/mp3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Mp3AudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (Mp3AudioConfigurationListQueryParams, dict) -> Mp3AudioConfiguration
        """List MP3 Configurations

        :param query_params: Query parameters
        :type query_params: Mp3AudioConfigurationListQueryParams
        :return: List of MP3 codec configurations
        :rtype: Mp3AudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/mp3',
            query_params=query_params,
            pagination_response=True,
            type=Mp3AudioConfiguration,
            **kwargs
        )
