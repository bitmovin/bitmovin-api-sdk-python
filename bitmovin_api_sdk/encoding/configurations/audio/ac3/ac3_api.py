# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.ac3_audio_configuration import Ac3AudioConfiguration
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.ac3.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.ac3.ac3_audio_configuration_list_query_params import Ac3AudioConfigurationListQueryParams


class Ac3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Ac3Api, self).__init__(
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

    def create(self, ac3_audio_configuration, **kwargs):
        # type: (Ac3AudioConfiguration, dict) -> Ac3AudioConfiguration
        """Create AC3 Codec Configuration

        :param ac3_audio_configuration: The AC3 Codec Configuration to be created
        :type ac3_audio_configuration: Ac3AudioConfiguration, required
        :return: AC3 Audio Configuration
        :rtype: Ac3AudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/ac3',
            ac3_audio_configuration,
            type=Ac3AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete AC3 Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/ac3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> Ac3AudioConfiguration
        """AC3 Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: AC3 Audio Configuration
        :rtype: Ac3AudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/ac3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Ac3AudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (Ac3AudioConfigurationListQueryParams, dict) -> Ac3AudioConfiguration
        """List AC3 Configurations

        :param query_params: Query parameters
        :type query_params: Ac3AudioConfigurationListQueryParams
        :return: List of AC3 codec configurations
        :rtype: Ac3AudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/ac3',
            query_params=query_params,
            pagination_response=True,
            type=Ac3AudioConfiguration,
            **kwargs
        )
