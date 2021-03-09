# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.packed_audio_muxing import PackedAudioMuxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.muxings.packed_audio.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.encodings.muxings.packed_audio.information.information_api import InformationApi
from bitmovin_api_sdk.encoding.encodings.muxings.packed_audio.drm.drm_api import DrmApi
from bitmovin_api_sdk.encoding.encodings.muxings.packed_audio.packed_audio_muxing_list_query_params import PackedAudioMuxingListQueryParams


class PackedAudioApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PackedAudioApi, self).__init__(
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

        self.drm = DrmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, packed_audio_muxing, **kwargs):
        # type: (string_types, PackedAudioMuxing, dict) -> PackedAudioMuxing
        """Add Packed Audio muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param packed_audio_muxing: The Packed Audio muxing to be created
        :type packed_audio_muxing: PackedAudioMuxing, required
        :return: Packed Audio muxing
        :rtype: PackedAudioMuxing
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/packed-audio',
            packed_audio_muxing,
            path_params={'encoding_id': encoding_id},
            type=PackedAudioMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Delete Packed Audio muxing

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Packed Audio muxing
        :type muxing_id: string_types, required
        :return: Id of the Packed Audio muxing
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/packed-audio/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> PackedAudioMuxing
        """Packed Audio muxing details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the Packed Audio muxing
        :type muxing_id: string_types, required
        :return: Packed Audio muxing
        :rtype: PackedAudioMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/packed-audio/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=PackedAudioMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, PackedAudioMuxingListQueryParams, dict) -> PackedAudioMuxing
        """List Packed Audio muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: PackedAudioMuxingListQueryParams
        :return: List of Packed Audio muxings
        :rtype: PackedAudioMuxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/packed-audio',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=PackedAudioMuxing,
            **kwargs
        )
