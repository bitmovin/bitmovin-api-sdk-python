# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.gcs_input import GcsInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.gcs.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.gcs.gcs_input_list_query_params import GcsInputListQueryParams


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

    def create(self, gcs_input, **kwargs):
        # type: (GcsInput, dict) -> GcsInput
        """Create GCS Input

        :param gcs_input: The GcsInput to be created
        :type gcs_input: GcsInput, required
        :return: GCS input
        :rtype: GcsInput
        """

        return self.api_client.post(
            '/encoding/inputs/gcs',
            gcs_input,
            type=GcsInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> GcsInput
        """Delete GCS Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: GcsInput
        """

        return self.api_client.delete(
            '/encoding/inputs/gcs/{input_id}',
            path_params={'input_id': input_id},
            type=GcsInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> GcsInput
        """GCS Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: GCS input
        :rtype: GcsInput
        """

        return self.api_client.get(
            '/encoding/inputs/gcs/{input_id}',
            path_params={'input_id': input_id},
            type=GcsInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (GcsInputListQueryParams, dict) -> GcsInput
        """List GCS Inputs

        :param query_params: Query parameters
        :type query_params: GcsInputListQueryParams
        :return: List of GCS inputs
        :rtype: GcsInput
        """

        return self.api_client.get(
            '/encoding/inputs/gcs',
            query_params=query_params,
            pagination_response=True,
            type=GcsInput,
            **kwargs
        )
