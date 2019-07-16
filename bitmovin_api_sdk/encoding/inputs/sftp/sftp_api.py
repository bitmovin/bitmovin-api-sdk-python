# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.sftp_input import SftpInput
from bitmovin_api_sdk.encoding.inputs.sftp.customdata.customdata_api import CustomdataApi
from bitmovin_api_sdk.encoding.inputs.sftp.sftp_input_list_query_params import SftpInputListQueryParams


class SftpApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(SftpApi, self).__init__(
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

    def create(self, sftp_input, **kwargs):
        # type: (SftpInput, dict) -> SftpInput
        """Create SFTP Input

        :param sftp_input: The SFTP input to be created
        :type sftp_input: SftpInput, required
        :return: SFTP input
        :rtype: SftpInput
        """

        return self.api_client.post(
            '/encoding/inputs/sftp',
            sftp_input,
            type=SftpInput,
            **kwargs
        )

    def delete(self, input_id, **kwargs):
        # type: (string_types, dict) -> SftpInput
        """Delete SFTP Input

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: Id of the input
        :rtype: SftpInput
        """

        return self.api_client.delete(
            '/encoding/inputs/sftp/{input_id}',
            path_params={'input_id': input_id},
            type=SftpInput,
            **kwargs
        )

    def get(self, input_id, **kwargs):
        # type: (string_types, dict) -> SftpInput
        """SFTP Input Details

        :param input_id: Id of the input
        :type input_id: string_types, required
        :return: SFTP input
        :rtype: SftpInput
        """

        return self.api_client.get(
            '/encoding/inputs/sftp/{input_id}',
            path_params={'input_id': input_id},
            type=SftpInput,
            **kwargs
        )

    def list(self, query_params=None, **kwargs):
        # type: (SftpInputListQueryParams, dict) -> SftpInput
        """List SFTP Inputs

        :param query_params: Query parameters
        :type query_params: SftpInputListQueryParams
        :return: List of SFTP inputs
        :rtype: SftpInput
        """

        return self.api_client.get(
            '/encoding/inputs/sftp',
            query_params=query_params,
            pagination_response=True,
            type=SftpInput,
            **kwargs
        )
