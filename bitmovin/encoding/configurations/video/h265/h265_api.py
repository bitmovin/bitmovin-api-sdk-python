# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.h265_video_configuration import H265VideoConfiguration
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.configurations.video.h265.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.configurations.video.h265.h265_video_configuration_list_query_params import H265VideoConfigurationListQueryParams


class H265Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(H265Api, self).__init__(
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

    def create(self, h265_video_configuration, **kwargs):
        """Create H265/HEVC Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/video/h265',
            h265_video_configuration,
            type=H265VideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete H265/HEVC Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/video/h265/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """H265/HEVC Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/video/h265/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=H265VideoConfiguration,
            **kwargs
        )

    def list(self, query_params: H265VideoConfigurationListQueryParams = None, **kwargs):
        """List H265/HEVC Codec Configurations"""

        return self.api_client.get(
            '/encoding/configurations/video/h265',
            query_params=query_params,
            pagination_response=True,
            type=H265VideoConfiguration,
            **kwargs
        )
