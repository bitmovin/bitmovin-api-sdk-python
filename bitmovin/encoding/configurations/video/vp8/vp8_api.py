# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.vp8_video_configuration import Vp8VideoConfiguration
from bitmovin.encoding.configurations.video.vp8.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.configurations.video.vp8.vp8_video_configuration_list_query_params import Vp8VideoConfigurationListQueryParams


class Vp8Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(Vp8Api, self).__init__(
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

    def create(self, vp8_video_configuration, **kwargs):
        """Create VP8 Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/video/vp8',
            vp8_video_configuration,
            type=Vp8VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete VP8 Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/video/vp8/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """VP8 Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/video/vp8/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=Vp8VideoConfiguration,
            **kwargs
        )

    def list(self, query_params: Vp8VideoConfigurationListQueryParams = None, **kwargs):
        """get_encoding_configurations_video_vp8"""

        return self.api_client.get(
            '/encoding/configurations/video/vp8',
            query_params=query_params,
            pagination_response=True,
            type=Vp8VideoConfiguration,
            **kwargs
        )
