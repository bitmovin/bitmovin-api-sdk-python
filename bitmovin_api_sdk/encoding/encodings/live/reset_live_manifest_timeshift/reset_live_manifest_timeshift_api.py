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
        :param reset_live_manifest_time_shift: Removes older segments from live manifests. This resets or reduces the time-shift (DVR) window. The &#x60;residualPeriod&#x60; value determines how many seconds will remain in the time-shift window. The original time-shift window does not change. Newer segments will be added and not removed from the  manifest until the original time-shift duration is reached again.  Currently, only HLS live manifests are supported. 
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
