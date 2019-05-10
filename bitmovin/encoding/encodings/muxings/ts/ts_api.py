# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.ts_muxing import TsMuxing
from bitmovin.encoding.encodings.muxings.ts.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.encodings.muxings.ts.drm.drm_api import DrmApi
from bitmovin.encoding.encodings.muxings.ts.ts_muxing_list_query_params import TsMuxingListQueryParams


class TsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(TsApi, self).__init__(
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

        self.drm = DrmApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, ts_muxing, **kwargs):
        """Add TS Segment Muxing"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/muxings/ts',
            ts_muxing,
            path_params={'encoding_id': encoding_id},
            type=TsMuxing,
            **kwargs
        )

    def delete(self, encoding_id, muxing_id, **kwargs):
        """Delete TS Segment Muxing"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, muxing_id, **kwargs):
        """TS Segment Muxing Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts/{muxing_id}',
            path_params={'encoding_id': encoding_id, 'muxing_id': muxing_id},
            type=TsMuxing,
            **kwargs
        )

    def list(self, encoding_id, query_params: TsMuxingListQueryParams = None, **kwargs):
        """List TS Segment Muxings"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/muxings/ts',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=TsMuxing,
            **kwargs
        )
