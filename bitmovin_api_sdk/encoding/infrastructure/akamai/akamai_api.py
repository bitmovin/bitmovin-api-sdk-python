# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.akamai_account import AkamaiAccount
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.akamai.regions.regions_api import RegionsApi
from bitmovin_api_sdk.encoding.infrastructure.akamai.akamai_account_list_query_params import AkamaiAccountListQueryParams


class AkamaiApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AkamaiApi, self).__init__(
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

    def create(self, akamai_account, **kwargs):
        # type: (AkamaiAccount, dict) -> AkamaiAccount
        """Add Akamai account

        :param akamai_account: The Akamai account to be added
        :type akamai_account: AkamaiAccount, required
        :return: Akamai account
        :rtype: AkamaiAccount
        """

        return self.api_client.post(
            '/encoding/infrastructure/akamai',
            akamai_account,
            type=AkamaiAccount,
            **kwargs
        )

    def delete(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> AkamaiAccount
        """Delete Akamai account

        :param infrastructure_id: Id of the Akamai account
        :type infrastructure_id: string_types, required
        :return: Akamai account
        :rtype: AkamaiAccount
        """

        return self.api_client.delete(
            '/encoding/infrastructure/akamai/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=AkamaiAccount,
            **kwargs
        )

    def get(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> AkamaiAccount
        """Akamai account details

        :param infrastructure_id: Id of the Akamai account
        :type infrastructure_id: string_types, required
        :return: Akamai account
        :rtype: AkamaiAccount
        """

        return self.api_client.get(
            '/encoding/infrastructure/akamai/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=AkamaiAccount,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AkamaiAccountListQueryParams, dict) -> AkamaiAccount
        """List Akamai accounts

        :param query_params: Query parameters
        :type query_params: AkamaiAccountListQueryParams
        :return: List of Akamai accounts
        :rtype: AkamaiAccount
        """

        return self.api_client.get(
            '/encoding/infrastructure/akamai',
            query_params=query_params,
            pagination_response=True,
            type=AkamaiAccount,
            **kwargs
        )
