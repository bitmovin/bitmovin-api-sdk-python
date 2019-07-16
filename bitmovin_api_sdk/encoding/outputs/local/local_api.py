# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.local_output import LocalOutput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.local.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.local.local_output_list_query_params import LocalOutputListQueryParams


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

    def create(self, local_output, **kwargs):
        # type: (LocalOutput, dict) -> LocalOutput
        """Create Local Output

        :param local_output: The Local output to be created
        :type local_output: LocalOutput, required
        :return: Local output
        :rtype: LocalOutput
        """

        return self.api_client.post(
            '/encoding/outputs/local',
            local_output,
            type=LocalOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> LocalOutput
        """Delete Local Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: LocalOutput
        """

        return self.api_client.delete(
            '/encoding/outputs/local/{output_id}',
            path_params={'output_id': output_id},
            type=LocalOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> LocalOutput
        """Local Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Local output details
        :rtype: LocalOutput
        """

        return self.api_client.get(
            '/encoding/outputs/local/{output_id}',
            path_params={'output_id': output_id},
            type=LocalOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (LocalOutputListQueryParams, dict) -> LocalOutput
        """List Local Outputs

        :param query_params: Query parameters
        :type query_params: LocalOutputListQueryParams
        :return: List of Local outputs
        :rtype: LocalOutput
        """

        return self.api_client.get(
            '/encoding/outputs/local',
            query_params=query_params,
            pagination_response=True,
            type=LocalOutput,
            **kwargs
        )
