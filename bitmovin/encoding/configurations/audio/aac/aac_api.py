# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.aac_audio_configuration import AacAudioConfiguration
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.configurations.audio.aac.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.configurations.audio.aac.aac_audio_configuration_list_query_params import AacAudioConfigurationListQueryParams


class AacApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AacApi, self).__init__(
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

    def create(self, aac_audio_configuration, **kwargs):
        """Create AAC Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/audio/aac',
            aac_audio_configuration,
            type=AacAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete AAC Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/audio/aac/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """AAC Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/audio/aac/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=AacAudioConfiguration,
            **kwargs
        )

    def list(self, query_params: AacAudioConfigurationListQueryParams = None, **kwargs):
        """List AAC Configurations"""

        return self.api_client.get(
            '/encoding/configurations/audio/aac',
            query_params=query_params,
            pagination_response=True,
            type=AacAudioConfiguration,
            **kwargs
        )
