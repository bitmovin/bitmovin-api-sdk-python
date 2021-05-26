# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.analytics_azure_output import AnalyticsAzureOutput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.analytics.outputs.azure.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.analytics.outputs.azure.analytics_azure_output_list_query_params import AnalyticsAzureOutputListQueryParams


class AzureApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AzureApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, analytics_azure_output, **kwargs):
        # type: (AnalyticsAzureOutput, dict) -> AnalyticsAzureOutput
        """Create Microsoft Azure Output

        :param analytics_azure_output: The Microsoft Azure output to be created
        :type analytics_azure_output: AnalyticsAzureOutput, required
        :return: Microsoft Azure output
        :rtype: AnalyticsAzureOutput
        """

        return self.api_client.post(
            '/analytics/outputs/azure',
            analytics_azure_output,
            type=AnalyticsAzureOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> AnalyticsAzureOutput
        """Delete Microsoft Azure Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: AnalyticsAzureOutput
        """

        return self.api_client.delete(
            '/analytics/outputs/azure/{output_id}',
            path_params={'output_id': output_id},
            type=AnalyticsAzureOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> AnalyticsAzureOutput
        """Microsoft Azure Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Microsoft Azure output
        :rtype: AnalyticsAzureOutput
        """

        return self.api_client.get(
            '/analytics/outputs/azure/{output_id}',
            path_params={'output_id': output_id},
            type=AnalyticsAzureOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AnalyticsAzureOutputListQueryParams, dict) -> AnalyticsAzureOutput
        """List Microsoft Azure Outputs

        :param query_params: Query parameters
        :type query_params: AnalyticsAzureOutputListQueryParams
        :return: List of Microsoft Azure outputs
        :rtype: AnalyticsAzureOutput
        """

        return self.api_client.get(
            '/analytics/outputs/azure',
            query_params=query_params,
            pagination_response=True,
            type=AnalyticsAzureOutput,
            **kwargs
        )
