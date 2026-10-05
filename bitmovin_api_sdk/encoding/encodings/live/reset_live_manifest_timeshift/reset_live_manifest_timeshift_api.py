# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.reset_live_manifest_time_shift import ResetLiveManifestTimeShift
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class ResetLiveManifestTimeshiftApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ResetLiveManifestTimeshiftApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, reset_live_manifest_time_shift, **kwargs):
        # type: (string_types, ResetLiveManifestTimeShift, dict) -> ResetLiveManifestTimeShift
        """Reset Live manifest time-shift

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param reset_live_manifest_time_shift: Removes older segments from live manifests, resetting or reducing the time-shift (DVR) window. You can set &#x60;residualPeriodInSeconds&#x60; to specify how many seconds of content remain in the manifest after the reset, or &#x60;offsetInSeconds&#x60; to remove all segments before a position measured from the start of the live event. Do not set both parameters. If neither parameter is set, only the most recent segment remains. For DASH manifests that use SegmentTemplate, the duration retained by &#x60;residualPeriodInSeconds&#x60; (or when neither parameter is set) also includes the configured &#x60;liveEdgeOffset&#x60;. The configured time-shift window does not change. After the reset, new segments are added without removing older ones until the configured window duration is reached again. This operation supports HLS live manifests and, with encoder version 2.235.0 or later, DASH live manifests. The live encoding must have the &#x60;RUNNING&#x60; status. The request is processed asynchronously. 
        :type reset_live_manifest_time_shift: ResetLiveManifestTimeShift, required
        :return: Reset Live manifest time-shift request
        :rtype: ResetLiveManifestTimeShift
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/reset-live-manifest-timeshift',
            reset_live_manifest_time_shift,
            path_params={'encoding_id': encoding_id},
            type=ResetLiveManifestTimeShift,
            **kwargs
        )
