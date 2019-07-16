# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.zixi_input import ZixiInput
from bitmovin_api_sdk.encoding.inputs.zixi.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.zixi.zixi_input_list_query_params import ZixiInputListQueryParams


class ZixiApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(ZixiApi, self).__init__(
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

    def create(self, zixi_input, **kwargs):
        # type: (ZixiInput, dict) -> ZixiInput
        """Create Zixi input

        :param zixi_input: The ZixiInput to be created
        :type zixi_input: ZixiInput, required
        :return: Zixi input
        :rtype: ZixiInput
        """

        return self.api_client.post(
            '/encoding/inputs/zixi',
            zixi_input,
            type=ZixiInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> ZixiInput
        """Delete Zixi input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: ZixiInput
        """

        return self.api_client.delete(
            '/encoding/inputs/zixi/{input_id}',
            path_params={'input_id': input_id},
            type=ZixiInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> ZixiInput
        """Zixi Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Zixi input
        :rtype: ZixiInput
        """

        return self.api_client.get(
            '/encoding/inputs/zixi/{input_id}',
            path_params={'input_id': input_id},
            type=ZixiInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (ZixiInputListQueryParams, dict) -> ZixiInput
        """List Zixi inputs

        :param query_params: Query parameters
        :type query_params: ZixiInputListQueryParams
        :return: List of Zixi inputs
        :rtype: ZixiInput
        """

        return self.api_client.get(
            '/encoding/inputs/zixi',
            query_params=query_params,
            pagination_response=True,
            type=ZixiInput,
            **kwargs
        )
