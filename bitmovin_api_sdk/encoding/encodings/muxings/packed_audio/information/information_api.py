# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.packed_audio_muxing_information import PackedAudioMuxingInformation
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class InformationApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(InformationApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> PackedAudioMuxingInformation
        """Packed Audio muxing Information

        :param encoding_id: ID of the Encoding.
        :type encoding_id: string_types, required
        :param muxing_id: ID of the Packed Audio muxing
        :type muxing_id: string_types, required
        :return: Packed Audio muxing Information
        :rtype: PackedAudioMuxingInformation
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/packed-audio/{muxing_id}/information',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=PackedAudioMuxingInformation,
            **kwargs
        )
