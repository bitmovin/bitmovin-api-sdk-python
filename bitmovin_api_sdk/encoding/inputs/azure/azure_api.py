# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.azure_input import AzureInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.azure.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.azure.azure_input_list_query_params import AzureInputListQueryParams


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

    def create(self, azure_input, **kwargs):
        # type: (AzureInput, dict) -> AzureInput
        """Create Azure Input

        :param azure_input: The Azure input to be created
        :type azure_input: AzureInput, required
        :return: Azure input
        :rtype: AzureInput
        """

        return self.api_client.post(
            '/encoding/inputs/azure',
            azure_input,
            type=AzureInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> AzureInput
        """Delete Azure Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: AzureInput
        """

        return self.api_client.delete(
            '/encoding/inputs/azure/{input_id}',
            path_params={'input_id': input_id},
            type=AzureInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> AzureInput
        """Azure Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Azure input
        :rtype: AzureInput
        """

        return self.api_client.get(
            '/encoding/inputs/azure/{input_id}',
            path_params={'input_id': input_id},
            type=AzureInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AzureInputListQueryParams, dict) -> AzureInput
        """List Azure Inputs

        :param query_params: Query parameters
        :type query_params: AzureInputListQueryParams
        :return: List of Azure inputs
        :rtype: AzureInput
        """

        return self.api_client.get(
            '/encoding/inputs/azure',
            query_params=query_params,
            pagination_response=True,
            type=AzureInput,
            **kwargs
        )
