# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.pcc_report import PccReport
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.player.testing.codec_compatibility.pcc_report_get_query_params import PccReportGetQueryParams


class CodecCompatibilityApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(CodecCompatibilityApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, query_params=None, **kwargs):
        # type: (PccReportGetQueryParams, dict) -> PccReport
        """Get Codec Compatibility Report

        :param query_params: Query parameters
        :type query_params: PccReportGetQueryParams
        :return:
        :rtype: PccReport
        """

        return self.api_client.get(
            '/player/testing/codec-compatibility',
            query_params=query_params,
            type=PccReport,
            **kwargs
        )
