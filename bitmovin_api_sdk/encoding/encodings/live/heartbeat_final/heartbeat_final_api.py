# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.live_encoding_heartbeat_url_response import LiveEncodingHeartbeatUrlResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class HeartbeatFinalApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(HeartbeatFinalApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> LiveEncodingHeartbeatUrlResponse
        """Get Final Live Encoding Heartbeat Download URL

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :return: Presigned download URL for the final heartbeat of the live encoding
        :rtype: LiveEncodingHeartbeatUrlResponse
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/live/heartbeat-final',
            path_params={'encoding_id': encoding_id},
            type=LiveEncodingHeartbeatUrlResponse,
            **kwargs
        )
