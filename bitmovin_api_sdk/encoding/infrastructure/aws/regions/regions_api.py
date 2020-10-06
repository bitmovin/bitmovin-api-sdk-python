# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.aws_account_region_settings import AwsAccountRegionSettings
from bitmovin_api_sdk.models.aws_cloud_region import AwsCloudRegion
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.infrastructure.aws.regions.aws_account_region_settings_list_query_params import AwsAccountRegionSettingsListQueryParams


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

    def create(self, infrastructure_id, region, aws_account_region_settings, **kwargs):
        # type: (string_types, AwsCloudRegion, AwsAccountRegionSettings, dict) -> AwsAccountRegionSettings
        """Add AWS Region Setting

        :param infrastructure_id: Id of the AWS account
        :type infrastructure_id: string_types, required
        :param region: AWS region.
        :type region: AwsCloudRegion, required
        :param aws_account_region_settings: The AWS Region Settings to be added
        :type aws_account_region_settings: AwsAccountRegionSettings, required
        :return: AWS account
        :rtype: AwsAccountRegionSettings
        """

        return self.api_client.post(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions/{region}',
            aws_account_region_settings,
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AwsAccountRegionSettings,
            **kwargs
        )

    def delete(self, infrastructure_id, region, **kwargs):
        # type: (string_types, AwsCloudRegion, dict) -> AwsAccountRegionSettings
        """Delete AWS Region Settings

        :param infrastructure_id: Id of the AWS account
        :type infrastructure_id: string_types, required
        :param region: AWS region.
        :type region: AwsCloudRegion, required
        :return: Region settings for specified region
        :rtype: AwsAccountRegionSettings
        """

        return self.api_client.delete(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AwsAccountRegionSettings,
            **kwargs
        )

    def get(self, infrastructure_id, region, **kwargs):
        # type: (string_types, AwsCloudRegion, dict) -> AwsAccountRegionSettings
        """AWS Region Settings Details

        :param infrastructure_id: Id of the AWS account
        :type infrastructure_id: string_types, required
        :param region: AWS region.
        :type region: AwsCloudRegion, required
        :return: Region settings for specified region
        :rtype: AwsAccountRegionSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AwsAccountRegionSettings,
            **kwargs
        )

    def list(self, infrastructure_id, query_params=None, **kwargs):
        # type: (string_types, AwsAccountRegionSettingsListQueryParams, dict) -> AwsAccountRegionSettings
        """List AWS Region Settings

        :param infrastructure_id: Id of the AWS account
        :type infrastructure_id: string_types, required
        :param query_params: Query parameters
        :type query_params: AwsAccountRegionSettingsListQueryParams
        :return: List of AWS Region Settings
        :rtype: AwsAccountRegionSettings
        """

        return self.api_client.get(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions',
            path_params={'infrastructure_id': infrastructure_id},
            query_params=query_params,
            pagination_response=True,
            type=AwsAccountRegionSettings,
            **kwargs
        )
