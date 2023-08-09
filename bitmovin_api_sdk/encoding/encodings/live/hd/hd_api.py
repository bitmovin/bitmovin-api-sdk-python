# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.start_live_channel_encoding_request import StartLiveChannelEncodingRequest
from bitmovin_api_sdk.models.start_live_encoding_request import StartLiveEncodingRequest


class HdApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(HdApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get_start_request(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> StartLiveChannelEncodingRequest
        """Live Encoding Start Details

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :return: Service specific result
        :rtype: StartLiveChannelEncodingRequest
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/live/hd/start',
            path_params={'encoding_id': encoding_id},
            type=StartLiveChannelEncodingRequest,
            **kwargs
        )

    def start(self, encoding_id, start_live_channel_encoding_request, **kwargs):
        # type: (string_types, StartLiveChannelEncodingRequest, dict) -> BitmovinResponse
        """Start HD Options Live Encoding

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param start_live_channel_encoding_request: Live Encoding startup options
        :type start_live_channel_encoding_request: StartLiveChannelEncodingRequest, required
        :return: Id of the encoding
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/hd/start',
            start_live_channel_encoding_request,
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )
