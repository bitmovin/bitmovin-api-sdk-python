# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.virtual_license import VirtualLicense
from bitmovin_api_sdk.models.virtual_license_create_request import VirtualLicenseCreateRequest


class VirtualLicensesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(VirtualLicensesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, virtual_license_create_request, **kwargs):
        # type: (VirtualLicenseCreateRequest, dict) -> VirtualLicense
        """Create Virtual License

        :param virtual_license_create_request: Virtual License to be created
        :type virtual_license_create_request: VirtualLicenseCreateRequest, required
        :return: Created Virtual license
        :rtype: VirtualLicense
        """

        return self.api_client.post(
            '/analytics/virtual-licenses',
            virtual_license_create_request,
            type=VirtualLicense,
            **kwargs
        )
