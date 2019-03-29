# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.av1_video_configuration import Av1VideoConfiguration
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.configurations.video.av1.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.configurations.video.av1.av1_video_configuration_list_query_params import Av1VideoConfigurationListQueryParams


class Av1Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Av1Api, self).__init__(
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

    def create(self, av1_video_configuration, **kwargs):
        """Create AV1 Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/video/av1',
            av1_video_configuration,
            type=Av1VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete AV1 Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/video/av1/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """AV1 Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/video/av1/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Av1VideoConfiguration,
            **kwargs
        )

    def list(self, query_params: Av1VideoConfigurationListQueryParams = None, **kwargs):
        """List AV1 Codec Configurations"""

        return self.api_client.get(
            '/encoding/configurations/video/av1',
            query_params=query_params,
            pagination_response=True,
            type=Av1VideoConfiguration,
            **kwargs
        )
