# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.gcs_service_account_input import GcsServiceAccountInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.gcs_service_account.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.gcs_service_account.gcs_service_account_input_list_query_params import GcsServiceAccountInputListQueryParams


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

    def create(self, gcs_service_account_input, **kwargs):
        # type: (GcsServiceAccountInput, dict) -> GcsServiceAccountInput
        """Create Service Account based GCS Input

        :param gcs_service_account_input: The GcsInput to be created
        :type gcs_service_account_input: GcsServiceAccountInput, required
        :return: Service Account based GCS input
        :rtype: GcsServiceAccountInput
        """

        return self.api_client.post(
            '/encoding/inputs/gcs-service-account',
            gcs_service_account_input,
            type=GcsServiceAccountInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> GcsServiceAccountInput
        """Delete Service Account based GCS Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: GcsServiceAccountInput
        """

        return self.api_client.delete(
            '/encoding/inputs/gcs-service-account/{input_id}',
            path_params={'input_id': input_id},
            type=GcsServiceAccountInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> GcsServiceAccountInput
        """List Service Account based GCS Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: GCS input
        :rtype: GcsServiceAccountInput
        """

        return self.api_client.get(
            '/encoding/inputs/gcs-service-account/{input_id}',
            path_params={'input_id': input_id},
            type=GcsServiceAccountInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (GcsServiceAccountInputListQueryParams, dict) -> GcsServiceAccountInput
        """List Service Account based GCS Inputs

        :param query_params: Query parameters
        :type query_params: GcsServiceAccountInputListQueryParams
        :return: List of GCS inputs
        :rtype: GcsServiceAccountInput
        """

        return self.api_client.get(
            '/encoding/inputs/gcs-service-account',
            query_params=query_params,
            pagination_response=True,
            type=GcsServiceAccountInput,
            **kwargs
        )
