# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.gcs_output import GcsOutput
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.outputs.gcs.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.outputs.gcs.gcs_output_list_query_params import GcsOutputListQueryParams


class GcsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(GcsApi, self).__init__(
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

    def create(self, gcs_output, **kwargs):
        """Create GCS Output"""

        return self.api_client.post(
            '/encoding/outputs/gcs',
            gcs_output,
            type=GcsOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete GCS Output"""

        return self.api_client.delete(
            '/encoding/outputs/gcs/{output_id}',
            path_params={'output_id': output_id},
            type=GcsOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """GCS Output Details"""

        return self.api_client.get(
            '/encoding/outputs/gcs/{output_id}',
            path_params={'output_id': output_id},
            type=GcsOutput,
            **kwargs
        )

    def list(self, query_params: GcsOutputListQueryParams = None, **kwargs):
        """List GCS Outputs"""

        return self.api_client.get(
            '/encoding/outputs/gcs',
            query_params=query_params,
            pagination_response=True,
            type=GcsOutput,
            **kwargs
        )
