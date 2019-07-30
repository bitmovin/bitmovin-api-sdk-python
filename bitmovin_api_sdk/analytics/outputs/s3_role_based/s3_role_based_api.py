# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.s3_role_based_output import S3RoleBasedOutput
from bitmovin_api_sdk.analytics.outputs.s3_role_based.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.analytics.outputs.s3_role_based.s3_role_based_output_list_query_params import S3RoleBasedOutputListQueryParams


class S3RoleBasedApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (S3RoleBasedOutput, dict) -> S3RoleBasedOutput
        """Create S3 Role-based Output

        :param s3_role_based_output: The S3 Role-based output to be created
        :type s3_role_based_output: S3RoleBasedOutput, required
        :return: S3 Role-based Output
        :rtype: S3RoleBasedOutput
        """

        return self.api_client.post(
            '/analytics/outputs/s3-role-based',
            s3_role_based_output,
            type=S3RoleBasedOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> S3RoleBasedOutput
        """Delete S3 Role-based Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the input
        :rtype: S3RoleBasedOutput
        """

        return self.api_client.delete(
            '/analytics/outputs/s3-role-based/{output_id}',
            path_params={'output_id': output_id},
            type=S3RoleBasedOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> S3RoleBasedOutput
        """S3 Role-based Output Details

        :param output_id: Id of the input
        :type output_id: string_types, required
        :return: S3 Role-based Output
        :rtype: S3RoleBasedOutput
        """

        return self.api_client.get(
            '/analytics/outputs/s3-role-based/{output_id}',
            path_params={'output_id': output_id},
            type=S3RoleBasedOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (S3RoleBasedOutputListQueryParams, dict) -> S3RoleBasedOutput
        """List S3 Role-based Outputs

        :param query_params: Query parameters
        :type query_params: S3RoleBasedOutputListQueryParams
        :return: List of S3 Role-based Outputs
        :rtype: S3RoleBasedOutput
        """

        return self.api_client.get(
            '/analytics/outputs/s3-role-based',
            query_params=query_params,
            pagination_response=True,
            type=S3RoleBasedOutput,
            **kwargs
        )
