# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.eac3_audio_configuration import Eac3AudioConfiguration
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.configurations.audio.eac3.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.configurations.audio.eac3.eac3_audio_configuration_list_query_params import Eac3AudioConfigurationListQueryParams


class Eac3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
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
        """Create E-AC3 Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/audio/eac3',
            eac3_audio_configuration,
            type=Eac3AudioConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete E-AC3 Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/audio/eac3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """E-AC3 Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/audio/eac3/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Eac3AudioConfiguration,
            **kwargs
        )

    def list(self, query_params: Eac3AudioConfigurationListQueryParams = None, **kwargs):
        """List E-AC3 Configurations"""

        return self.api_client.get(
            '/encoding/configurations/audio/eac3',
            query_params=query_params,
            pagination_response=True,
            type=Eac3AudioConfiguration,
            **kwargs
        )
