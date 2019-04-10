# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.models.s3_role_based_output import S3RoleBasedOutput
from bitmovin.analytics.outputs.s3RoleBased.customdata.customdata_api import CustomdataApi
from bitmovin.analytics.outputs.s3RoleBased.s3_role_based_output_list_query_params import S3RoleBasedOutputListQueryParams


class S3RoleBasedApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(S3RoleBasedApi, self).__init__(
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

    def create(self, s3_role_based_output, **kwargs):
        """Create S3 Role-based Output"""

        return self.api_client.post(
            '/analytics/outputs/s3-role-based',
            s3_role_based_output,
            type=S3RoleBasedOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        """Delete S3 Role-based Output"""

        return self.api_client.delete(
            '/analytics/outputs/s3-role-based/{output_id}',
            path_params={'output_id': output_id},
            type=S3RoleBasedOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        """S3 Role-based Output Details"""

        return self.api_client.get(
            '/analytics/outputs/s3-role-based/{output_id}',
            path_params={'output_id': output_id},
            type=S3RoleBasedOutput,
            **kwargs
        )

    def list(self, query_params: S3RoleBasedOutputListQueryParams = None, **kwargs):
        """List S3 Role-based Outputs"""

        return self.api_client.get(
            '/analytics/outputs/s3-role-based',
            query_params=query_params,
            pagination_response=True,
            type=S3RoleBasedOutput,
            **kwargs
        )
