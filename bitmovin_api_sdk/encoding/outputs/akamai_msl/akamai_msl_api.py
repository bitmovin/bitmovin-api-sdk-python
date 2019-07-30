# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.akamai_msl_output import AkamaiMslOutput
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.akamai_msl.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.akamai_msl.akamai_msl_output_list_query_params import AkamaiMslOutputListQueryParams


class AkamaiMslApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(AkamaiMslApi, self).__init__(
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

    def create(self, akamai_msl_output, **kwargs):
        # type: (AkamaiMslOutput, dict) -> AkamaiMslOutput
        """Create Akamai MSL Output

        :param akamai_msl_output: The Akamai MSL output to be created
        :type akamai_msl_output: AkamaiMslOutput, required
        :return: Akamai MSL output
        :rtype: AkamaiMslOutput
        """

        return self.api_client.post(
            '/encoding/outputs/akamai-msl',
            akamai_msl_output,
            type=AkamaiMslOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Akamai MSL Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/outputs/akamai-msl/{output_id}',
            path_params={'output_id': output_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> AkamaiMslOutput
        """Akamai MSL Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Akamai MSL output
        :rtype: AkamaiMslOutput
        """

        return self.api_client.get(
            '/encoding/outputs/akamai-msl/{output_id}',
            path_params={'output_id': output_id},
            type=AkamaiMslOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (AkamaiMslOutputListQueryParams, dict) -> AkamaiMslOutput
        """List Akamai MSL Outputs

        :param query_params: Query parameters
        :type query_params: AkamaiMslOutputListQueryParams
        :return: List of Akamai MSL outputs
        :rtype: AkamaiMslOutput
        """

        return self.api_client.get(
            '/encoding/outputs/akamai-msl',
            query_params=query_params,
            pagination_response=True,
            type=AkamaiMslOutput,
            **kwargs
        )
