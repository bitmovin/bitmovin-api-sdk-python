# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.he_aac_v2_audio_configuration import HeAacV2AudioConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.audio.he_aac_v2.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.audio.he_aac_v2.he_aac_v2_audio_configuration_list_query_params import HeAacV2AudioConfigurationListQueryParams


class HeAacV2Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(HeAacV2Api, self).__init__(
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

    def create(self, he_aac_v2_audio_configuration, **kwargs):
        # type: (HeAacV2AudioConfiguration, dict) -> HeAacV2AudioConfiguration
        """Create HE-AAC v2 Codec Configuration

        :param he_aac_v2_audio_configuration: The HE-AAC v2 Codec Configuration to be created
        :type he_aac_v2_audio_configuration: HeAacV2AudioConfiguration, required
        :return: HE-AAC v2 Audio Configuration
        :rtype: HeAacV2AudioConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/audio/he-aac-v2',
            he_aac_v2_audio_configuration,
            type=HeAacV2AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete HE-AAC v2 Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/audio/he-aac-v2/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> HeAacV2AudioConfiguration
        """HE-AAC v2 Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: HE-AAC v2 Audio Configuration
        :rtype: HeAacV2AudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/he-aac-v2/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=HeAacV2AudioConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (HeAacV2AudioConfigurationListQueryParams, dict) -> HeAacV2AudioConfiguration
        """List HE-AAC v2 Configurations

        :param query_params: Query parameters
        :type query_params: HeAacV2AudioConfigurationListQueryParams
        :return: List of HE-AAC v2 codec configuration ids
        :rtype: HeAacV2AudioConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/audio/he-aac-v2',
            query_params=query_params,
            pagination_response=True,
            type=HeAacV2AudioConfiguration,
            **kwargs
        )
