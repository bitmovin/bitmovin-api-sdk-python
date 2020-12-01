# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.codec_configuration import CodecConfiguration
from bitmovin_api_sdk.models.dts_passthrough_audio_configuration import DtsPassthroughAudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.dts_passthrough.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.dts_passthrough.dts_passthrough_audio_configuration_list_query_params import DtsPassthroughAudioConfigurationListQueryParams


class DtsPassthroughApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DtsPassthroughApi, self).__init__(
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

    def create(self, dts_passthrough_audio_configuration, **kwargs):
        # type: (DtsPassthroughAudioConfiguration, dict) -> DtsPassthroughAudioConfiguration
        """Create DTS Passthrough Configuration

        :param dts_passthrough_audio_configuration: The DTS Passthrough Codec Configuration to be created
        :type dts_passthrough_audio_configuration: DtsPassthroughAudioConfiguration, required
        :return: DTS Passthrough Audio Configuration
        :rtype: DtsPassthroughAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/dts-passthrough',
            dts_passthrough_audio_configuration,
            type=DtsPassthroughAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete DTS Passthrough Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/dts-passthrough/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> DtsPassthroughAudioConfiguration
        """DTS Passthrough Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: DTS Passthrough Audio Configuration
        :rtype: DtsPassthroughAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dts-passthrough/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=DtsPassthroughAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DtsPassthroughAudioConfigurationListQueryParams, dict) -> DtsPassthroughAudioConfiguration
        """List DTS Passthrough Configurations

        :param query_params: Query parameters
        :type query_params: DtsPassthroughAudioConfigurationListQueryParams
        :return: List of DTS Passthrough codec configurations
        :rtype: DtsPassthroughAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dts-passthrough',
            query_params=query_params,
            pagination_response=True,
            type=DtsPassthroughAudioConfiguration,
            **kwargs
        )
