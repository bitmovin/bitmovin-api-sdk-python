# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.aspera_input import AsperaInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.aspera.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.aspera.aspera_input_list_query_params import AsperaInputListQueryParams


class AsperaApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AsperaApi, self).__init__(
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

    def create(self, aspera_input, **kwargs):
        # type: (AsperaInput, dict) -> AsperaInput
        """Create Aspera Input

        :param aspera_input: The Aspera input to be created
        :type aspera_input: AsperaInput, required
        :return: Aspera input
        :rtype: AsperaInput
        """

        return self.api_client.post(
            '/encoding/inputs/aspera',
            aspera_input,
            type=AsperaInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> AsperaInput
        """Delete Aspera Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: AsperaInput
        """

        return self.api_client.delete(
            '/encoding/inputs/aspera/{input_id}',
            path_params={'input_id': input_id},
            type=AsperaInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> AsperaInput
        """Aspera Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Aspera input
        :rtype: AsperaInput
        """

        return self.api_client.get(
            '/encoding/inputs/aspera/{input_id}',
            path_params={'input_id': input_id},
            type=AsperaInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AsperaInputListQueryParams, dict) -> AsperaInput
        """List Aspera Inputs

        :param query_params: Query parameters
        :type query_params: AsperaInputListQueryParams
        :return: List of Aspera inputs
        :rtype: AsperaInput
        """

        return self.api_client.get(
            '/encoding/inputs/aspera',
            query_params=query_params,
            pagination_response=True,
            type=AsperaInput,
            **kwargs
        )
