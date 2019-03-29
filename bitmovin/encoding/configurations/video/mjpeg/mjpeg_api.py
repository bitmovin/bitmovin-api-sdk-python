# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.mjpeg_video_configuration import MjpegVideoConfiguration
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.configurations.video.mjpeg.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.configurations.video.mjpeg.mjpeg_video_configuration_list_query_params import MjpegVideoConfigurationListQueryParams


class MjpegApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(MjpegApi, self).__init__(
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

    def create(self, mjpeg_video_configuration, **kwargs):
        """Create MJPEG Codec Configuration"""

        return self.api_client.post(
            '/encoding/configurations/video/mjpeg',
            mjpeg_video_configuration,
            type=MjpegVideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        """Delete MJPEG Codec Configuration"""

        return self.api_client.delete(
            '/encoding/configurations/video/mjpeg/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        """MJPEG Codec Configuration Details"""

        return self.api_client.get(
            '/encoding/configurations/video/mjpeg/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=MjpegVideoConfiguration,
            **kwargs
        )

    def list(self, query_params: MjpegVideoConfigurationListQueryParams = None, **kwargs):
        """List MJPEG Configurations"""

        return self.api_client.get(
            '/encoding/configurations/video/mjpeg',
            query_params=query_params,
            pagination_response=True,
            type=MjpegVideoConfiguration,
            **kwargs
        )
