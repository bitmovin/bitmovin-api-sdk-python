# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.imsc_configuration import ImscConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.subtitles.imsc.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.subtitles.imsc.imsc_configuration_list_query_params import ImscConfigurationListQueryParams


class ImscApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ImscApi, self).__init__(
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

    def create(self, imsc_configuration, **kwargs):
        # type: (ImscConfiguration, dict) -> ImscConfiguration
        """Create IMSC subtitle configuration

        :param imsc_configuration: The IMSC subtitle configuration to be created
        :type imsc_configuration: ImscConfiguration, required
        :return: The created IMSC subtitle configuration
        :rtype: ImscConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/subtitles/imsc',
            imsc_configuration,
            type=ImscConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete IMSC subtitle configuration

        :param configuration_id: Id of the subtitle configuration
        :type configuration_id: string_types, required
        :return: Id of the deleted configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/subtitles/imsc/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> ImscConfiguration
        """IMSC subtitle configuration details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: IMSC subtitle configuration
        :rtype: ImscConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/subtitles/imsc/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=ImscConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (ImscConfigurationListQueryParams, dict) -> ImscConfiguration
        """List IMSC subtitle configurations

        :param query_params: Query parameters
        :type query_params: ImscConfigurationListQueryParams
        :return: List of IMSC subtitle configurations
        :rtype: ImscConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/subtitles/imsc',
            query_params=query_params,
            pagination_response=True,
            type=ImscConfiguration,
            **kwargs
        )
