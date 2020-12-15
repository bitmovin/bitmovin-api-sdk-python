# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.mp2_audio_configuration import Mp2AudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.mp2.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.mp2.mp2_audio_configuration_list_query_params import Mp2AudioConfigurationListQueryParams


class Mp2Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Mp2Api, self).__init__(
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

    def create(self, mp2_audio_configuration, **kwargs):
        # type: (Mp2AudioConfiguration, dict) -> Mp2AudioConfiguration
        """Create MP2 Codec Configuration

        :param mp2_audio_configuration: The MP2 Codec Configuration to be created
        :type mp2_audio_configuration: Mp2AudioConfiguration, required
        :return: MP2 Audio Configuration
        :rtype: Mp2AudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/mp2',
            mp2_audio_configuration,
            type=Mp2AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete MP2 Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/mp2/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> Mp2AudioConfiguration
        """MP2 Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: MP2 Audio Configuration
        :rtype: Mp2AudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/mp2/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Mp2AudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (Mp2AudioConfigurationListQueryParams, dict) -> Mp2AudioConfiguration
        """List MP2 Configurations

        :param query_params: Query parameters
        :type query_params: Mp2AudioConfigurationListQueryParams
        :return: List of MP2 codec configurations
        :rtype: Mp2AudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/mp2',
            query_params=query_params,
            pagination_response=True,
            type=Mp2AudioConfiguration,
            **kwargs
        )
