# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.http_input import HttpInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.http.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.http.http_input_list_query_params import HttpInputListQueryParams


class HttpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(HttpApi, self).__init__(
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

    def create(self, http_input, **kwargs):
        # type: (HttpInput, dict) -> HttpInput
        """Create HTTP Input

        :param http_input: The HTTP input to be created
        :type http_input: HttpInput, required
        :return: HTTP input
        :rtype: HttpInput
        """

        return self.api_client.post(
            '/encoding/inputs/http',
            http_input,
            type=HttpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> HttpInput
        """Delete HTTP Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: HttpInput
        """

        return self.api_client.delete(
            '/encoding/inputs/http/{input_id}',
            path_params={'input_id': input_id},
            type=HttpInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> HttpInput
        """HTTP Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: HTTP input
        :rtype: HttpInput
        """

        return self.api_client.get(
            '/encoding/inputs/http/{input_id}',
            path_params={'input_id': input_id},
            type=HttpInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (HttpInputListQueryParams, dict) -> HttpInput
        """List HTTP Inputs

        :param query_params: Query parameters
        :type query_params: HttpInputListQueryParams
        :return: List of HTTP inputs
        :rtype: HttpInput
        """

        return self.api_client.get(
            '/encoding/inputs/http',
            query_params=query_params,
            pagination_response=True,
            type=HttpInput,
            **kwargs
        )
