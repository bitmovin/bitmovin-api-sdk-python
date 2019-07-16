# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.azure_output import AzureOutput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.azure.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.azure.azure_output_list_query_params import AzureOutputListQueryParams


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

    def create(self, azure_output, **kwargs):
        # type: (AzureOutput, dict) -> AzureOutput
        """Create Azure Output

        :param azure_output: The Azure output to be created
        :type azure_output: AzureOutput, required
        :return: Azure output
        :rtype: AzureOutput
        """

        return self.api_client.post(
            '/encoding/outputs/azure',
            azure_output,
            type=AzureOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> AzureOutput
        """Delete Azure Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: AzureOutput
        """

        return self.api_client.delete(
            '/encoding/outputs/azure/{output_id}',
            path_params={'output_id': output_id},
            type=AzureOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> AzureOutput
        """Azure Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Azure output
        :rtype: AzureOutput
        """

        return self.api_client.get(
            '/encoding/outputs/azure/{output_id}',
            path_params={'output_id': output_id},
            type=AzureOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AzureOutputListQueryParams, dict) -> AzureOutput
        """List Azure Outputs

        :param query_params: Query parameters
        :type query_params: AzureOutputListQueryParams
        :return: List of Azure outputs
        :rtype: AzureOutput
        """

        return self.api_client.get(
            '/encoding/outputs/azure',
            query_params=query_params,
            pagination_response=True,
            type=AzureOutput,
            **kwargs
        )
