# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.muxing import Muxing
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.stream_mode import StreamMode
from bitmovin_api_sdk.encoding.encodings.muxings.fmp4.fmp4_api import Fmp4Api
from bitmovin_api_sdk.encoding.encodings.muxings.chunked_text.chunked_text_api import ChunkedTextApi
from bitmovin_api_sdk.encoding.encodings.muxings.cmaf.cmaf_api import CmafApi
from bitmovin_api_sdk.encoding.encodings.muxings.segmented_raw.segmented_raw_api import SegmentedRawApi
from bitmovin_api_sdk.encoding.encodings.muxings.packed_audio.packed_audio_api import PackedAudioApi
from bitmovin_api_sdk.encoding.encodings.muxings.text.text_api import TextApi
from bitmovin_api_sdk.encoding.encodings.muxings.ts.ts_api import TsApi
from bitmovin_api_sdk.encoding.encodings.muxings.webm.webm_api import WebmApi
from bitmovin_api_sdk.encoding.encodings.muxings.mp3.mp3_api import Mp3Api
from bitmovin_api_sdk.encoding.encodings.muxings.mp4.mp4_api import Mp4Api
from bitmovin_api_sdk.encoding.encodings.muxings.mxf.mxf_api import MxfApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_ts.progressive_ts_api import ProgressiveTsApi
from bitmovin_api_sdk.encoding.encodings.muxings.broadcast_ts.broadcast_ts_api import BroadcastTsApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_webm.progressive_webm_api import ProgressiveWebmApi
from bitmovin_api_sdk.encoding.encodings.muxings.progressive_mov.progressive_mov_api import ProgressiveMovApi
from bitmovin_api_sdk.encoding.encodings.muxings.muxing_list_query_params import MuxingListQueryParams


class MuxingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(MuxingsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.fmp4 = Fmp4Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.chunked_text = ChunkedTextApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.cmaf = CmafApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.segmented_raw = SegmentedRawApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.packed_audio = PackedAudioApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.text = TextApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.ts = TsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.webm = WebmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mp3 = Mp3Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mp4 = Mp4Api(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.mxf = MxfApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.progressive_ts = ProgressiveTsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.broadcast_ts = BroadcastTsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.progressive_webm = ProgressiveWebmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.progressive_mov = ProgressiveMovApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        # type: (string_types, string_types, dict) -> Muxing
        """Muxing Details

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param muxing_id: Id of the muxing.
        :type muxing_id: string_types, required
        :return: Muxing details
        :rtype: Muxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=Muxing,
            **kwargs
        )

    def list(self, encoding_id, query_params=None, **kwargs):
        # type: (string_types, MuxingListQueryParams, dict) -> Muxing
        """List All Muxings

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param query_params: Query parameters
        :type query_params: MuxingListQueryParams
        :return: List of muxings
        :rtype: Muxing
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Muxing,
            **kwargs
        )
