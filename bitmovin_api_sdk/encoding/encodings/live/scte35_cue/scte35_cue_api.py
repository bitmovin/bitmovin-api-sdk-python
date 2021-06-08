# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.scte35_cue import Scte35Cue


class Scte35CueApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(Scte35CueApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, scte35_cue, **kwargs):
        # type: (string_types, Scte35Cue, dict) -> Scte35Cue
        """Insert cue duration

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param scte35_cue: Cue duration and manifest ids.
        :type scte35_cue: Scte35Cue, required
        :return: SCTE-35 Cue
        :rtype: Scte35Cue
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/live/scte-35-cue',
            scte35_cue,
            path_params={'encoding_id': encoding_id},
            type=Scte35Cue,
            **kwargs
        )
