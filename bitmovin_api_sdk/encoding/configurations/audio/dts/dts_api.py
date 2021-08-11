# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dts_audio_configuration import DtsAudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.dts.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.dts.dts_audio_configuration_list_query_params import DtsAudioConfigurationListQueryParams


class DtsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DtsApi, self).__init__(
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

    def create(self, dts_audio_configuration, **kwargs):
        # type: (DtsAudioConfiguration, dict) -> DtsAudioConfiguration
        """Create DTS Codec Configuration

        :param dts_audio_configuration: The DTS Codec Configuration to be created
        :type dts_audio_configuration: DtsAudioConfiguration, required
        :return: DTS Audio Configuration
        :rtype: DtsAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/dts',
            dts_audio_configuration,
            type=DtsAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete DTS Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/dts/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> DtsAudioConfiguration
        """DTS Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: DTS Audio Configuration
        :rtype: DtsAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dts/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=DtsAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DtsAudioConfigurationListQueryParams, dict) -> DtsAudioConfiguration
        """List DTS Codec Configurations

        :param query_params: Query parameters
        :type query_params: DtsAudioConfigurationListQueryParams
        :return: List of DTS codec configurations
        :rtype: DtsAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dts',
            query_params=query_params,
            pagination_response=True,
            type=DtsAudioConfiguration,
            **kwargs
        )
