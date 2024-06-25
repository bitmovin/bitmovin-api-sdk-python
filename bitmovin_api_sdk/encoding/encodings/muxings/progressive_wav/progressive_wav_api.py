# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.progressive_wav_muxing import ProgressiveWavMuxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_wav.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_wav.information.information_api import InformationApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_wav.progressive_wav_muxing_list_query_params import ProgressiveWavMuxingListQueryParams


class ProgressiveWavApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ProgressiveWavApi, self).__init__(
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

        self.information = InformationApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, progressive_wav_muxing, **kwargs):
        # type: (string_types, ProgressiveWavMuxing, dict) -> ProgressiveWavMuxing
        """Add Progressive Wav muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param progressive_wav_muxing: The Progressive WAV muxing to be created
        :type progressive_wav_muxing: ProgressiveWavMuxing, required
        :return: Progressive WAV muxing
        :rtype: ProgressiveWavMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/progressive-wav',
            progressive_wav_muxing,
            path_params={'encoding_id': encoding_id},
            type=ProgressiveWavMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Progressive WAV muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Progressive WAV muxing
        :type muxing_id: string_types, required
        :return: Id of the Progressive WAV muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/progressive-wav/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> ProgressiveWavMuxing
        """Progressive WAV muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Progressive WAV muxing
        :type muxing_id: string_types, required
        :return: Progressive WAV muxing details
        :rtype: ProgressiveWavMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-wav/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=ProgressiveWavMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, ProgressiveWavMuxingListQueryParams, dict) -> ProgressiveWavMuxing
        """List Progressive WAV muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: ProgressiveWavMuxingListQueryParams
        :return: List of Progressive WAV muxings
        :rtype: ProgressiveWavMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/progressive-wav',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=ProgressiveWavMuxing,
            **kwargs
        )
