# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.azure_account_region_settings import AzureAccountRegionSettings
from bitmovin_api_sdk.models.azure_cloud_region import AzureCloudRegion
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.azure.regions.azure_account_region_settings_list_query_params import AzureAccountRegionSettingsListQueryParams


class RegionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(RegionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, infrastructure_id, region, azure_account_region_settings, **kwargs):
        # type: (string_types, AzureCloudRegion, AzureAccountRegionSettings, dict) -> AzureAccountRegionSettings
        """Add Azure Region Setting

        :param infrastructure_id: Id of the Azure account
        :type infrastructure_id: string_types, required
        :param region: Azure region.
        :type region: AzureCloudRegion, required
        :param azure_account_region_settings: The Azure Region Settings to be added
        :type azure_account_region_settings: AzureAccountRegionSettings, required
        :return: Azure account
        :rtype: AzureAccountRegionSettings
        """

        return self.api_client.post(
            '/encoding/infrastructure/azure/{infrastructure_id}/regions/{region}',
            azure_account_region_settings,
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AzureAccountRegionSettings,
            **kwargs
        )

    def delete(self, infrastructure_id, region, **kwargs):
        # type: (string_types, AzureCloudRegion, dict) -> AzureAccountRegionSettings
        """Delete Azure Region Settings

        :param infrastructure_id: Id of the Azure account
        :type infrastructure_id: string_types, required
        :param region: Azure region.
        :type region: AzureCloudRegion, required
        :return: Region settings for specified region
        :rtype: AzureAccountRegionSettings
        """

        return self.api_client.delete(
            '/encoding/infrastructure/azure/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AzureAccountRegionSettings,
            **kwargs
        )

    def get(self, infrastructure_id, region, **kwargs):
        # type: (string_types, AzureCloudRegion, dict) -> AzureAccountRegionSettings
        """Azure Region Settings Details

        :param infrastructure_id: Id of the Azure account
        :type infrastructure_id: string_types, required
        :param region: Azure region.
        :type region: AzureCloudRegion, required
        :return: Region settings for specified region
        :rtype: AzureAccountRegionSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/azure/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AzureAccountRegionSettings,
            **kwargs
        )

    def list(self, infrastructure_id, query_params=None, **kwargs):
        # type: (string_types, AzureAccountRegionSettingsListQueryParams, dict) -> AzureAccountRegionSettings
        """List Azure Region Settings

        :param infrastructure_id: Id of the Azure account
        :type infrastructure_id: string_types, required
        :param query_params: Query parameters
        :type query_params: AzureAccountRegionSettingsListQueryParams
        :return: List of Azure Region Settings
        :rtype: AzureAccountRegionSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/azure/{infrastructure_id}/regions',
            path_params={'infrastructure_id': infrastructure_id},
            query_params=query_params,
            pagination_response=True,
            type=AzureAccountRegionSettings,
            **kwargs
        )
