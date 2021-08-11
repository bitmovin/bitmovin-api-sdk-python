# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dts_x_audio_configuration import DtsXAudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.dtsx.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.dtsx.dts_x_audio_configuration_list_query_params import DtsXAudioConfigurationListQueryParams


class DtsxApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DtsxApi, self).__init__(
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

    def create(self, dts_x_audio_configuration, **kwargs):
        # type: (DtsXAudioConfiguration, dict) -> DtsXAudioConfiguration
        """Create DTS:X Codec Configuration

        :param dts_x_audio_configuration: The DTS:X Codec Configuration to be created
        :type dts_x_audio_configuration: DtsXAudioConfiguration, required
        :return: DTS:X Audio Configuration
        :rtype: DtsXAudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/dtsx',
            dts_x_audio_configuration,
            type=DtsXAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete DTS:X Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/dtsx/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> DtsXAudioConfiguration
        """DTS:X Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: DTS:X Audio Configuration
        :rtype: DtsXAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dtsx/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=DtsXAudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DtsXAudioConfigurationListQueryParams, dict) -> DtsXAudioConfiguration
        """List DTS:X Codec Configurations

        :param query_params: Query parameters
        :type query_params: DtsXAudioConfigurationListQueryParams
        :return: List of DTS:X codec configurations
        :rtype: DtsXAudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/dtsx',
            query_params=query_params,
            pagination_response=True,
            type=DtsXAudioConfiguration,
            **kwargs
        )
