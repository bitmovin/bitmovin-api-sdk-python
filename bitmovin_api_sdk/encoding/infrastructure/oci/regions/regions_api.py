# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.oci_account_region_settings import OciAccountRegionSettings
from bitmovin_api_sdk.models.oci_cloud_region import OciCloudRegion
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.oci.regions.oci_account_region_settings_list_query_params import OciAccountRegionSettingsListQueryParams


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

    def create(self, infrastructure_id, region, oci_account_region_settings, **kwargs):
        # type: (string_types, OciCloudRegion, OciAccountRegionSettings, dict) -> OciAccountRegionSettings
        """Add OCI account region settings

        :param infrastructure_id: Id of the OCI account
        :type infrastructure_id: string_types, required
        :param region: OCI region
        :type region: OciCloudRegion, required
        :param oci_account_region_settings: The OCI account region settings to be added
        :type oci_account_region_settings: OciAccountRegionSettings, required
        :return: OCI account region settings
        :rtype: OciAccountRegionSettings
        """

        return self.api_client.post(
            '/encoding/infrastructure/oci/{infrastructure_id}/regions/{region}',
            oci_account_region_settings,
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=OciAccountRegionSettings,
            **kwargs
        )

    def delete(self, infrastructure_id, region, **kwargs):
        # type: (string_types, OciCloudRegion, dict) -> OciAccountRegionSettings
        """Delete OCI account region settings

        :param infrastructure_id: Id of the OCI account
        :type infrastructure_id: string_types, required
        :param region: OCI region
        :type region: OciCloudRegion, required
        :return: OCI account region settings
        :rtype: OciAccountRegionSettings
        """

        return self.api_client.delete(
            '/encoding/infrastructure/oci/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=OciAccountRegionSettings,
            **kwargs
        )

    def get(self, infrastructure_id, region, **kwargs):
        # type: (string_types, OciCloudRegion, dict) -> OciAccountRegionSettings
        """OCI account region settings details

        :param infrastructure_id: Id of the OCI account
        :type infrastructure_id: string_types, required
        :param region: OCI region
        :type region: OciCloudRegion, required
        :return: Region settings for specified region
        :rtype: OciAccountRegionSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/oci/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=OciAccountRegionSettings,
            **kwargs
        )

    def list(self, infrastructure_id, query_params=None, **kwargs):
        # type: (string_types, OciAccountRegionSettingsListQueryParams, dict) -> OciAccountRegionSettings
        """List OCI account region settings

        :param infrastructure_id: Id of the OCI account
        :type infrastructure_id: string_types, required
        :param query_params: Query parameters
        :type query_params: OciAccountRegionSettingsListQueryParams
        :return: List of OCI account region settings
        :rtype: OciAccountRegionSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/oci/{infrastructure_id}/regions',
            path_params={'infrastructure_id': infrastructure_id},
            query_params=query_params,
            pagination_response=True,
            type=OciAccountRegionSettings,
            **kwargs
        )
