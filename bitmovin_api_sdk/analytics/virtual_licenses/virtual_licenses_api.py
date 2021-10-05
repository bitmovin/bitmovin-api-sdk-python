# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_virtual_license import AnalyticsVirtualLicense
from bitmovin_api_sdk.models.analytics_virtual_license_request import AnalyticsVirtualLicenseRequest
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.analytics.virtual_licenses.analytics_virtual_license_list_query_params import AnalyticsVirtualLicenseListQueryParams


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

    def create(self, analytics_virtual_license_request, **kwargs):
        # type: (AnalyticsVirtualLicenseRequest, dict) -> AnalyticsVirtualLicense
        """Create Analytics Virtual License

        :param analytics_virtual_license_request: Analytics Virtual License to be created
        :type analytics_virtual_license_request: AnalyticsVirtualLicenseRequest, required
        :return: Created Analytics Virtual license
        :rtype: AnalyticsVirtualLicense
        """

        return self.api_client.post(
            '/analytics/virtual-licenses',
            analytics_virtual_license_request,
            type=AnalyticsVirtualLicense,
            **kwargs
        )

    def delete(self, virtual_license_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Analytics Virtual License

        :param virtual_license_id: Virtual License id
        :type virtual_license_id: string_types, required
        :return: Id of deleted Virtual License
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/analytics/virtual-licenses/{virtual_license_id}',
            path_params={'virtual_license_id': virtual_license_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, virtual_license_id, **kwargs):
        # type: (string_types, dict) -> AnalyticsVirtualLicense
        """Analytics Virtual License

        :param virtual_license_id: Virtual license id
        :type virtual_license_id: string_types, required
        :return: Analytics Virtual License
        :rtype: AnalyticsVirtualLicense
        """

        return self.api_client.get(
            '/analytics/virtual-licenses/{virtual_license_id}',
            path_params={'virtual_license_id': virtual_license_id},
            type=AnalyticsVirtualLicense,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AnalyticsVirtualLicenseListQueryParams, dict) -> AnalyticsVirtualLicense
        """List Analytics Virtual Licenses

        :param query_params: Query parameters
        :type query_params: AnalyticsVirtualLicenseListQueryParams
        :return: List of Analytics Virtual licenses
        :rtype: AnalyticsVirtualLicense
        """

        return self.api_client.get(
            '/analytics/virtual-licenses',
            query_params=query_params,
            pagination_response=True,
            type=AnalyticsVirtualLicense,
            **kwargs
        )

    def update(self, virtual_license_id, analytics_virtual_license_request, **kwargs):
        # type: (string_types, AnalyticsVirtualLicenseRequest, dict) -> AnalyticsVirtualLicense
        """Update Analytics Virtual License

        :param virtual_license_id: Virtual license id
        :type virtual_license_id: string_types, required
        :param analytics_virtual_license_request: Analytics Virtual License details to be updated
        :type analytics_virtual_license_request: AnalyticsVirtualLicenseRequest, required
        :return: Updated Analytics Virtual License
        :rtype: AnalyticsVirtualLicense
        """

        return self.api_client.put(
            '/analytics/virtual-licenses/{virtual_license_id}',
            analytics_virtual_license_request,
            path_params={'virtual_license_id': virtual_license_id},
            type=AnalyticsVirtualLicense,
            **kwargs
        )
