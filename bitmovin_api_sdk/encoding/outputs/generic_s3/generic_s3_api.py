# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.generic_s3_output import GenericS3Output
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.generic_s3.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.generic_s3.generic_s3_output_list_query_params import GenericS3OutputListQueryParams


class GenericS3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(GenericS3Api, self).__init__(
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

    def create(self, generic_s3_output, **kwargs):
        # type: (GenericS3Output, dict) -> GenericS3Output
        """Create Generic S3 Output

        :param generic_s3_output: The Generic S3 output to be created
        :type generic_s3_output: GenericS3Output, required
        :return: Generic S3 output
        :rtype: GenericS3Output
        """

        return self.api_client.post(
            '/encoding/outputs/generic-s3',
            generic_s3_output,
            type=GenericS3Output,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> GenericS3Output
        """Delete Generic S3 Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: GenericS3Output
        """

        return self.api_client.delete(
            '/encoding/outputs/generic-s3/{output_id}',
            path_params={'output_id': output_id},
            type=GenericS3Output,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> GenericS3Output
        """Generic S3 Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Generic S3 output details
        :rtype: GenericS3Output
        """

        return self.api_client.get(
            '/encoding/outputs/generic-s3/{output_id}',
            path_params={'output_id': output_id},
            type=GenericS3Output,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (GenericS3OutputListQueryParams, dict) -> GenericS3Output
        """List Generic S3 Outputs

        :param query_params: Query parameters
        :type query_params: GenericS3OutputListQueryParams
        :return: List of Generic S3 outputs
        :rtype: GenericS3Output
        """

        return self.api_client.get(
            '/encoding/outputs/generic-s3',
            query_params=query_params,
            pagination_response=True,
            type=GenericS3Output,
            **kwargs
        )
