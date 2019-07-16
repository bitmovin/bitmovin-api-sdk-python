# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.local_input import LocalInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.local.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.local.local_input_list_query_params import LocalInputListQueryParams


class LocalApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(LocalApi, self).__init__(
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

    def create(self, local_input, **kwargs):
        # type: (LocalInput, dict) -> LocalInput
        """Create Local Input

        :param local_input: The LocalInput to be created.
        :type local_input: LocalInput, required
        :return: Local input
        :rtype: LocalInput
        """

        return self.api_client.post(
            '/encoding/inputs/local',
            local_input,
            type=LocalInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Local Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/inputs/local/{input_id}',
            path_params={'input_id': input_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> LocalInput
        """Local Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Local input details
        :rtype: LocalInput
        """

        return self.api_client.get(
            '/encoding/inputs/local/{input_id}',
            path_params={'input_id': input_id},
            type=LocalInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (LocalInputListQueryParams, dict) -> LocalInput
        """List Local Inputs

        :param query_params: Query parameters
        :type query_params: LocalInputListQueryParams
        :return: List of local inputs
        :rtype: LocalInput
        """

        return self.api_client.get(
            '/encoding/inputs/local',
            query_params=query_params,
            pagination_response=True,
            type=LocalInput,
            **kwargs
        )
