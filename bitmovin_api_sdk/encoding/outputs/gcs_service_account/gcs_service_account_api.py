# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.gcs_service_account_output import GcsServiceAccountOutput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.outputs.gcs_service_account.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.outputs.gcs_service_account.gcs_service_account_output_list_query_params import GcsServiceAccountOutputListQueryParams


class GcsServiceAccountApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(GcsServiceAccountApi, self).__init__(
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

    def create(self, gcs_service_account_output, **kwargs):
        # type: (GcsServiceAccountOutput, dict) -> GcsServiceAccountOutput
        """Create Service Account based GCS Output

        :param gcs_service_account_output: The GCS output to be created
        :type gcs_service_account_output: GcsServiceAccountOutput, required
        :return: GCS output
        :rtype: GcsServiceAccountOutput
        """

        return self.api_client.post(
            '/encoding/outputs/gcs-service-account',
            gcs_service_account_output,
            type=GcsServiceAccountOutput,
            **kwargs
        )

    def delete(self, output_id, **kwargs):
        # type: (string_types, dict) -> GcsServiceAccountOutput
        """Delete Service Account based GCS Output

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: Id of the output
        :rtype: GcsServiceAccountOutput
        """

        return self.api_client.delete(
            '/encoding/outputs/gcs-service-account/{output_id}',
            path_params={'output_id': output_id},
            type=GcsServiceAccountOutput,
            **kwargs
        )

    def get(self, output_id, **kwargs):
        # type: (string_types, dict) -> GcsServiceAccountOutput
        """Service Account based GCS Output Details

        :param output_id: Id of the output
        :type output_id: string_types, required
        :return: GCS output
        :rtype: GcsServiceAccountOutput
        """

        return self.api_client.get(
            '/encoding/outputs/gcs-service-account/{output_id}',
            path_params={'output_id': output_id},
            type=GcsServiceAccountOutput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (GcsServiceAccountOutputListQueryParams, dict) -> GcsServiceAccountOutput
        """List Service Account based GCS Outputs

        :param query_params: Query parameters
        :type query_params: GcsServiceAccountOutputListQueryParams
        :return: List of GCS outputs
        :rtype: GcsServiceAccountOutput
        """

        return self.api_client.get(
            '/encoding/outputs/gcs-service-account',
            query_params=query_params,
            pagination_response=True,
            type=GcsServiceAccountOutput,
            **kwargs
        )
