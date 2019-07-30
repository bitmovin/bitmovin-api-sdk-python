# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.generic_s3_input import GenericS3Input
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.generic_s3.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.generic_s3.generic_s3_input_list_query_params import GenericS3InputListQueryParams


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

    def create(self, generic_s3_input, **kwargs):
        # type: (GenericS3Input, dict) -> GenericS3Input
        """Create Generic S3 Input

        :param generic_s3_input: The GenericS3 input to be created
        :type generic_s3_input: GenericS3Input, required
        :return: Generic S3 input
        :rtype: GenericS3Input
        """

        return self.api_client.post(
            '/encoding/inputs/generic-s3',
            generic_s3_input,
            type=GenericS3Input,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> GenericS3Input
        """Delete Generic S3 Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: GenericS3Input
        """

        return self.api_client.delete(
            '/encoding/inputs/generic-s3/{input_id}',
            path_params={'input_id': input_id},
            type=GenericS3Input,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> GenericS3Input
        """Generic S3 Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Generic S3 input details
        :rtype: GenericS3Input
        """

        return self.api_client.get(
            '/encoding/inputs/generic-s3/{input_id}',
            path_params={'input_id': input_id},
            type=GenericS3Input,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (GenericS3InputListQueryParams, dict) -> GenericS3Input
        """List Generic S3 Inputs

        :param query_params: Query parameters
        :type query_params: GenericS3InputListQueryParams
        :return: List of generic S3 inputs
        :rtype: GenericS3Input
        """

        return self.api_client.get(
            '/encoding/inputs/generic-s3',
            query_params=query_params,
            pagination_response=True,
            type=GenericS3Input,
            **kwargs
        )
