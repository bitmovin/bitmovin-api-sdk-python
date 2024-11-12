# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.akamai_account_region_settings import AkamaiAccountRegionSettings
from bitmovin_api_sdk.models.akamai_cloud_region import AkamaiCloudRegion
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.akamai.regions.akamai_account_region_settings_list_query_params import AkamaiAccountRegionSettingsListQueryParams


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

    def create(self, infrastructure_id, region, akamai_account_region_settings, **kwargs):
        # type: (string_types, AkamaiCloudRegion, AkamaiAccountRegionSettings, dict) -> AkamaiAccountRegionSettings
        """Add Akamai account region settings

        :param infrastructure_id: Id of the Akamai account
        :type infrastructure_id: string_types, required
        :param region: Akamai region
        :type region: AkamaiCloudRegion, required
        :param akamai_account_region_settings: The Akamai account region settings to be added
        :type akamai_account_region_settings: AkamaiAccountRegionSettings, required
        :return: Akamai account region settings
        :rtype: AkamaiAccountRegionSettings
        """

        return self.api_client.post(
            '/encoding/infrastructure/akamai/{infrastructure_id}/regions/{region}',
            akamai_account_region_settings,
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AkamaiAccountRegionSettings,
            **kwargs
        )

    def delete(self, infrastructure_id, region, **kwargs):
        # type: (string_types, AkamaiCloudRegion, dict) -> AkamaiAccountRegionSettings
        """Delete Akamai account region settings

        :param infrastructure_id: Id of the Akamai account
        :type infrastructure_id: string_types, required
        :param region: Akamai region
        :type region: AkamaiCloudRegion, required
        :return: Akamai account region settings
        :rtype: AkamaiAccountRegionSettings
        """

        return self.api_client.delete(
            '/encoding/infrastructure/akamai/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AkamaiAccountRegionSettings,
            **kwargs
        )

    def get(self, infrastructure_id, region, **kwargs):
        # type: (string_types, AkamaiCloudRegion, dict) -> AkamaiAccountRegionSettings
        """Akamai account region settings details

        :param infrastructure_id: Id of the Akamai account
        :type infrastructure_id: string_types, required
        :param region: Akamai region
        :type region: AkamaiCloudRegion, required
        :return: Region settings for specified region
        :rtype: AkamaiAccountRegionSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/akamai/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AkamaiAccountRegionSettings,
            **kwargs
        )

    def list(self, infrastructure_id, query_params=None, **kwargs):
        # type: (string_types, AkamaiAccountRegionSettingsListQueryParams, dict) -> AkamaiAccountRegionSettings
        """List Akamai account region settings

        :param infrastructure_id: Id of the Akamai account
        :type infrastructure_id: string_types, required
        :param query_params: Query parameters
        :type query_params: AkamaiAccountRegionSettingsListQueryParams
        :return: List of Akamai account region settings
        :rtype: AkamaiAccountRegionSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/akamai/{infrastructure_id}/regions',
            path_params={'infrastructure_id': infrastructure_id},
            query_params=query_params,
            pagination_response=True,
            type=AkamaiAccountRegionSettings,
            **kwargs
        )
