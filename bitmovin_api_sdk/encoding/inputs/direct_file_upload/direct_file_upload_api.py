# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.bitmovin_response import BitmovinResponse
from bitmovin_api_sdk.models.direct_file_upload_input import DirectFileUploadInput
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.encoding.inputs.direct_file_upload.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.direct_file_upload.direct_file_upload_input_list_query_params import DirectFileUploadInputListQueryParams


class DirectFileUploadApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DirectFileUploadApi, self).__init__(
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

    def create(self, direct_file_upload_input, **kwargs):
        # type: (DirectFileUploadInput, dict) -> DirectFileUploadInput
        """Create Direct File Upload Input

        :param direct_file_upload_input: The Direct File Upload input to be created
        :type direct_file_upload_input: DirectFileUploadInput, required
        :return: Direct File Upload input
        :rtype: DirectFileUploadInput
        """

        return self.api_client.post(
            '/encoding/inputs/direct-file-upload',
            direct_file_upload_input,
            type=DirectFileUploadInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> BitmovinResponse
        """Delete Direct File Upload Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the deleted input
        :rtype: BitmovinResponse
        """

        return self.api_client.delete(
            '/encoding/inputs/direct-file-upload/{input_id}',
            path_params={'input_id': input_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> DirectFileUploadInput
        """Direct File Upload Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Direct File Upload input
        :rtype: DirectFileUploadInput
        """

        return self.api_client.get(
            '/encoding/inputs/direct-file-upload/{input_id}',
            path_params={'input_id': input_id},
            type=DirectFileUploadInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (DirectFileUploadInputListQueryParams, dict) -> DirectFileUploadInput
        """List Direct File Upload Inputs

        :param query_params: Query parameters
        :type query_params: DirectFileUploadInputListQueryParams
        :return: List of Direct File Upload inputs
        :rtype: DirectFileUploadInput
        """

        return self.api_client.get(
            '/encoding/inputs/direct-file-upload',
            query_params=query_params,
            pagination_response=True,
            type=DirectFileUploadInput,
            **kwargs
        )
