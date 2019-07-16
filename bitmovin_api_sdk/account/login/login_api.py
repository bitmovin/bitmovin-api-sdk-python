# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.account_information import AccountInformation
from bitmovin_api_sdk.models.login import Login
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class LoginApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LoginApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, login, **kwargs):
        # type: (Login, dict) -> AccountInformation
        """Login

        :param login: Login Credentials
        :type login: Login, required
        :return: Account Information
        :rtype: AccountInformation
        """

        return self.api_client.post(
            '/account/login',
            login,
            type=AccountInformation,
            **kwargs
        )
