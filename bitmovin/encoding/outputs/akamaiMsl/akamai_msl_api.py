# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.akamai_msl_output import AkamaiMslOutput
from bitmovin.models.bitmovin_response import BitmovinResponse
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.outputs.akamaiMsl.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.outputs.akamaiMsl.akamai_msl_output_list_query_params import AkamaiMslOutputListQueryParams


class AkamaiMslApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AkamaiMslApi, self).__init__(
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

    def create(self, akamai_msl_output, **kwargs):
        """Create Akamai MSL Output"""

        return self.api_client.post(
            '/encoding/outputs/akamai-msl',
            akamai_msl_output,
            type=AkamaiMslOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete Akamai MSL Output"""

        return self.api_client.delete(
            '/encoding/outputs/akamai-msl/{output_id}',
            path_params={'output_id': output_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """Akamai MSL Output Details"""

        return self.api_client.get(
            '/encoding/outputs/akamai-msl/{output_id}',
            path_params={'output_id': output_id},
            type=AkamaiMslOutput,
            **kwargs
        )

    def list(self, query_params: AkamaiMslOutputListQueryParams = None, **kwargs):
        """List Akamai MSL Outputs"""

        return self.api_client.get(
            '/encoding/outputs/akamai-msl',
            query_params=query_params,
            pagination_response=True,
            type=AkamaiMslOutput,
            **kwargs
        )
