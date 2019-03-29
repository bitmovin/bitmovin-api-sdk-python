# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.aws_account_region_settings import AwsAccountRegionSettings
from bitmovin.models.aws_cloud_region import AwsCloudRegion
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.infrastructure.aws.regions.aws_account_region_settings_list_query_params import AwsAccountRegionSettingsListQueryParams


class RegionsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
        super(RegionsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, infrastructure_id, region, aws_account_region_settings, **kwargs):
        """Add AWS Region Setting"""

        return self.api_client.post(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions/{region}',
            aws_account_region_settings,
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AwsAccountRegionSettings,
            **kwargs
        )

    def delete(self, infrastructure_id, region, **kwargs):
        """Delete AWS Region Settings"""

        return self.api_client.delete(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AwsAccountRegionSettings,
            **kwargs
        )

    def get(self, infrastructure_id, region, **kwargs):
        """AWS Region Settings Details"""

        return self.api_client.get(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions/{region}',
            path_params={'infrastructure_id': infrastructure_id, 'region': region},
            type=AwsAccountRegionSettings,
            **kwargs
        )

    def list(self, infrastructure_id, query_params: AwsAccountRegionSettingsListQueryParams = None, **kwargs):
        """List AWS Region Settings"""

        return self.api_client.get(
            '/encoding/infrastructure/aws/{infrastructure_id}/regions',
            path_params={'infrastructure_id': infrastructure_id},
            query_params=query_params,
            pagination_response=True,
            type=AwsAccountRegionSettings,
            **kwargs
        )
