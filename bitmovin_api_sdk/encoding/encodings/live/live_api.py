# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.live_encoding import LiveEncoding
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.start_live_encoding_request import StartLiveEncodingRequest
from bitmovin_api_sdk.encoding.encodings.live.insertable_content.insertable_content_api import InsertableContentApi
from bitmovin_api_sdk.encoding.encodings.live.scte35_cue.scte35_cue_api import Scte35CueApi


class LiveApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LiveApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.insertable_content = InsertableContentApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.scte35_cue = Scte35CueApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> LiveEncoding
        """Live Encoding Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :return: Encoding
        :rtype: LiveEncoding
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/live',
            path_params={'encoding_id': encoding_id},
            type=LiveEncoding,
            **kwargs
        )

    def get_start_request(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> StartLiveEncodingRequest
        """Live Encoding Start Details

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :return: Service specific result
        :rtype: StartLiveEncodingRequest
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/live/start',
            path_params={'encoding_id': encoding_id},
            type=StartLiveEncodingRequest,
            **kwargs
        )

    def restart(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Re-Start Live Encoding

        :param encoding_id: Id of the encoding.  **Important:** Only live encodings with the status &#x60;RUNNING&#x60;, &#x60;FINISHED&#x60;, &#x60;CANCELED&#x60; or &#x60;ERROR&#x60; can be restarted. 
        :type encoding_id: string_types, required
        :return: Id of the encoding
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/restart',
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def start(self, encoding_id, start_live_encoding_request, **kwargs):
        # type: (string_types, StartLiveEncodingRequest, dict) -> BitmovinResponse
        """Start Live Encoding

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :param start_live_encoding_request: Live Encoding startup options
        :type start_live_encoding_request: StartLiveEncodingRequest, required
        :return: Id of the encoding
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/start',
            start_live_encoding_request,
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )

    def stop(self, encoding_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Stop Live Encoding

        :param encoding_id: Id of the encoding
        :type encoding_id: string_types, required
        :return: Id of the encoding
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/stop',
            path_params={'encoding_id': encoding_id},
            type=BitmovinResponse,
            **kwargs
        )
