# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.account_api_key import AccountApiKey
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class ApiKeysApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ApiKeysApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, **kwargs):
        # type: (dict) -> AccountApiKey
        """Create Api Key

        :return: Api Key
        :rtype: AccountApiKey
        """

        return self.api_client.post(
            '/account/api-keys',
            type=AccountApiKey,
            **kwargs
        )

    def delete(self, api_key_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Api Key

        :param api_key_id: Id of the api key
        :type api_key_id: string_types, required
        :return: Id of the Api Key
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/account/api-keys/{api_key_id}',
            path_params={'api_key_id': api_key_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, api_key_id, **kwargs):
        # type: (string_types, dict) -> AccountApiKey
        """Get Api Key

        :param api_key_id: Id of the api key
        :type api_key_id: string_types, required
        :return: Service specific result
        :rtype: AccountApiKey
        """

        return self.api_client.get(
            '/account/api-keys/{api_key_id}',
            path_params={'api_key_id': api_key_id},
            type=AccountApiKey,
            **kwargs
        )

    def list(self, **kwargs):
        # type: (dict) -> AccountApiKey
        """List Api Keys

        :return: Api keys
        :rtype: AccountApiKey
        """

        return self.api_client.get(
            '/account/api-keys',
            pagination_response=True,
            type=AccountApiKey,
            **kwargs
        )
