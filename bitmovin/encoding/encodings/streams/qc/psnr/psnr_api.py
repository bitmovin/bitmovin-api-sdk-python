# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.psnr_quality_metric import PsnrQualityMetric
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.encodings.streams.qc.psnr.psnr_quality_metric_list_query_params import PsnrQualityMetricListQueryParams


class PsnrApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(PsnrApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream_id, **kwargs):
        """Activate PSNR quality metrics for the selected stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/qc/psnr',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params: PsnrQualityMetricListQueryParams = None, **kwargs):
        """Get Stream PSNR metrics"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/qc/psnr',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=PsnrQualityMetric,
            **kwargs
        )
