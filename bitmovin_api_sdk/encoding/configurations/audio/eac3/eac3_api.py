# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.eac3_audio_configuration import Eac3AudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.eac3.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.eac3.eac3_audio_configuration_list_query_params import Eac3AudioConfigurationListQueryParams


class Eac3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Eac3Api, self).__init__(
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

    def create(self, eac3_audio_configuration, **kwargs):
        # type: (Eac3AudioConfiguration, dict) -> Eac3AudioConfiguration
        """Create E-AC3 Codec Configuration

        :param eac3_audio_configuration: The E-AC3 Codec Configuration to be created
        :type eac3_audio_configuration: Eac3AudioConfiguration, required
        :return: E-AC3 Audio Configuration
        :rtype: Eac3AudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/eac3',
            eac3_audio_configuration,
            type=Eac3AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete E-AC3 Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/eac3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> Eac3AudioConfiguration
        """E-AC3 Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: E-AC3 Audio Configuration
        :rtype: Eac3AudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/eac3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Eac3AudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (Eac3AudioConfigurationListQueryParams, dict) -> Eac3AudioConfiguration
        """List E-AC3 Configurations

        :param query_params: Query parameters
        :type query_params: Eac3AudioConfigurationListQueryParams
        :return: List of E-AC3 codec configurations
        :rtype: Eac3AudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/eac3',
            query_params=query_params,
            pagination_response=True,
            type=Eac3AudioConfiguration,
            **kwargs
        )
