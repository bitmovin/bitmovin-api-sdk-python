# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.moq_output import MoqOutput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.moq.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.moq.moq_output_list_query_params import MoqOutputListQueryParams


class MoqApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(MoqApi, self).__init__(
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

    def create(self, moq_output, **kwargs):
        # type: (MoqOutput, dict) -> MoqOutput
        """Create MoQ Output

        :param moq_output: The MoQ output to be created
        :type moq_output: MoqOutput, required
        :return: MoQ output
        :rtype: MoqOutput
        """

        return self.api_client.post(
            '/encoding/outputs/moq',
            moq_output,
            type=MoqOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete MoQ Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/outputs/moq/{output_id}',
            path_params={'output_id': output_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> MoqOutput
        """Get MoQ Output details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: MoQ output
        :rtype: MoqOutput
        """

        return self.api_client.get(
            '/encoding/outputs/moq/{output_id}',
            path_params={'output_id': output_id},
            type=MoqOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (MoqOutputListQueryParams, dict) -> MoqOutput
        """List MoQ Outputs

        :param query_params: Query parameters
        :type query_params: MoqOutputListQueryParams
        :return: List of MoQ outputs
        :rtype: MoqOutput
        """

        return self.api_client.get(
            '/encoding/outputs/moq',
            query_params=query_params,
            pagination_response=True,
            type=MoqOutput,
            **kwargs
        )
