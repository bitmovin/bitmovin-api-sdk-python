# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.oci_account import OciAccount
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.oci.regions.regions_api import RegionsApi
from bitmovin_api_sdk.encoding.infrastructure.oci.oci_account_list_query_params import OciAccountListQueryParams


class OciApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(OciApi, self).__init__(
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

    def create(self, oci_account, **kwargs):
        # type: (OciAccount, dict) -> OciAccount
        """Add OCI account

        :param oci_account: The OCI account to be added
        :type oci_account: OciAccount, required
        :return: OCI account
        :rtype: OciAccount
        """

        return self.api_client.post(
            '/encoding/infrastructure/oci',
            oci_account,
            type=OciAccount,
            **kwargs
        )

    def delete(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> OciAccount
        """Delete OCI account

        :param infrastructure_id: Id of the OCI account
        :type infrastructure_id: string_types, required
        :return: OCI account
        :rtype: OciAccount
        """

        return self.api_client.delete(
            '/encoding/infrastructure/oci/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=OciAccount,
            **kwargs
        )

    def get(self, infrastructure_id, **kwargs):
        # type: (string_types, dict) -> OciAccount
        """OCI account details

        :param infrastructure_id: Id of the OCI account
        :type infrastructure_id: string_types, required
        :return: OCI account
        :rtype: OciAccount
        """

        return self.api_client.get(
            '/encoding/infrastructure/oci/{infrastructure_id}',
            path_params={'infrastructure_id': infrastructure_id},
            type=OciAccount,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (OciAccountListQueryParams, dict) -> OciAccount
        """List OCI accounts

        :param query_params: Query parameters
        :type query_params: OciAccountListQueryParams
        :return: List of OCI accounts
        :rtype: OciAccount
        """

        return self.api_client.get(
            '/encoding/infrastructure/oci',
            query_params=query_params,
            pagination_response=True,
            type=OciAccount,
            **kwargs
        )
