# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.opus_audio_configuration import OpusAudioConfiguration
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.configurations.audio.opus.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.configurations.audio.opus.opus_audio_configuration_list_query_params import OpusAudioConfigurationListQueryParams


class OpusApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(OpusApi, self).__init__(
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

    def create(self, opus_audio_configuration, **kwargs):
        """Create Opus Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/audio/opus',
            opus_audio_configuration,
            type=OpusAudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete Opus Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/audio/opus/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """Opus Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/audio/opus/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=OpusAudioConfiguration,
            **kwargs
        )

    def list(self, query_params: OpusAudioConfigurationListQueryParams = None, **kwargs):
        """List Opus Configurations"""

        return self.api_client.get(
            '/encoding/configurations/audio/opus',
            query_params=query_params,
            pagination_response=True,
            type=OpusAudioConfiguration,
            **kwargs
        )
