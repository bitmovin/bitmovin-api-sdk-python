# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.muxing import Muxing
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.stream_mode import StreamMode
from bitmovin.encoding.encodings.muxings.fmp4.fmp4_api import Fmp4Api
from bitmovin.encoding.encodings.muxings.cmaf.cmaf_api import CmafApi
from bitmovin.encoding.encodings.muxings.segmentedRaw.segmented_raw_api import SegmentedRawApi
from bitmovin.encoding.encodings.muxings.ts.ts_api import TsApi
from bitmovin.encoding.encodings.muxings.webm.webm_api import WebmApi
from bitmovin.encoding.encodings.muxings.mp3.mp3_api import Mp3Api
from bitmovin.encoding.encodings.muxings.mp4.mp4_api import Mp4Api
from bitmovin.encoding.encodings.muxings.progressiveTs.progressive_ts_api import ProgressiveTsApi
from bitmovin.encoding.encodings.muxings.broadcastTs.broadcast_ts_api import BroadcastTsApi
from bitmovin.encoding.encodings.muxings.progressiveWebm.progressive_webm_api import ProgressiveWebmApi
from bitmovin.encoding.encodings.muxings.progressiveMov.progressive_mov_api import ProgressiveMovApi
from bitmovin.encoding.encodings.muxings.muxing_list_query_params import MuxingListQueryParams


class MuxingsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
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

        self.cmaf = CmafApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.segmentedRaw = SegmentedRawApi(
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

        self.progressiveTs = ProgressiveTsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.broadcastTs = BroadcastTsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.progressiveWebm = ProgressiveWebmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.progressiveMov = ProgressiveMovApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def list(self, encoding_id, query_params: MuxingListQueryParams = None, **kwargs):
        """List All Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=Muxing,
            **kwargs
        )
