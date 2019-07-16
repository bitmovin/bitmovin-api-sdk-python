# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.psnr_quality_metric import PsnrQualityMetric
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.encodings.streams.qc.psnr.psnr_quality_metric_list_query_params import PsnrQualityMetricListQueryParams


class PsnrApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(PsnrApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, encoding_id, stream_id, **kwargs):
        # type: (string_types, string_types, dict) -> BitmovinResponse
        """Activate PSNR quality metrics for the selected stream

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :return: Id of the Audio Mix configuration
        :rtype: BitmovinResponse
        """

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/qc/psnr',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params=None, **kwargs):
        # type: (string_types, string_types, PsnrQualityMetricListQueryParams, dict) -> PsnrQualityMetric
        """Get Stream PSNR metrics

        :param encoding_id: Id of the encoding.
        :type encoding_id: string_types, required
        :param stream_id: Id of the stream.
        :type stream_id: string_types, required
        :param query_params: Query parameters
        :type query_params: PsnrQualityMetricListQueryParams
        :return: List PSNR metrics
        :rtype: PsnrQualityMetric
        """

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/qc/psnr',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=PsnrQualityMetric,
            **kwargs
        )
