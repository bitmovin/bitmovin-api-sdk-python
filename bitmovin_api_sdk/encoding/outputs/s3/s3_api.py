# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.s3_output import S3Output
from bitmovin_api_sdk.encoding.outputs.s3.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.s3.s3_output_list_query_params import S3OutputListQueryParams


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

    def create(self, s3_output, **kwargs):
        # type: (S3Output, dict) -> S3Output
        """Create S3 Output

        :param s3_output: The S3 output to be created  The following permissions are required for S3 output:  * s3:PutObject  * s3:PutObjectAcl  * s3:ListBucket  * s3:GetBucketLocation 
        :type s3_output: S3Output, required
        :return: S3 output
        :rtype: S3Output
        """

        return self.api_client.post(
            '/encoding/outputs/s3',
            s3_output,
            type=S3Output,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> S3Output
        """Delete S3 Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the input
        :rtype: S3Output
        """

        return self.api_client.delete(
            '/encoding/outputs/s3/{output_id}',
            path_params={'output_id': output_id},
            type=S3Output,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> S3Output
        """S3 Output Details

        :param output_id: Id of the input
        :type output_id: string_types, required
        :return: S3 output
        :rtype: S3Output
        """

        return self.api_client.get(
            '/encoding/outputs/s3/{output_id}',
            path_params={'output_id': output_id},
            type=S3Output,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (S3OutputListQueryParams, dict) -> S3Output
        """List S3 Outputs

        :param query_params: Query parameters
        :type query_params: S3OutputListQueryParams
        :return: List of S3 outputs
        :rtype: S3Output
        """

        return self.api_client.get(
            '/encoding/outputs/s3',
            query_params=query_params,
            pagination_response=True,
            type=S3Output,
            **kwargs
        )
