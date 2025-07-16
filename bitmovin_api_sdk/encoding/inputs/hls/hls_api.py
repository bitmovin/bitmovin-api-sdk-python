# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.hls_input import HlsInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.hls.hls_input_list_query_params import HlsInputListQueryParams


class HlsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(HlsApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, hls_input, **kwargs):
        # type: (HlsInput, dict) -> HlsInput
        """Create HLS input

        :param hls_input: The HLSInput to be created
        :type hls_input: HlsInput, required
        :return: HLS input
        :rtype: HlsInput
        """

        return self.api_client.post(
            '/encoding/inputs/hls',
            hls_input,
            type=HlsInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> HlsInput
        """Delete HLS Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: HlsInput
        """

        return self.api_client.delete(
            '/encoding/inputs/hls/{input_id}',
            path_params={'input_id': input_id},
            type=HlsInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> HlsInput
        """HLS Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: HLS input
        :rtype: HlsInput
        """

        return self.api_client.get(
            '/encoding/inputs/hls/{input_id}',
            path_params={'input_id': input_id},
            type=HlsInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (HlsInputListQueryParams, dict) -> HlsInput
        """List HLS inputs

        :param query_params: Query parameters
        :type query_params: HlsInputListQueryParams
        :return: List of HLS inputs
        :rtype: HlsInput
        """

        return self.api_client.get(
            '/encoding/inputs/hls',
            query_params=query_params,
            pagination_response=True,
            type=HlsInput,
            **kwargs
        )
