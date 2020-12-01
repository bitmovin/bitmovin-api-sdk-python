# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.mjpeg_video_configuration import MjpegVideoConfiguration
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.configurations.video.mjpeg.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.configurations.video.mjpeg.mjpeg_video_configuration_list_query_params import MjpegVideoConfigurationListQueryParams


class MjpegApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (MjpegVideoConfiguration, dict) -> MjpegVideoConfiguration
        """Create MJPEG Codec Configuration

        :param mjpeg_video_configuration: The MJPEG Codec Configuration to be created
        :type mjpeg_video_configuration: MjpegVideoConfiguration, required
        :return: MJPEG Video Configuration
        :rtype: MjpegVideoConfiguration
        """

        return self.api_client.post(
            '/encoding/configurations/video/mjpeg',
            mjpeg_video_configuration,
            type=MjpegVideoConfiguration,
            **kwargs
        )

    def delete(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete MJPEG Codec Configuration

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: Id of the codec configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/configurations/video/mjpeg/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, configuration_id, **kwargs):
        # type: (string_types, dict) -> MjpegVideoConfiguration
        """MJPEG Codec Configuration Details

        :param configuration_id: Id of the codec configuration
        :type configuration_id: string_types, required
        :return: MJPEG Audio Configuration
        :rtype: MjpegVideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/mjpeg/{configuration_id}',
            path_params={'configuration_id': configuration_id},
            type=MjpegVideoConfiguration,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (MjpegVideoConfigurationListQueryParams, dict) -> MjpegVideoConfiguration
        """List MJPEG Configurations

        :param query_params: Query parameters
        :type query_params: MjpegVideoConfigurationListQueryParams
        :return: List of MJPEG codec configurations
        :rtype: MjpegVideoConfiguration
        """

        return self.api_client.get(
            '/encoding/configurations/video/mjpeg',
            query_params=query_params,
            pagination_response=True,
            type=MjpegVideoConfiguration,
            **kwargs
        )
