# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.s3_role_based_input import S3RoleBasedInput
from bitmovin_api_sdk.encoding.inputs.s3_role_based.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.s3_role_based.s3_role_based_input_list_query_params import S3RoleBasedInputListQueryParams


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

    def create(self, s3_role_based_input, **kwargs):
        # type: (S3RoleBasedInput, dict) -> S3RoleBasedInput
        """Create S3 Role-based Input

        :param s3_role_based_input: The S3 Role-based input to be created  The following permissions are required for S3 Role-based input:   * s3:GetObject   * s3:GetBucketLocation, 
        :type s3_role_based_input: S3RoleBasedInput, required
        :return: S3 Role-based Input
        :rtype: S3RoleBasedInput
        """

        return self.api_client.post(
            '/encoding/inputs/s3-role-based',
            s3_role_based_input,
            type=S3RoleBasedInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> S3RoleBasedInput
        """Delete S3 Role-based Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: S3RoleBasedInput
        """

        return self.api_client.delete(
            '/encoding/inputs/s3-role-based/{input_id}',
            path_params={'input_id': input_id},
            type=S3RoleBasedInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> S3RoleBasedInput
        """S3 Role-based Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: S3 Role-based Input
        :rtype: S3RoleBasedInput
        """

        return self.api_client.get(
            '/encoding/inputs/s3-role-based/{input_id}',
            path_params={'input_id': input_id},
            type=S3RoleBasedInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (S3RoleBasedInputListQueryParams, dict) -> S3RoleBasedInput
        """List S3 Role-based Inputs

        :param query_params: Query parameters
        :type query_params: S3RoleBasedInputListQueryParams
        :return: List of S3 Role-based Inputs
        :rtype: S3RoleBasedInput
        """

        return self.api_client.get(
            '/encoding/inputs/s3-role-based',
            query_params=query_params,
            pagination_response=True,
            type=S3RoleBasedInput,
            **kwargs
        )
