# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.https_input import HttpsInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.https.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.https.https_input_list_query_params import HttpsInputListQueryParams


class HttpsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(HttpsApi, self).__init__(
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

    def create(self, https_input, **kwargs):
        # type: (HttpsInput, dict) -> HttpsInput
        """Create HTTPS Input

        :param https_input: The Https input to be created
        :type https_input: HttpsInput, required
        :return: HTTPS input
        :rtype: HttpsInput
        """

        return self.api_client.post(
            '/encoding/inputs/https',
            https_input,
            type=HttpsInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> HttpsInput
        """Delete HTTPS Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: HttpsInput
        """

        return self.api_client.delete(
            '/encoding/inputs/https/{input_id}',
            path_params={'input_id': input_id},
            type=HttpsInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> HttpsInput
        """HTTPS Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: HTTPS input
        :rtype: HttpsInput
        """

        return self.api_client.get(
            '/encoding/inputs/https/{input_id}',
            path_params={'input_id': input_id},
            type=HttpsInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (HttpsInputListQueryParams, dict) -> HttpsInput
        """List HTTPS Inputs

        :param query_params: Query parameters
        :type query_params: HttpsInputListQueryParams
        :return: List of HTTPS inputs
        :rtype: HttpsInput
        """

        return self.api_client.get(
            '/encoding/inputs/https',
            query_params=query_params,
            pagination_response=True,
            type=HttpsInput,
            **kwargs
        )
