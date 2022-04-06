# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.cdn_output import CdnOutput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.cdn.cdn_output_list_query_params import CdnOutputListQueryParams


class CdnApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(CdnApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> CdnOutput
        """CDN Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: CDN output
        :rtype: CdnOutput
        """

        return self.api_client.get(
            '/encoding/outputs/cdn/{output_id}',
            path_params={'output_id': output_id},
            type=CdnOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (CdnOutputListQueryParams, dict) -> CdnOutput
        """List CDN Outputs

        :param query_params: Query parameters
        :type query_params: CdnOutputListQueryParams
        :return: List of CDN outputs
        :rtype: CdnOutput
        """

        return self.api_client.get(
            '/encoding/outputs/cdn',
            query_params=query_params,
            pagination_response=True,
            type=CdnOutput,
            **kwargs
        )
