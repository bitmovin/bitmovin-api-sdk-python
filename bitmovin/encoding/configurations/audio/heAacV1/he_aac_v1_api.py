# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.he_aac_v1_audio_configuration import HeAacV1AudioConfiguration
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.configurations.audio.heAacV1.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.configurations.audio.heAacV1.he_aac_v1_audio_configuration_list_query_params import HeAacV1AudioConfigurationListQueryParams


class HeAacV1Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(HeAacV1Api, self).__init__(
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

    def create(self, he_aac_v1_audio_configuration, **kwargs):
        """Create HE-AAC v1 Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/audio/he-aac-v1',
            he_aac_v1_audio_configuration,
            type=HeAacV1AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete HE-AAC v1 Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/audio/he-aac-v1/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """HE-AAC v1 Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/audio/he-aac-v1/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=HeAacV1AudioConfiguration,
            **kwargs
        )

    def list(self, query_params: HeAacV1AudioConfigurationListQueryParams = None, **kwargs):
        """List HE-AAC v1 Configurations"""

        return self.api_client.get(
            '/encoding/configurations/audio/he-aac-v1',
            query_params=query_params,
            pagination_response=True,
            type=HeAacV1AudioConfiguration,
            **kwargs
        )
