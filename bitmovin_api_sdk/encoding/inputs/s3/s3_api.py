# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.s3_input import S3Input
from bitmovin_api_sdk.encoding.inputs.s3.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.s3.s3_input_list_query_params import S3InputListQueryParams


class S3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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

    def create(self, s3_input, **kwargs):
        # type: (S3Input, dict) -> S3Input
        """Create S3 Input

        :param s3_input: The S3 input to be created  The following permissions are required for S3 input:   * s3:GetObject   * s3:GetBucketLocation, 
        :type s3_input: S3Input, required
        :return: S3 input
        :rtype: S3Input
        """

        return self.api_client.post(
            '/encoding/inputs/s3',
            s3_input,
            type=S3Input,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete S3 Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the deleted input
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/inputs/s3/{input_id}',
            path_params={'input_id': input_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> S3Input
        """S3 Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: S3 input
        :rtype: S3Input
        """

        return self.api_client.get(
            '/encoding/inputs/s3/{input_id}',
            path_params={'input_id': input_id},
            type=S3Input,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (S3InputListQueryParams, dict) -> S3Input
        """List S3 Inputs

        :param query_params: Query parameters
        :type query_params: S3InputListQueryParams
        :return: List of S3 inputs
        :rtype: S3Input
        """

        return self.api_client.get(
            '/encoding/inputs/s3',
            query_params=query_params,
            pagination_response=True,
            type=S3Input,
            **kwargs
        )
