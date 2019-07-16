# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.srt_input import SrtInput
from bitmovin_api_sdk.encoding.inputs.srt.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.srt.srt_input_list_query_params import SrtInputListQueryParams


class SrtApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SrtApi, self).__init__(
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

    def create(self, srt_input, **kwargs):
        # type: (SrtInput, dict) -> SrtInput
        """Create SRT input

        :param srt_input: The SrtInput to be created
        :type srt_input: SrtInput, required
        :return: SRT input
        :rtype: SrtInput
        """

        return self.api_client.post(
            '/encoding/inputs/srt',
            srt_input,
            type=SrtInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> SrtInput
        """Delete SRT input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: SrtInput
        """

        return self.api_client.delete(
            '/encoding/inputs/srt/{input_id}',
            path_params={'input_id': input_id},
            type=SrtInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> SrtInput
        """SRT Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: SRT input
        :rtype: SrtInput
        """

        return self.api_client.get(
            '/encoding/inputs/srt/{input_id}',
            path_params={'input_id': input_id},
            type=SrtInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (SrtInputListQueryParams, dict) -> SrtInput
        """List SRT inputs

        :param query_params: Query parameters
        :type query_params: SrtInputListQueryParams
        :return: List of SRT inputs
        :rtype: SrtInput
        """

        return self.api_client.get(
            '/encoding/inputs/srt',
            query_params=query_params,
            pagination_response=True,
            type=SrtInput,
            **kwargs
        )
