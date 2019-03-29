# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.s3_output import S3Output
from bitmovin.encoding.outputs.s3.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.outputs.s3.s3_output_list_query_params import S3OutputListQueryParams


class S3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(S3Api, self).__init__(
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

    def create(self, s3_output, **kwargs):
        """Create S3 Output"""

        return self.api_client.post(
            '/encoding/outputs/s3',
            s3_output,
            type=S3Output,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete S3 Output"""

        return self.api_client.delete(
            '/encoding/outputs/s3/{output_id}',
            path_params={'output_id': output_id},
            type=S3Output,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """S3 Output Details"""

        return self.api_client.get(
            '/encoding/outputs/s3/{output_id}',
            path_params={'output_id': output_id},
            type=S3Output,
            **kwargs
        )

    def list(self, query_params: S3OutputListQueryParams = None, **kwargs):
        """List S3 Outputs"""

        return self.api_client.get(
            '/encoding/outputs/s3',
            query_params=query_params,
            pagination_response=True,
            type=S3Output,
            **kwargs
        )
