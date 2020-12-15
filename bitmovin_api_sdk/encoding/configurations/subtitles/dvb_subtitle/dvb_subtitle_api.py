# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.dvb_subtitle_configuration import DvbSubtitleConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.subtitle_configuration import SubtitleConfiguration
from bitmovin_api_sdk.encoding.configurations.subtitles.dvb_subtitle.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.subtitles.dvb_subtitle.dvb_subtitle_configuration_list_query_params import DvbSubtitleConfigurationListQueryParams


class DvbSubtitleApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DvbSubtitleApi, self).__init__(
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

    def create(self, dvb_subtitle_configuration, **kwargs):
        # type: (DvbSubtitleConfiguration, dict) -> DvbSubtitleConfiguration
        """Create DVB-SUB subtitle configuration

        :param dvb_subtitle_configuration: The DVB-SUB subtitle configuration to be created
        :type dvb_subtitle_configuration: DvbSubtitleConfiguration, required
        :return: The created DVB-SUB subtitle configuration
        :rtype: DvbSubtitleConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/subtitles/dvb-subtitle',
            dvb_subtitle_configuration,
            type=DvbSubtitleConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete DVB-SUB subtitle configuration

        :param configuration_id: Id of the subtitle configuration
        :type configuration_id: string_types, required
        :return: Id of the deleted configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/subtitles/dvb-subtitle/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> DvbSubtitleConfiguration
        """DVB-SUB subtitle configuration details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: DVB-SUB subtitle configuration
        :rtype: DvbSubtitleConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/subtitles/dvb-subtitle/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=DvbSubtitleConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DvbSubtitleConfigurationListQueryParams, dict) -> DvbSubtitleConfiguration
        """List DVB-SUB subtitle configurations

        :param query_params: Query parameters
        :type query_params: DvbSubtitleConfigurationListQueryParams
        :return: List of DVB-SUB subtitle configurations
        :rtype: DvbSubtitleConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/subtitles/dvb-subtitle',
            query_params=query_params,
            pagination_response=True,
            type=DvbSubtitleConfiguration,
            **kwargs
        )
