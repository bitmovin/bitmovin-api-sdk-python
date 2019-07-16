# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.aws_account import AwsAccount
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.aws.regions.regions_api import RegionsApi
from bitmovin_api_sdk.encoding.infrastructure.aws.aws_account_list_query_params import AwsAccountListQueryParams


class AwsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

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
        # type: (AwsAccount, dict) -> AwsAccount
        """Add AWS Account

        :param aws_account: The AWS Account to be added
        :type aws_account: AwsAccount, required
        :return: AWS account
        :rtype: AwsAccount
        """

        return self.api_client.post(
            '/encoding/infrastructure/aws',
            aws_account,
            type=AwsAccount,
            **kwargs
        )

    def delete(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> AwsAccount
        """Delete AWS Account

        :param infrastructure_id: Id of the AWS account
        :type infrastructure_id: string_types, required
        :return: Id of the AWS account
        :rtype: AwsAccount
        """

        return self.api_client.delete(
            '/encoding/infrastructure/aws/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=AwsAccount,
            **kwargs
        )

    def get(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> AwsAccount
        """AWS Account Details

        :param infrastructure_id: Id of the AWS account
        :type infrastructure_id: string_types, required
        :return: AWS account
        :rtype: AwsAccount
        """

        return self.api_client.get(
            '/encoding/infrastructure/aws/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=AwsAccount,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AwsAccountListQueryParams, dict) -> AwsAccount
        """List AWS Accounts

        :param query_params: Query parameters
        :type query_params: AwsAccountListQueryParams
        :return: List of AWS accounts
        :rtype: AwsAccount
        """

        return self.api_client.get(
            '/encoding/infrastructure/aws',
            query_params=query_params,
            pagination_response=True,
            type=AwsAccount,
            **kwargs
        )
