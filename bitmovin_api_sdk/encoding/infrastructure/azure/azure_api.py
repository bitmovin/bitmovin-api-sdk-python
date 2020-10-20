# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.azure_account import AzureAccount
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.azure.regions.regions_api import RegionsApi
from bitmovin_api_sdk.encoding.infrastructure.azure.azure_account_list_query_params import AzureAccountListQueryParams


class AzureApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AzureApi, self).__init__(
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

    def create(self, azure_account, **kwargs):
        # type: (AzureAccount, dict) -> AzureAccount
        """Add Azure Account

        :param azure_account: The Azure Account to be added
        :type azure_account: AzureAccount, required
        :return: Azure account
        :rtype: AzureAccount
        """

        return self.api_client.post(
            '/encoding/infrastructure/azure',
            azure_account,
            type=AzureAccount,
            **kwargs
        )

    def delete(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> AzureAccount
        """Delete Azure Account

        :param infrastructure_id: Id of the Azure account
        :type infrastructure_id: string_types, required
        :return: Id of the Azure account
        :rtype: AzureAccount
        """

        return self.api_client.delete(
            '/encoding/infrastructure/azure/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=AzureAccount,
            **kwargs
        )

    def get(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> AzureAccount
        """Azure Account Details

        :param infrastructure_id: Id of the Azure account
        :type infrastructure_id: string_types, required
        :return: Azure account
        :rtype: AzureAccount
        """

        return self.api_client.get(
            '/encoding/infrastructure/azure/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=AzureAccount,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AzureAccountListQueryParams, dict) -> AzureAccount
        """List Azure Accounts

        :param query_params: Query parameters
        :type query_params: AzureAccountListQueryParams
        :return: List of Azure accounts
        :rtype: AzureAccount
        """

        return self.api_client.get(
            '/encoding/infrastructure/azure',
            query_params=query_params,
            pagination_response=True,
            type=AzureAccount,
            **kwargs
        )
