# coding: utf-8

from __future__ import absolute_import

from bitmovin.common import BaseApi
from bitmovin.common.poscheck import poscheck_except

from bitmovin.models.azure_input import AzureInput
from bitmovin.models.response_envelope import ResponseEnvelope
from bitmovin.models.response_error import ResponseError
from bitmovin.encoding.inputs.azure.customdata.customdata_api import CustomdataApi
from bitmovin.encoding.inputs.azure.azure_input_list_query_params import AzureInputListQueryParams


class AzureApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, logger=None):
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
        """Create Azure Input"""

        return self.api_client.post(
            '/encoding/inputs/azure',
            azure_input,
            type=AzureInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        """Delete Azure Input"""

        return self.api_client.delete(
            '/encoding/inputs/azure/{input_id}',
            path_params={'input_id': input_id},
            type=AzureInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        """Azure Input Details"""

        return self.api_client.get(
            '/encoding/inputs/azure/{input_id}',
            path_params={'input_id': input_id},
            type=AzureInput,
            **kwargs
        )

    def list(self, query_params: AzureInputListQueryParams = None, **kwargs):
        """List Azure Inputs"""

        return self.api_client.get(
            '/encoding/inputs/azure',
            query_params=query_params,
            pagination_response=True,
            type=AzureInput,
            **kwargs
        )
