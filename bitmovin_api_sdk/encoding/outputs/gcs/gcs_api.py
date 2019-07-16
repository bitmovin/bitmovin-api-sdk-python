# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.gcs_output import GcsOutput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.gcs.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.gcs.gcs_output_list_query_params import GcsOutputListQueryParams


class GcsApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(GcsApi, self).__init__(
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

    def create(self, gcs_output, **kwargs):
        # type: (GcsOutput, dict) -> GcsOutput
        """Create GCS Output

        :param gcs_output: The GCS output to be created
        :type gcs_output: GcsOutput, required
        :return: GCS output
        :rtype: GcsOutput
        """

        return self.api_client.post(
            '/encoding/outputs/gcs',
            gcs_output,
            type=GcsOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> GcsOutput
        """Delete GCS Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: GcsOutput
        """

        return self.api_client.delete(
            '/encoding/outputs/gcs/{output_id}',
            path_params={'output_id': output_id},
            type=GcsOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> GcsOutput
        """GCS Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: GCS output
        :rtype: GcsOutput
        """

        return self.api_client.get(
            '/encoding/outputs/gcs/{output_id}',
            path_params={'output_id': output_id},
            type=GcsOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (GcsOutputListQueryParams, dict) -> GcsOutput
        """List GCS Outputs

        :param query_params: Query parameters
        :type query_params: GcsOutputListQueryParams
        :return: List of GCS outputs
        :rtype: GcsOutput
        """

        return self.api_client.get(
            '/encoding/outputs/gcs',
            query_params=query_params,
            pagination_response=True,
            type=GcsOutput,
            **kwargs
        )
