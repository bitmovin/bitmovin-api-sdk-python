# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.generic_s3_input import GenericS3Input
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.inputs.genericS3.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.inputs.genericS3.generic_s3_input_list_query_params import GenericS3InputListQueryParams


class GenericS3Api(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
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
        """Create Generic S3 Input"""

        return self.api_client.post(
            '/encoding/inputs/generic-s3',
            generic_s3_input,
            type=GenericS3Input,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete Generic S3 Input"""

        return self.api_client.delete(
            '/encoding/inputs/generic-s3/{input_id}',
            path_params={'input_id': input_id},
            type=GenericS3Input,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """Generic S3 Input Details"""

        return self.api_client.get(
            '/encoding/inputs/generic-s3/{input_id}',
            path_params={'input_id': input_id},
            type=GenericS3Input,
            **kwargs
        )

    def list(self, query_params: GenericS3InputListQueryParams = None, **kwargs):
        """List Generic S3 Inputs"""

        return self.api_client.get(
            '/encoding/inputs/generic-s3',
            query_params=query_params,
            pagination_response=True,
            type=GenericS3Input,
            **kwargs
        )
