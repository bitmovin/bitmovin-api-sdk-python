# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.streams_config_response import StreamsConfigResponse
from bitmovin_api_sdk.models.streams_config_update_request import StreamsConfigUpdateRequest


class ConfigsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ConfigsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def patch_stream_config(self, config_id, streams_config_update_request, **kwargs):
        # type: (string_types, StreamsConfigUpdateRequest, dict) -> StreamsConfigResponse
        """Update stream config by id

        :param config_id: Id of the stream config.
        :type config_id: string_types, required
        :param streams_config_update_request: The updated stream config object.
        :type streams_config_update_request: StreamsConfigUpdateRequest, required
        :return:
        :rtype: StreamsConfigResponse
        """

        return self.api_client.patch(
            '/streams/configs/{config_id}',
            streams_config_update_request,
            path_params={'config_id': config_id},
            type=StreamsConfigResponse,
            **kwargs
        )
