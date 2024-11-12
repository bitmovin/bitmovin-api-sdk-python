# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.gce_account import GceAccount
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.gce.regions.regions_api import RegionsApi
from bitmovin_api_sdk.encoding.infrastructure.gce.gce_account_list_query_params import GceAccountListQueryParams


class GceApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(GceApi, self).__init__(
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

    def create(self, gce_account, **kwargs):
        # type: (GceAccount, dict) -> GceAccount
        """Add GCE Account

        :param gce_account: The GCE Account to be added
        :type gce_account: GceAccount, required
        :return: GCE account
        :rtype: GceAccount
        """

        return self.api_client.post(
            '/encoding/infrastructure/gce',
            gce_account,
            type=GceAccount,
            **kwargs
        )

    def delete(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> GceAccount
        """Delete GCE Account

        :param infrastructure_id: Id of the GCE account
        :type infrastructure_id: string_types, required
        :return: GCE account
        :rtype: GceAccount
        """

        return self.api_client.delete(
            '/encoding/infrastructure/gce/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=GceAccount,
            **kwargs
        )

    def get(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> GceAccount
        """GCE Account Details

        :param infrastructure_id: Id of the GCE account
        :type infrastructure_id: string_types, required
        :return: GCE account
        :rtype: GceAccount
        """

        return self.api_client.get(
            '/encoding/infrastructure/gce/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=GceAccount,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (GceAccountListQueryParams, dict) -> GceAccount
        """List GCE Accounts

        :param query_params: Query parameters
        :type query_params: GceAccountListQueryParams
        :return: List of GCE accounts
        :rtype: GceAccount
        """

        return self.api_client.get(
            '/encoding/infrastructure/gce',
            query_params=query_params,
            pagination_response=True,
            type=GceAccount,
            **kwargs
        )
