# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.live_auto_shutdown_configuration import LiveAutoShutdownConfiguration
from bitmovin_api_sdk.models.live_auto_shutdown_configuration_update_request import LiveAutoShutdownConfigurationUpdateRequest
from bitmovin_api_sdk.models.live_auto_shutdown_configuration_update_response import LiveAutoShutdownConfigurationUpdateResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class UpdateAutoshutdownConfigApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(UpdateAutoshutdownConfigApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, live_auto_shutdown_configuration_update_request, **kwargs):
        # type: (string_types, LiveAutoShutdownConfigurationUpdateRequest, dict) -> LiveAutoShutdownConfigurationUpdateResponse
        """Replace Live Auto Shutdown Configuration

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param live_auto_shutdown_configuration_update_request: Applies a new auto shutdown configuration to a Live Encoding that is already running, without interrupting the stream.  **The body is a full replacement, not a partial update.** Every field that is omitted or set to &#x60;null&#x60; disarms the corresponding timer, and an empty body &#x60;{}&#x60; disarms all timers. Always send the complete configuration you want the encoding to run with, including the values you want to keep.  **&#x60;streamTimeoutMinutes&#x60; is counted from this call, not from the start of the encoding.** The encoding is stopped that many minutes after the update is accepted, whereas in the start request the same field is counted from when the encoding started. An encoding started at 12:00 with &#x60;streamTimeoutMinutes&#x60; of 120 is scheduled to stop at 14:00; updating it at 13:30 with &#x60;streamTimeoutMinutes&#x60; of 150 moves the shutdown to 16:00, not to 14:30. &#x60;bytesReadTimeoutSeconds&#x60; is relative by nature, as it always counts from the last byte received, and &#x60;waitingForFirstConnectTimeoutMinutes&#x60; has no effect once the input is connected.  The organization&#39;s maximum live encoding runtime still bounds the total runtime of the encoding, measured from the start of the encoding. An update that would push the shutdown past that limit is rejected rather than extending the encoding beyond it.  **Do not leave the call to the last few seconds.** The update is rejected with &#x60;409&#x60; when any armed shutdown timer is within 10 seconds of firing, because at that point the shutdown sequence is effectively already in flight. 
        :type live_auto_shutdown_configuration_update_request: LiveAutoShutdownConfigurationUpdateRequest, required
        :return: The accepted Live Encoding auto shutdown configuration
        :rtype: LiveAutoShutdownConfigurationUpdateResponse
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/update-autoshutdown-config',
            live_auto_shutdown_configuration_update_request,
            path_params={'encoding_id': encoding_id},
            type=LiveAutoShutdownConfigurationUpdateResponse,
            **kwargs
        )
