# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.gce_account_region_settings import GceAccountRegionSettings
from bitmovin_api_sdk.models.google_cloud_region import GoogleCloudRegion
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.gce.regions.gce_account_region_settings_list_query_params import GceAccountRegionSettingsListQueryParams


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

    def create(self, infrastructure_id, region, gce_account_region_settings, **kwargs):
        # type: (string_types, GoogleCloudRegion, GceAccountRegionSettings, dict) -> GceAccountRegionSettings
        """Add Google Cloud Region Setting

        :param infrastructure_id: Id of the Google Cloud Connect infrastructure resource
        :type infrastructure_id: string_types, required
        :param region: Google Cloud Region.
        :type region: GoogleCloudRegion, required
        :param gce_account_region_settings: The Google Cloud Region Settings to be added
        :type gce_account_region_settings: GceAccountRegionSettings, required
        :return: Google Cloud Account
        :rtype: GceAccountRegionSettings
        """

        return self.api_client.post(
            '/encoding/infrastructure/gce/{infrastructure_id}/regions/{region}',
            gce_account_region_settings,
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=GceAccountRegionSettings,
            **kwargs
        )

    def delete(self, infrastructure_id, region, **kwargs):
        # type: (string_types, GoogleCloudRegion, dict) -> GceAccountRegionSettings
        """Delete Google Cloud Region Settings

        :param infrastructure_id: Id of the Google Cloud Connect infrastructure resource
        :type infrastructure_id: string_types, required
        :param region: Google Cloud Region
        :type region: GoogleCloudRegion, required
        :return: Region settings for specified region
        :rtype: GceAccountRegionSettings
        """

        return self.api_client.delete(
            '/encoding/infrastructure/gce/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=GceAccountRegionSettings,
            **kwargs
        )

    def get(self, infrastructure_id, region, **kwargs):
        # type: (string_types, GoogleCloudRegion, dict) -> GceAccountRegionSettings
        """Google Cloud Region Settings Details

        :param infrastructure_id: Id of the Google Cloud Connect infrastructure resource
        :type infrastructure_id: string_types, required
        :param region: Google Cloud region.
        :type region: GoogleCloudRegion, required
        :return: Region settings for specified region
        :rtype: GceAccountRegionSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/gce/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=GceAccountRegionSettings,
            **kwargs
        )

    def list(self, infrastructure_id, query_params=None, **kwargs):
        # type: (string_types, GceAccountRegionSettingsListQueryParams, dict) -> GceAccountRegionSettings
        """List Google Cloud Region Settings

        :param infrastructure_id: Id of the Google Cloud Connect infrastructure resource
        :type infrastructure_id: string_types, required
        :param query_params: Query parameters
        :type query_params: GceAccountRegionSettingsListQueryParams
        :return: List of Google Cloud Region Settings
        :rtype: GceAccountRegionSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/gce/{infrastructure_id}/regions',
            path_params={'infrastructure_id': infrastructure_id},
            query_params=query_params,
            pagination_response=True,
            type=GceAccountRegionSettings,
            **kwargs
        )
