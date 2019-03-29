# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.aws_account import AwsAccount
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.infrastructure.aws.regions.regions_api import RegionsApi
from bitmovin.encoding.infrastructure.aws.aws_account_list_query_params import AwsAccountListQueryParams


class AwsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(AwsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.regions = RegionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, aws_account, **kwargs):
        """Add AWS Account"""

        return self.api_client.post(
            '/encoding/infrastructure/aws',
            aws_account,
            type=AwsAccount,
            **kwargs
        )

    def delete(self, infrastructure_id, **kwargs):
        """Delete AWS Account"""

        return self.api_client.delete(
            '/encoding/infrastructure/aws/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=AwsAccount,
            **kwargs
        )

    def get(self, infrastructure_id, **kwargs):
        """AWS Account Details"""

        return self.api_client.get(
            '/encoding/infrastructure/aws/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=AwsAccount,
            **kwargs
        )

    def list(self, query_params: AwsAccountListQueryParams = None, **kwargs):
        """List AWS Accounts"""

        return self.api_client.get(
            '/encoding/infrastructure/aws',
            query_params=query_params,
            pagination_response=True,
            type=AwsAccount,
            **kwargs
        )
